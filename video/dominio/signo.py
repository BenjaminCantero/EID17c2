"""Clasificación del signo de f(x) y lo que implica para A(x)."""

from dataclasses import dataclass
from enum import Enum

TOL_CERO = 0.15  # |f(x)| menor que esto se considera "casi cero"


class Signo(Enum):
    POSITIVO = "positivo"  # f > 0  →  A crece
    NEGATIVO = "negativo"  # f < 0  →  A decrece
    CERO = "cero"          # f = 0  →  tangente horizontal


def clasificar_signo(valor, tol=TOL_CERO):
    if valor > tol:
        return Signo.POSITIVO
    if valor < -tol:
        return Signo.NEGATIVO
    return Signo.CERO


@dataclass(frozen=True)
class Tramo:
    """Intervalo [inicio, fin] donde f mantiene el signo."""
    inicio: float
    fin: float
    signo: Signo


@dataclass(frozen=True)
class Extremo:
    """Punto donde f se anula y cambia de signo: A tiene un extremo local."""
    x: float
    nombre: str


def pendiente_numerica(F, x, h=1e-4):
    """Pendiente de F en x con un cociente incremental centrado.
    Se calcula SOLO a partir de A, sin usar f, para comprobar en pantalla
    que la pendiente de A coincide con f(x)."""
    return (F(x + h) - F(x - h)) / (2 * h)
