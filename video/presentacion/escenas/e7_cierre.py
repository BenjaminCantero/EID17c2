"""ESCENA 7 — Respuesta a la pregunta central, fuentes e IA   (~55 s)"""

from manim import *

from ...datos_grupo import DECLARACION_IA, FUENTES, GRUPO, NOMBRES
from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_CERO, COLOR_NEG, COLOR_POS, COLOR_X, texto


class Cierre(EscenaNarrada):
    hablante = "cierre"

    def construct(self):
        self.mostrar_hablante()
        self.mostrar_respuesta()
        self.limpiar()
        self.mostrar_hablante()
        self.mostrar_creditos()
        self.limpiar()

    def mostrar_respuesta(self):
        titulo = texto("Respuesta a la pregunta central", 40, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        clave = MathTex(r"A'(x)=f(x)", font_size=70, color=COLOR_A)
        caja = SurroundingRectangle(clave, color=COLOR_X, buff=0.2)
        VGroup(clave, caja).next_to(titulo, DOWN, buff=0.35)
        self.play(Write(clave), Create(caja))
        self.wait(3)

        frase = texto("El valor de f(x) ES la pendiente de A en x.", 32)
        frase.next_to(caja, DOWN, buff=0.35)
        self.play(FadeIn(frase))
        self.wait(3)

        casos = VGroup(
            texto("f(x) > 0   ⇒   A crece", 30, color=COLOR_POS),
            texto("f(x) < 0   ⇒   A decrece", 30, color=COLOR_NEG),
            texto("f(x) = 0   ⇒   tangente horizontal (extremo si f cambia de signo)", 30, color=COLOR_CERO),
            texto("|f(x)| grande   ⇒   A cambia más rápido", 30, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(frase, DOWN, buff=0.35)
        for c in casos:
            self.play(FadeIn(c, shift=RIGHT * 0.2))
            self.wait(3.5)

        cierre = texto(
            "Integrar y derivar son procesos inversos: Teorema Fundamental del Cálculo.",
            24, color=COLOR_X,
        ).next_to(casos, DOWN, buff=0.4)
        self.play(FadeIn(cierre))
        self.wait(6)

    def mostrar_creditos(self):
        """Fuentes y declaración de IA (rúbrica V7)."""
        t2 = texto("Fuentes y recursos", 36, weight=BOLD).to_edge(UP)
        lista = VGroup(*[texto("• " + s, 20) for s in FUENTES]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ia = VGroup(*[texto(s, 20, color=GRAY_A) for s in DECLARACION_IA]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        equipo = texto(f"{GRUPO}: " + ", ".join(NOMBRES), 22, color=COLOR_X)
        bloque = VGroup(lista, ia, equipo).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(t2, DOWN, buff=0.6)
        if bloque.width > 13:
            bloque.scale_to_fit_width(13)
        self.play(FadeIn(t2), FadeIn(bloque))
        self.wait(7)
