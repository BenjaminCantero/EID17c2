"""Escena 1: Portada y pregunta central."""

from manim import *

from ...datos_grupo import CURSO, GRUPO, NOMBRES
from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_X, texto


class Portada(EscenaNarrada):
    hablante = "portada"

    def construct(self):
        titulo = texto("La pendiente de la acumulación", 48, weight=BOLD)
        sub = texto(f"{CURSO}  ·  {GRUPO}", 26, color=GRAY_B)
        integrantes = texto("  ·  ".join(NOMBRES), 24, color=GRAY_A)
        cab = VGroup(titulo, sub, integrantes).arrange(DOWN, buff=0.3).to_edge(UP, buff=0.8)

        pregunta = VGroup(
            texto("Pregunta central", 30, color=COLOR_X),
            texto("¿Cómo se relaciona el valor de f(x)", 34),
            texto("con la pendiente de la función de acumulación A(x)?", 34),
        ).arrange(DOWN, buff=0.25).next_to(cab, DOWN, buff=0.9)

        formula = MathTex(r"A(x)=\int_{a}^{x} f(t)\,dt", font_size=52, color=COLOR_A)
        formula.next_to(pregunta, DOWN, buff=0.6)

        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(sub, shift=UP * 0.2), FadeIn(integrantes, shift=UP * 0.2))
        self.mostrar_hablante()
        self.wait(3)
        self.play(FadeIn(pregunta, shift=UP * 0.3), run_time=1.5)
        self.wait(5)
        self.play(Write(formula))
        self.wait(7)
        self.limpiar()
