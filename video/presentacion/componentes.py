"""Piezas visuales reutilizadas por varias escenas."""

from manim import DL, GRAY_A, FadeOut, Group, Scene, VGroup

from ..datos_grupo import HABLA, NOMBRES
from .estilo import texto


def etiqueta_hablante(clave):
    """Rótulo en la esquina que identifica quién está explicando (rúbrica V6c)."""
    nombre = NOMBRES[HABLA[clave]]
    caja = VGroup(texto("Explica: " + nombre, 20, color=GRAY_A))
    caja.to_corner(DL, buff=0.25)
    return caja


class EscenaNarrada(Scene):
    """Escena con rótulo del narrador. Las subclases definen `hablante`."""

    hablante = None

    def mostrar_hablante(self):
        self.add(etiqueta_hablante(self.hablante))

    def limpiar(self):
        self.play(FadeOut(Group(*self.mobjects)))
