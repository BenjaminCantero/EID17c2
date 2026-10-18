"""Colores y tipografía compartidos por todas las escenas."""

from manim import BLUE_C, GREEN_C, ORANGE, PURPLE_B, RED_C, YELLOW, Text

from ..dominio.signo import Signo, clasificar_signo

COLOR_F = BLUE_C
COLOR_A = ORANGE
COLOR_POS = GREEN_C     # f > 0
COLOR_NEG = RED_C       # f < 0
COLOR_CERO = YELLOW     # f = 0
COLOR_X = PURPLE_B

COLOR_POR_SIGNO = {
    Signo.POSITIVO: COLOR_POS,
    Signo.NEGATIVO: COLOR_NEG,
    Signo.CERO: COLOR_CERO,
}


def color_por_signo(valor):
    return COLOR_POR_SIGNO[clasificar_signo(valor)]


def texto(s, size=30, **kw):
    return Text(s, font_size=size, **kw)
