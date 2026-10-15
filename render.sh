#!/usr/bin/env bash
# Renderiza todas las escenas y las une en un solo video.
#
# Uso:
#   ./render.sh          calidad alta (1080p60)  → video_final.mp4
#   ./render.sh l        calidad baja (480p15), para revisar rápido
#   ./render.sh m|h|k    media (720p30), alta (1080p60), 4K (2160p60)
#
# Requiere LaTeX, ffmpeg y manim. Si existe .venv/ se usa su manim:
#   python -m venv .venv && .venv/bin/pip install -r requirements.txt
# Para usar un manim de otro entorno: MANIM=/ruta/a/manim ./render.sh

set -euo pipefail
cd "$(dirname "$0")"

CALIDAD="${1:-h}"
if [[ -z "${MANIM:-}" && -x .venv/bin/manim ]]; then
    MANIM=".venv/bin/manim"
fi
MANIM="${MANIM:-manim}"
SALIDA="video_final.mp4"

case "$CALIDAD" in
    l) CARPETA="480p15" ;;
    m) CARPETA="720p30" ;;
    h) CARPETA="1080p60" ;;
    k) CARPETA="2160p60" ;;
    *) echo "Calidad inválida: '$CALIDAD' (usar l, m, h o k)" >&2; exit 1 ;;
esac

ESCENAS=(
    Escena1_Portada
    Escena2_Definicion
    Escena3_DosGraficas
    Escena4_Franja
    Escena5_Calculo
    Escena6_Contraejemplo
    Escena7_Cierre
)

for cmd in "$MANIM" ffmpeg latex; do
    command -v "$cmd" >/dev/null || {
        echo "Falta '$cmd'." >&2
        [[ "$cmd" == "$MANIM" ]] && echo "Instalar con: python -m venv .venv && .venv/bin/pip install -r requirements.txt" >&2
        exit 1
    }
done

echo "==> Renderizando ${#ESCENAS[@]} escenas en calidad '$CALIDAD' ($CARPETA)"
"$MANIM" "-q$CALIDAD" escenas.py "${ESCENAS[@]}"

DIR="media/videos/escenas/$CARPETA"
LISTA="$(mktemp)"
trap 'rm -f "$LISTA"' EXIT
for escena in "${ESCENAS[@]}"; do
    archivo="$DIR/$escena.mp4"
    [[ -f "$archivo" ]] || { echo "No se generó $archivo" >&2; exit 1; }
    echo "file '$PWD/$archivo'" >> "$LISTA"
done

echo "==> Uniendo escenas en $SALIDA"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$LISTA" -c copy "$SALIDA"

DURACION="$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$SALIDA")"
echo "==> Listo: $SALIDA ($(printf '%.0f' "$DURACION") s)"
