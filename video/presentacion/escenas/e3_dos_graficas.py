"""ESCENA 3 — Las dos gráficas, sincronizadas                (~95 s)

Esta es la escena central del proyecto."""

from manim import *

from ...dominio.ejemplos import A, A_INICIO, EXTREMOS, TRAMOS, X_FIN, f

from ...dominio.signo import Signo, clasificar_signo, pendiente_numerica

from ..componentes import EscenaNarrada

from ..estilo import (

    COLOR_A, COLOR_CERO, COLOR_F, COLOR_NEG, COLOR_POR_SIGNO, COLOR_X,

    color_por_signo, texto,

)

Y_MIN_A, Y_MAX_A = -9.5, 3.5  # rango vertical de los ejes de A

Y_MAX_F = 6                   # tope vertical de los ejes de f

MEDIO_ANCHO = 0.7             # mitad del largo de la tangente, en unidades de x

ESTADO_POR_SIGNO = {

    Signo.POSITIVO: (r"f(x) > 0", "A crece"),

    Signo.NEGATIVO: (r"f(x) < 0", "A decrece"),

    Signo.CERO: (r"f(x) = 0", "tangente horizontal"),

}

PALABRA_RESUMEN = {Signo.POSITIVO: "crece", Signo.NEGATIVO: "decrece"}

class DosGraficas(EscenaNarrada):

    hablante = "dos_graficas"

    def construct(self):

        self.mostrar_hablante()

        ax_f, ax_A = self.crear_ejes()

        graf_f, guia_A = self.mostrar_graficas(ax_f, ax_A)

        # Pausa adicional
        self.wait(2)

        # El parámetro que mueve todo: x

        x_t = ValueTracker(A_INICIO + 0.001)

        x = x_t.get_value

        dinamicos = self.crear_dinamicos(ax_f, ax_A, graf_f, x)

        tangente = always_redraw(lambda: self.dibujar_tangente(ax_A, x()))

        filas = self.crear_panel(x)

        estado = always_redraw(lambda: self.dibujar_estado(filas, x()))

        self.play(FadeIn(filas), FadeIn(guia_A))

        self.add(*dinamicos)

        self.play(Create(tangente), FadeIn(estado))

        self.wait(4)

        # Pausa adicional: panel completo antes de comenzar el área verde.
        self.wait(2)

        self.recorrer(x_t, ax_f, ax_A)

        vertical = dinamicos[1]

        self.play(FadeOut(tangente), FadeOut(estado), FadeOut(vertical))

        self.mostrar_resumen(ax_A)

        self.limpiar()

    # ---------- Ejes: arriba f, abajo A, con la MISMA escala horizontal ----------

    def crear_ejes(self):

        comunes = dict(

            x_range=[-2.5, 4.5, 1],

            x_length=8.4,

            y_length=2.9,

            tips=False,

            axis_config={"font_size": 20, "stroke_width": 2},

        )

        ax_f = Axes(

            y_range=[-5, Y_MAX_F, 1],

            x_axis_config={"numbers_to_include": [-2, -1, 1, 2, 3, 4]},

            y_axis_config={"numbers_to_include": [-4, -2, 2, 4]},

            **comunes,

        )

        ax_A = Axes(

            y_range=[Y_MIN_A, Y_MAX_A, 1],

            x_axis_config={"numbers_to_include": [-2, -1, 1, 2, 3, 4]},

            y_axis_config={"numbers_to_include": [-9, -6, -3, 3]},

            **comunes,

        )

        VGroup(ax_f, ax_A).arrange(DOWN, buff=0.55).to_edge(LEFT, buff=0.5).shift(DOWN * 0.15)

        return ax_f, ax_A

    def mostrar_graficas(self, ax_f, ax_A):

        etiquetas = VGroup(

            MathTex("f(t)", font_size=22, color=COLOR_F).next_to(

                ax_f.y_axis, UP, buff=0.08

            ).shift(RIGHT * 0.55),

            MathTex("t", font_size=22, color=COLOR_X).next_to(

                ax_f.x_axis, RIGHT, buff=0.08

            ),

            MathTex("A(x)", font_size=22, color=COLOR_A).next_to(

                ax_A.y_axis, UP, buff=0.08

            ).shift(RIGHT * 0.55),

            MathTex("x", font_size=22, color=COLOR_X).next_to(

                ax_A.x_axis, RIGHT, buff=0.08

            ),

        )

        nombre_f = MathTex(r"y = f(t) = t^2-2t-3", font_size=30, color=COLOR_F)

        nombre_f.next_to(ax_f, UP, buff=0.05).align_to(ax_f, LEFT).shift(RIGHT * 0.3)

        nombre_A = MathTex(r"y = A(x) = \int_{-2}^{x} f(t)\,dt", font_size=30, color=COLOR_A)

        nombre_A.move_to(ax_A.c2p(1.2, 2.6), aligned_edge=LEFT)

        graf_f = ax_f.plot(f, x_range=[A_INICIO, X_FIN], color=COLOR_F, stroke_width=4)

        guia_A = DashedVMobject(

            ax_A.plot(A, x_range=[A_INICIO, X_FIN], color=COLOR_A, stroke_opacity=0.35),

            num_dashes=60,

        )

        self.play(Create(ax_f), Create(ax_A), FadeIn(etiquetas), run_time=1.5)

        self.play(Create(graf_f), Write(nombre_f), run_time=2)

        self.play(Write(nombre_A))

        self.wait(5)

        return graf_f, guia_A

    # ---------- Objetos que siguen a x ----------

    def crear_dinamicos(self, ax_f, ax_A, graf_f, x):

        """Devuelve [área, vertical, curva de A, punto en f, punto en A]."""

        # Área acumulada bajo f: verde donde f>0, roja donde f<0

        def dibujar_area():

            grupo = VGroup()

            for tramo in TRAMOS:

                tope = min(tramo.fin, x())

                if tope - tramo.inicio > 0.01:

                    grupo.add(ax_f.get_area(graf_f, x_range=[tramo.inicio, tope],

                                            color=COLOR_POR_SIGNO[tramo.signo], opacity=0.5))

            return grupo

        area = always_redraw(dibujar_area)

        # Curva de A que se va dibujando hasta x

        curva_A = always_redraw(

            lambda: ax_A.plot(A, x_range=[A_INICIO, max(x(), A_INICIO + 0.01)],

                              color=COLOR_A, stroke_width=5)

        )

        # Línea vertical que une el mismo x en ambas gráficas

        vertical = always_redraw(

            lambda: DashedLine(ax_A.c2p(x(), Y_MIN_A), ax_f.c2p(x(), Y_MAX_F),

                               color=COLOR_X, stroke_width=2, stroke_opacity=0.6)

        )

        punto_f = always_redraw(lambda: Dot(ax_f.c2p(x(), f(x())), color=color_por_signo(f(x())), radius=0.07))

        punto_A = always_redraw(lambda: Dot(ax_A.c2p(x(), A(x())), color=WHITE, radius=0.07))

        return [area, vertical, curva_A, punto_f, punto_A]

    @staticmethod

    def dibujar_tangente(ax_A, xv):

        """Recta tangente a A en x. Su pendiente es f(x)."""

        m = f(xv)

        p1 = ax_A.c2p(xv - MEDIO_ANCHO, A(xv) - m * MEDIO_ANCHO)

        p2 = ax_A.c2p(xv + MEDIO_ANCHO, A(xv) + m * MEDIO_ANCHO)

        return Line(p1, p2, color=color_por_signo(m), stroke_width=5)

    # ---------- Panel de lectura a la derecha ----------

    def crear_panel(self, x):

        lbl_x = MathTex("x =", font_size=36, color=COLOR_X)

        val_x = DecimalNumber(x(), num_decimal_places=2, font_size=36, color=COLOR_X)

        lbl_f = MathTex("f(x) =", font_size=36, color=COLOR_F)

        val_f = DecimalNumber(f(x()), num_decimal_places=2, font_size=36, include_sign=True)

        lbl_m = texto("pendiente de A:", 24, color=COLOR_A)

        val_m = DecimalNumber(0, num_decimal_places=2, font_size=36, include_sign=True)

        lbl_Ax = MathTex("A(x) =", font_size=36, color=COLOR_A)

        val_Ax = DecimalNumber(A(x()), num_decimal_places=2, font_size=36, include_sign=True)

        filas = VGroup(

            VGroup(lbl_x, val_x),

            VGroup(lbl_Ax, val_Ax),

            VGroup(lbl_f, val_f),

            VGroup(lbl_m, val_m),

        )

        for fila in filas:

            fila.arrange(RIGHT, buff=0.2)

        filas.arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        filas.to_edge(RIGHT, buff=0.5).shift(UP * 1.6)

        val_x.add_updater(lambda m: m.set_value(x()))

        val_Ax.add_updater(lambda m: m.set_value(A(x())))

        val_f.add_updater(lambda m: m.set_value(f(x())).set_color(color_por_signo(f(x()))))

        val_m.add_updater(

            lambda m: m.set_value(pendiente_numerica(A, x())).set_color(color_por_signo(f(x())))

        )

        return filas

    @staticmethod

    def dibujar_estado(filas, xv):

        v = f(xv)

        cond, frase = ESTADO_POR_SIGNO[clasificar_signo(v)]

        col = color_por_signo(v)

        g = VGroup(

            MathTex(cond, font_size=38, color=col),

            MathTex(r"\Downarrow", font_size=38, color=col),

            texto(frase, 26, color=col, weight=BOLD),

        ).arrange(DOWN, buff=0.15)

        caja = SurroundingRectangle(g, color=col, buff=0.2, corner_radius=0.1)

        bloque = VGroup(g, caja).next_to(filas, DOWN, buff=0.6)

        return bloque.to_edge(RIGHT, buff=0.3)

    # ---------- Animación ----------

    def recorrer(self, x_t, ax_f, ax_A):

        maximo, minimo = EXTREMOS

        # Tramo 1: f > 0, A crece

        self.play(x_t.animate.set_value(maximo.x), run_time=7, rate_func=linear)

        # Pausa en x = −1: f = 0, tangente horizontal, máximo local

        self.pausar_en_extremo(maximo, ax_f, ax_A)

        # Tramo 2: f < 0, A decrece

        self.play(x_t.animate.set_value(1), run_time=7, rate_func=linear)

        self.notar_bajada_rapida(ax_f)

        self.play(x_t.animate.set_value(minimo.x), run_time=7, rate_func=linear)

        # Pausa en x = 3: f = 0, tangente horizontal, mínimo local

        self.pausar_en_extremo(minimo, ax_f, ax_A)

        # Tramo 3: f > 0 otra vez, A vuelve a crecer

        self.play(x_t.animate.set_value(X_FIN), run_time=5, rate_func=linear)

        self.wait(4)

    def pausar_en_extremo(self, extremo, ax_f, ax_A):

        circ = Circle(radius=0.3, color=COLOR_CERO).move_to(ax_A.c2p(extremo.x, A(extremo.x)))

        circ_f = Circle(radius=0.25, color=COLOR_CERO).move_to(ax_f.c2p(extremo.x, 0))

        nota = texto(extremo.nombre, 22, color=COLOR_CERO).next_to(circ, UP, buff=0.05)

        self.play(Create(circ), Create(circ_f), FadeIn(nota))

        self.wait(7)

        self.play(FadeOut(circ), FadeOut(circ_f), FadeOut(nota))

    def notar_bajada_rapida(self, ax_f):

        """En x = 1 f alcanza su valor más negativo: A baja con la mayor rapidez."""

        nota_txt = VGroup(

            texto("f(1) = −4 es el valor más negativo:", 20, color=COLOR_NEG),

            texto("aquí A baja más rápido", 20, color=COLOR_NEG),

        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        nota_txt.to_corner(DR, buff=0.4)

        marca = Circle(radius=0.22, color=COLOR_NEG).move_to(ax_f.c2p(1, f(1)))

        nota = VGroup(nota_txt, marca)

        self.play(FadeIn(nota))

        self.wait(6)

        self.play(FadeOut(nota))

    # ---------- Resumen sobre la gráfica de A ----------

    def mostrar_resumen(self, ax_A):

        resumen = VGroup()

        for tramo in TRAMOS:

            lo, hi, col = tramo.inicio, tramo.fin, COLOR_POR_SIGNO[tramo.signo]

            banda = ax_A.get_area(

                ax_A.plot(lambda t: Y_MAX_A, x_range=[lo, hi]),

                x_range=[lo, hi],

                bounded_graph=ax_A.plot(lambda t: Y_MIN_A, x_range=[lo, hi]),

                color=col, opacity=0.12,

            )

            et = texto(PALABRA_RESUMEN[tramo.signo], 22, color=col).move_to(ax_A.c2p((lo + hi) / 2, -4.5))

            resumen.add(banda, et)

        self.play(FadeIn(resumen))

        self.wait(7)
