"""Piezas visuales reutilizadas por varias escenas."""

import subprocess
from pathlib import Path

import av
from manim import DL, DR, GRAY_A, FadeOut, Group, Scene, VGroup

from ..datos_grupo import AUDIOS, HABLA, NOMBRES
from .estilo import texto


RAIZ = Path(__file__).resolve().parents[2]
CARPETA_AUDIOS = RAIZ / "audios"
CARPETA_NORMALIZADOS = RAIZ / "media" / "audios_normalizados"
VOLUMEN_LUFS = -16

ORDEN_ESCENAS = {
    "portada": 1,
    "definicion": 2,
    "dos_graficas": 3,
    "franja": 4,
    "calculo": 5,
    "contraejemplo": 6,
    "cierre": 7,
}


def etiqueta_hablante(clave):
    nombre = NOMBRES[HABLA[clave]]
    caja = VGroup(texto("Explica: " + nombre, 20, color=GRAY_A))
    caja.to_corner(DL, buff=0.25)
    return caja


def etiqueta_escena(clave):
    indicador = texto(f"{ORDEN_ESCENAS[clave]} / {len(ORDEN_ESCENAS)}", 18, color=GRAY_A)
    return indicador.to_corner(DR, buff=0.25)


def audio_normalizado(nombre):
    """Copia .wav con el volumen igualado entre narradores; el original no se toca."""
    original = CARPETA_AUDIOS / nombre
    destino = CARPETA_NORMALIZADOS / (original.stem + ".wav")
    CARPETA_NORMALIZADOS.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-i", str(original),
         "-af", f"loudnorm=I={VOLUMEN_LUFS}:TP=-1.5:LRA=11", "-ar", "48000", str(destino)],
        check=True,
    )
    return destino


def duracion_audio(ruta):
    with av.open(str(ruta)) as contenedor:
        return contenedor.duration / av.time_base


class EscenaNarrada(Scene):
    hablante = None

    def setup(self):
        ruta = audio_normalizado(AUDIOS[self.hablante])
        self.add_sound(str(ruta))
        self.fin_audio = duracion_audio(ruta)

    def tear_down(self):
        # Si la narración dura más que las animaciones, espera a que termine.
        restante = self.fin_audio - self.time
        if restante > 0:
            self.wait(restante)

    def mostrar_hablante(self):
        self.add(etiqueta_hablante(self.hablante), etiqueta_escena(self.hablante))

    def limpiar(self):
        for mob in self.mobjects:
            mob.clear_updaters()
        self.play(FadeOut(Group(*self.mobjects)))
