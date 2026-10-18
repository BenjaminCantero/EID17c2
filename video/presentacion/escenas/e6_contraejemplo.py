"""Escena 6: Contraejemplo: f = 0 no siempre es extremo."""

from manim import *

from ...dominio.ejemplos import G, g
from ..componentes import EscenaNarrada
from ..estilo import COLOR_A, COLOR_CERO, COLOR_F, COLOR_X, color_por_signo, texto


class Contraejemplo(EscenaNarrada):
    hablante = "contraejemplo"

    def construct(self):
        self.mostrar_hablante()
        titulo = texto("Ojo: f(x) = 0 no siempre da un extremo", 36, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        ax1, ax2 = self.mostrar_graficas()
        self.recorrer(ax1, ax2)
        self.mostrar_conclusion()
        self.limpiar()

    def mostrar_graficas(self):
        cfg = dict(x_range=[-1.6, 1.6, 0.5], x_length=5.2, y_length=3.6, tips=False,
                   axis_config={"font_size": 20})
        ax1 = Axes(y_range=[-0.5, 2.6, 1], **cfg)
        ax2 = Axes(y_range=[-1.4, 1.4, 1], **cfg)
        VGroup(ax1, ax2).arrange(RIGHT, buff=1.0).shift(DOWN * 0.3)
        etiquetas = VGroup(
            MathTex("f(t)", font_size=22, color=COLOR_F).next_to(
                ax1.y_axis, LEFT, buff=0.08
            ),
            MathTex("t", font_size=22, color=COLOR_X).next_to(
                ax1.x_axis, RIGHT, buff=0.08
            ),
            MathTex("A(x)", font_size=22, color=COLOR_A).next_to(
                ax2.y_axis, LEFT, buff=0.08
            ),
            MathTex("x", font_size=22, color=COLOR_X).next_to(
                ax2.x_axis, RIGHT, buff=0.08
            ),
        )
        n1 = MathTex(r"f(t)=t^2", color=COLOR_F, font_size=34).next_to(ax1, UP, buff=0.1)
        n2 = MathTex(r"A(x)=\int_0^x t^2\,dt=\frac{x^3}{3}", color=COLOR_A, font_size=34).next_to(ax2, UP, buff=0.1)
        p1 = ax1.plot(g, x_range=[-1.5, 1.5], color=COLOR_F, stroke_width=4)
        p2 = ax2.plot(G, x_range=[-1.5, 1.5], color=COLOR_A, stroke_width=4)
        self.play(Create(ax1), Create(ax2), FadeIn(etiquetas), Write(n1), Write(n2))
        self.play(Create(p1), Create(p2), run_time=2)
        return ax1, ax2

    def recorrer(self, ax1, ax2):
        x_t = ValueTracker(-1.3)
        dot1 = always_redraw(lambda: Dot(ax1.c2p(x_t.get_value(), g(x_t.get_value())),
                                         color=color_por_signo(g(x_t.get_value()) * 3)))
        dot2 = always_redraw(lambda: Dot(ax2.c2p(x_t.get_value(), G(x_t.get_value())), color=WHITE))

        def tang():
            xv, m, d = x_t.get_value(), g(x_t.get_value()), 0.5
            return Line(ax2.c2p(xv - d, G(xv) - m * d), ax2.c2p(xv + d, G(xv) + m * d),
                        color=color_por_signo(m * 3), stroke_width=5)

        tg = always_redraw(tang)
        self.add(dot1, dot2, tg)
        self.play(x_t.animate.set_value(0), run_time=4, rate_func=linear)
        self.wait(3)
        self.play(x_t.animate.set_value(1.3), run_time=4, rate_func=linear)

    def mostrar_conclusion(self):
        conclusion = VGroup(
            texto("En x = 0 la tangente es horizontal, pero A sigue creciendo:", 26),
            texto("f no cambia de signo, así que no hay máximo ni mínimo.", 26, color=COLOR_CERO),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(conclusion))
        self.wait(5)
