"""Piezas visuales reutilizadas por varias escenas."""

from manim import DL, DR, GRAY_A, FadeOut, Group, Scene, VGroup

from ..datos_grupo import HABLA, NOMBRES
from .estilo import texto


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
    """Rótulo en la esquina que identifica quién está explicando (rúbrica V6c)."""
    nombre = NOMBRES[HABLA[clave]]
    caja = VGroup(texto("Explica: " + nombre, 20, color=GRAY_A))
    caja.to_corner(DL, buff=0.25)
    return caja


def etiqueta_escena(clave):
    indicador = texto(f"{ORDEN_ESCENAS[clave]} / {len(ORDEN_ESCENAS)}", 18, color=GRAY_A)
    return indicador.to_corner(DR, buff=0.25)


class EscenaNarrada(Scene):
    """Escena con rótulo del narrador. Las subclases definen `hablante`."""

    hablante = None

    def mostrar_hablante(self):
        self.add(etiqueta_hablante(self.hablante), etiqueta_escena(self.hablante))

    def limpiar(self):
        self.play(FadeOut(Group(*self.mobjects)))
