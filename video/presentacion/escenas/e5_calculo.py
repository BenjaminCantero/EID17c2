"""Escena 5: cálculo explícito y tabla de signos."""

from manim import *

from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_CERO, COLOR_NEG, COLOR_POS, COLOR_X, texto


# (columna, color) de la tabla de signos; la columna 1 son las etiquetas.
COLORES_COLUMNAS = [
    (2, COLOR_POS),
    (3, COLOR_CERO),
    (4, COLOR_NEG),
    (5, COLOR_CERO),
    (6, COLOR_POS),
]


class Calculo(EscenaNarrada):
    hablante = "calculo"

    def construct(self):
        self.mostrar_hablante()

        titulo = texto(
            "Comprobación con cálculo exacto",
            38,
            weight=BOLD,
        ).to_edge(UP)

        self.play(Write(titulo))

        lineas = self.mostrar_integral(titulo)
        caja = self.mostrar_derivada(lineas)
        ceros = self.mostrar_ceros(caja)

        self.mostrar_tabla()
        self.mostrar_valores(ceros)
        self.limpiar()

    def mostrar_integral(self, titulo):
        lineas = VGroup(
            MathTex(
                r"A(x)=\int_{-2}^{x}\left(t^2-2t-3\right)dt"
            ),
            MathTex(
                r"=\left[\frac{t^3}{3}-t^2-3t\right]_{-2}^{x}"
            ),
            MathTex(
                r"=\left(\frac{x^3}{3}-x^2-3x\right)"
                r"-\left(-\frac{8}{3}-4+6\right)"
            ),
            MathTex(
                r"=\frac{x^3}{3}-x^2-3x+\frac{2}{3}",
                color=COLOR_A,
            ),
        ).scale(0.62).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.2,
        )

        lineas.next_to(
            titulo,
            DOWN,
            buff=0.35,
        ).to_edge(LEFT, buff=0.6)

        for ln in lineas:
            self.play(Write(ln), run_time=1.6)
            self.wait(3)

        return lineas

    def mostrar_derivada(self, lineas):
        derivada = MathTex(
            r"A'(x)=x^2-2x-3=f(x)",
            font_size=38,
            color=COLOR_A,
        )

        caja = SurroundingRectangle(
            derivada,
            color=COLOR_X,
            buff=0.18,
        )

        VGroup(
            derivada,
            caja,
        ).to_edge(RIGHT, buff=0.6).align_to(lineas, UP)

        self.play(
            Write(derivada),
            Create(caja),
        )

        self.wait(5)
        return caja

    def mostrar_ceros(self, caja):
        ceros = VGroup(
            MathTex(
                r"f(x)=(x-3)(x+1)=0",
                font_size=32,
            ),
            MathTex(
                r"\Rightarrow x=-1\ \text{o}\ x=3",
                font_size=32,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15,
        )

        ceros.next_to(
            caja,
            DOWN,
            buff=0.35,
        ).align_to(caja, LEFT)

        self.play(Write(ceros))
        self.wait(4)

        return ceros

    def mostrar_tabla(self):
        tabla = MathTable(
            [
                [
                    r"(-2,-1)",
                    r"-1",
                    r"(-1,3)",
                    r"3",
                    r"(3,4)",
                ],
                [
                    r"+",
                    r"0",
                    r"-",
                    r"0",
                    r"+",
                ],
                [
                    r"\nearrow",
                    r"\text{max}",
                    r"\searrow",
                    r"\text{min}",
                    r"\nearrow",
                ],
            ],
            row_labels=[
                MathTex("x"),
                MathTex("f(x)=A'(x)"),
                MathTex("A(x)"),
            ],
            include_outer_lines=True,
            element_to_mobject_config={
                "font_size": 44,
            },
            line_config={
                "stroke_width": 1.5,
                "color": GRAY_B,
            },
        ).scale(0.55).to_edge(DOWN, buff=0.7)

        for col_idx, col in COLORES_COLUMNAS:
            tabla.get_entries(
                (2, col_idx)
            ).set_color(col)

            tabla.get_entries(
                (3, col_idx)
            ).set_color(col)

        self.play(
            Create(tabla),
            run_time=2.5,
        )
        self.wait(6)

    def mostrar_valores(self, ceros):
        valores = VGroup(
            MathTex(
                r"A(-1)=\frac{7}{3}\approx 2.33"
                r"\ \text{(max. local)}",
                font_size=32,
                color=COLOR_A,
            ),
            MathTex(
                r"A(3)=-\frac{25}{3}\approx -8.33"
                r"\ \text{(min. local)}",
                font_size=32,
                color=COLOR_A,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15,
        ).next_to(
            ceros,
            DOWN,
            buff=0.35,
        ).align_to(ceros, LEFT)

        self.play(Write(valores))
        self.wait(6)
