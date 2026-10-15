"""ESCENA 2 — Definición, símbolos y teorema                 (~55 s)"""

from manim import *

from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_F, COLOR_POS, COLOR_X, texto


class Definicion(EscenaNarrada):
    hablante = "definicion"

    def construct(self):
        self.mostrar_hablante()
        titulo = texto("La función de acumulación", 40, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        formula = self.mostrar_formula(titulo)
        explicaciones = self.explicar_simbolos(formula)
        self.mostrar_interpretacion(explicaciones)
        self.mostrar_teorema(formula)
        self.limpiar()

    def mostrar_formula(self, titulo):
        # Cada trozo de la fórmula es un objeto separado para poder señalarlo.
        formula = MathTex(
            "A(", "x", ")", "=", r"\int_{", "a", "}^{", "x", "}", "f(", "t", r")\,d", "t",
            font_size=72,
        )
        formula.next_to(titulo, DOWN, buff=0.7)
        self.play(Write(formula), run_time=2)
        self.wait(4)
        return formula

    def explicar_simbolos(self, formula):
        partes = [
            (formula[5], COLOR_POS, "a: punto fijo donde empezamos a acumular"),
            (VGroup(formula[1], formula[7]), COLOR_X, "x: extremo variable; A depende de x"),
            (VGroup(formula[10], formula[12]), BLUE_B, "t: variable de integración (muda)"),
            (VGroup(formula[9], formula[10], formula[11]), COLOR_F, "f(t): la función que se integra"),
        ]
        explicaciones = VGroup(*[texto(frase, 28, color=col) for _, col, frase in partes])
        explicaciones.arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(formula, DOWN, buff=0.7)

        for (obj, col, _), linea in zip(partes, explicaciones):
            self.play(obj.animate.set_color(col), FadeIn(linea, shift=RIGHT * 0.2))
            self.play(Indicate(obj, color=col, scale_factor=1.3))
            self.wait(3)
        return explicaciones

    def mostrar_interpretacion(self, explicaciones):
        interpretacion = texto(
            "A(x) = área con signo entre la gráfica de f y el eje, desde a hasta x",
            26, color=GRAY_A,
        ).next_to(explicaciones, DOWN, buff=0.5)
        self.play(FadeIn(interpretacion))
        self.wait(6)
        self.play(FadeOut(explicaciones), FadeOut(interpretacion))

    def mostrar_teorema(self, formula):
        """Teorema Fundamental del Cálculo (parte 1)."""
        tfc_titulo = texto("Teorema Fundamental del Cálculo (parte 1)", 32, color=COLOR_X)
        hipotesis = texto("Si f es continua en un intervalo que contiene a a y a x, entonces", 28)
        conclusion = MathTex(r"A'(x) = f(x)", font_size=64, color=COLOR_A)
        caja = SurroundingRectangle(conclusion, color=COLOR_X, buff=0.25)
        bloque = VGroup(tfc_titulo, hipotesis, VGroup(conclusion, caja)).arrange(DOWN, buff=0.35)
        bloque.next_to(formula, DOWN, buff=0.4)

        self.play(FadeIn(tfc_titulo))
        self.play(FadeIn(hipotesis))
        self.wait(4)
        self.play(Write(conclusion), Create(caja))
        self.wait(4)

        lectura = texto("La pendiente de A en cada punto es el valor de f en ese punto.", 28, color=COLOR_A)
        lectura.next_to(bloque, DOWN, buff=0.3)
        self.play(FadeIn(lectura, shift=UP * 0.2))
        self.wait(6)
