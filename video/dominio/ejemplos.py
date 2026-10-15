"""Los ejemplos matemáticos del video.

Ejemplo principal:
    f(t) = t² − 2t − 3 = (t − 3)(t + 1),   a = −2,   x ∈ [−2, 4]
    A(x) = x³/3 − x² − 3x + 2/3,   A'(x) = f(x)

Contraejemplo:
    g(t) = t²,   G(x) = ∫_0^x t² dt = x³/3   (g = 0 en x = 0 sin extremo)
"""

from .signo import Extremo, Signo, Tramo

A_INICIO = -2.0  # punto fijo a desde donde se acumula
X_FIN = 4.0      # último valor de x que se muestra


def f(t):
    """Función que se integra: f(t) = t² − 2t − 3 = (t − 3)(t + 1)."""
    return t**2 - 2 * t - 3


def A(x):
    """Función de acumulación A(x) = ∫_{-2}^{x} f(t) dt, calculada a mano."""
    return x**3 / 3 - x**2 - 3 * x + 2 / 3


# Signo de f en [A_INICIO, X_FIN]; ceros en x = −1 y x = 3.
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
    """Integrando del contraejemplo: g(t) = t²."""
    return t**2


def G(x):
    """Acumulación del contraejemplo: ∫_0^x t² dt."""
    return x**3 / 3
