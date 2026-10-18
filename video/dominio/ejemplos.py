"""Los ejemplos matemáticos del video."""

from .signo import Extremo, Signo, Tramo

A_INICIO = -2.0  # punto fijo a
X_FIN = 4.0


def f(t):
    return t**2 - 2 * t - 3


def A(x):
    """A(x) = ∫_{-2}^{x} f(t) dt, calculada a mano."""
    return x**3 / 3 - x**2 - 3 * x + 2 / 3


TRAMOS = (
    Tramo(-2, -1, Signo.POSITIVO),
    Tramo(-1, 3, Signo.NEGATIVO),
    Tramo(3, 4, Signo.POSITIVO),
)
EXTREMOS = (
    Extremo(-1, "máximo local"),
    Extremo(3, "mínimo local"),
)


def g(t):
    """Contraejemplo: g = 0 en x = 0 pero G no tiene extremo."""
    return t**2


def G(x):
    return x**3 / 3
