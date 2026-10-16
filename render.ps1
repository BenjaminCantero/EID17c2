# Renderiza todas las escenas y las une en un solo video.
#
# Uso (desde PowerShell, en la raíz del proyecto):
#   .\render.ps1          calidad alta (1080p60)  -> MAT1188_EID_G17_2026.mp4
#   .\render.ps1 l        calidad baja (480p15), para revisar rápido
#   .\render.ps1 m        calidad media (720p30)
#   .\render.ps1 k        4K (2160p60)
#
# Requiere LaTeX, ffmpeg y manim. Si existe .venv\ se usa su manim:
#   python -m venv .venv
#   .venv\Scripts\pip install -r requirements.txt

param(
    [string]$Calidad = "h"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# ---------- Selección de manim ----------
if ($env:MANIM) {
    $MANIM = $env:MANIM
} elseif (Test-Path ".venv\Scripts\manim.exe") {
    $MANIM = ".venv\Scripts\manim.exe"
} else {
    $MANIM = "manim"
}

$SALIDA = "MAT1188_EID_G17_2026.mp4"

# ---------- Carpeta según calidad ----------
switch ($Calidad) {
    "l" { $CARPETA = "480p15"  }
    "m" { $CARPETA = "720p30"  }
    "h" { $CARPETA = "1080p60" }
    "k" { $CARPETA = "2160p60" }
    default {
        Write-Error "Calidad invalida: '$Calidad' (usar l, m, h o k)"
        exit 1
    }
}

# ---------- Verificar dependencias ----------
foreach ($cmd in @($MANIM, "ffmpeg", "latex")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Error "Falta '$cmd'. Asegurate de tener LaTeX, ffmpeg y manim instalados."
        exit 1
    }
}

# ---------- Escenas a renderizar ----------
$ESCENAS = @(
    "Escena1_Portada",
    "Escena2_Definicion",
    "Escena3_DosGraficas",
    "Escena4_Franja",
    "Escena5_Calculo",
    "Escena6_Contraejemplo",
    "Escena7_Cierre"
)

Write-Host "==> Renderizando $($ESCENAS.Count) escenas en calidad '$Calidad' ($CARPETA)"
& $MANIM "-q$Calidad" escenas.py @ESCENAS

# ---------- Armar lista de archivos para ffmpeg ----------
$DIR = "media\videos\escenas\$CARPETA"
$LISTA = [System.IO.Path]::GetTempFileName()

try {
    foreach ($escena in $ESCENAS) {
        $archivo = Join-Path $DIR "$escena.mp4"
        if (-not (Test-Path $archivo)) {
            Write-Error "No se genero $archivo"
            exit 1
        }
        $rutaAbsoluta = Resolve-Path $archivo
        Add-Content -Path $LISTA -Value "file '$rutaAbsoluta'"
    }

    # ---------- Unir escenas ----------
    Write-Host "==> Uniendo escenas en $SALIDA"
    & ffmpeg -loglevel error -y -f concat -safe 0 -i $LISTA -c copy $SALIDA

    # ---------- Duración final ----------
    $duracion = & ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $SALIDA
    Write-Host ("==> Listo: $SALIDA ({0} s)" -f [math]::Round([double]$duracion))
} finally {
    Remove-Item $LISTA -ErrorAction SilentlyContinue
}
