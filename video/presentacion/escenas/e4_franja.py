"""ESCENA 4 — ¿Por qué A'(x) = f(x)? La franja delgada        (~60 s)"""

from manim import *

from ...dominio.ejemplos import A, f
from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_F, COLOR_POS, COLOR_X, texto

X0 = -1.6  # punto donde estudiamos la pendiente

EXPLICACIONES = [
    "El área nueva al avanzar de x a x+h es la franja verde.",
    "Si h es pequeño, la franja es casi un rectángulo.",
    "Dividimos por h: es la pendiente de una secante de A.",
    "Al achicar h, la aproximación se vuelve exacta.",
]


def nota_de(i):
    t = texto(EXPLICACIONES[i], 22, color=GRAY_A)
    if t.width > 6.2:
        t.scale_to_fit_width(6.2)
    return t


class Franja(EscenaNarrada):
    hablante = "franja"

    def construct(self):
        self.mostrar_hablante()
        titulo = texto("¿Por qué la pendiente de A es f(x)?", 38, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        h_t = ValueTracker(0.5)  # ancho de la franja
        self.mostrar_franja(h_t)
        pasos, nota = self.mostrar_razonamiento()
        self.mostrar_convergencia(h_t, pasos, nota)
        self.limpiar()

    def mostrar_franja(self, h_t):
        ax = Axes(
            x_range=[-2.2, -0.6, 0.2],
            y_range=[-1, 5.5, 1],
            x_length=6.2,
            y_length=5,
            tips=False,
            axis_config={"font_size": 22},
            x_axis_config={"numbers_to_include": [-2, -1]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4, 5]},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.4)
        graf = ax.plot(f, x_range=[-2.05, -0.9], color=COLOR_F, stroke_width=4)
        self.play(Create(ax), Create(graf))

        franja = always_redraw(
            lambda: ax.get_area(graf, x_range=[X0, X0 + h_t.get_value()], color=COLOR_POS, opacity=0.55)
        )
        rectangulo = always_redraw(
            lambda: Polygon(
                ax.c2p(X0, 0), ax.c2p(X0 + h_t.get_value(), 0),
                ax.c2p(X0 + h_t.get_value(), f(X0)), ax.c2p(X0, f(X0)),
                color=COLOR_X, stroke_width=3,
            )
        )
        marca_x = MathTex("x", color=COLOR_X, font_size=34).next_to(ax.c2p(X0, 0), DOWN, buff=0.45).shift(LEFT * 0.15)
        marca_xh = always_redraw(
            lambda: MathTex("x+h", color=COLOR_X, font_size=30).next_to(
                ax.c2p(X0 + h_t.get_value(), 0), DOWN, buff=0.45).shift(RIGHT * 0.4)
        )
        alto = always_redraw(
            lambda: MathTex("f(x)", color=COLOR_X, font_size=30).next_to(ax.c2p(X0, f(X0) / 2), LEFT, buff=0.15)
        )

        self.play(FadeIn(franja), Create(rectangulo), FadeIn(marca_x), FadeIn(marca_xh), FadeIn(alto))
        self.wait(3)

    def mostrar_razonamiento(self):
        pasos = VGroup(
            MathTex(r"A(x+h)-A(x)=\int_{x}^{x+h} f(t)\,dt", font_size=34),
            MathTex(r"\approx f(x)\cdot h", font_size=34),
            MathTex(r"\frac{A(x+h)-A(x)}{h}\approx f(x)", font_size=34),
            MathTex(r"A'(x)=\lim_{h\to 0}\frac{A(x+h)-A(x)}{h}=f(x)", font_size=34, color=COLOR_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        pasos.to_edge(RIGHT, buff=0.4).shift(UP * 0.9)

        nota = nota_de(0).next_to(pasos, DOWN, buff=0.6).align_to(pasos, LEFT)
        self.play(Write(pasos[0]), FadeIn(nota))
        self.wait(6)
        for i in range(1, 4):
            nueva = nota_de(i).move_to(nota, aligned_edge=LEFT)
            self.play(Write(pasos[i]), Transform(nota, nueva))
            self.wait(5)
        return pasos, nota

    def mostrar_convergencia(self, h_t, pasos, nota):
        """Lectura numérica del cociente incremental que converge a f(x)."""
        lbl_h = MathTex("h =", font_size=34, color=COLOR_X)
        val_h = DecimalNumber(0.5, num_decimal_places=3, font_size=34, color=COLOR_X)
        lbl_c = MathTex(r"\frac{A(x+h)-A(x)}{h} =", font_size=30)
        val_c = DecimalNumber(0, num_decimal_places=3, font_size=34, color=COLOR_POS)
        lbl_fx = MathTex(f"f({X0}) = {f(X0):.3f}", font_size=34, color=COLOR_F)
        lectura = VGroup(
            VGroup(lbl_h, val_h).arrange(RIGHT),
            VGroup(lbl_c, val_c).arrange(RIGHT),
            lbl_fx,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(pasos, DOWN, buff=0.5).align_to(pasos, LEFT)

        val_h.add_updater(lambda m: m.set_value(h_t.get_value()))
        val_c.add_updater(
            lambda m: m.set_value((A(X0 + h_t.get_value()) - A(X0)) / h_t.get_value())
        )
        self.play(FadeOut(nota), FadeIn(lectura))
        self.wait(3)
        self.play(h_t.animate.set_value(0.02), run_time=8, rate_func=smooth)
        self.play(Indicate(val_c), Indicate(lbl_fx))
        self.wait(6)
