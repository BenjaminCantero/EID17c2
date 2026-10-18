"""Clasificación del signo de f(x) y lo que implica para A(x)."""

from dataclasses import dataclass
from enum import Enum

TOL_CERO = 0.15  # |f(x)| menor que esto se considera "casi cero"


class Signo(Enum):
    POSITIVO = "positivo"
    NEGATIVO = "negativo"
    CERO = "cero"


def clasificar_signo(valor, tol=TOL_CERO):
    if valor > tol:
        return Signo.POSITIVO
    if valor < -tol:
        return Signo.NEGATIVO
    return Signo.CERO


@dataclass(frozen=True)
class Tramo:
    inicio: float
    fin: float
    signo: Signo


@dataclass(frozen=True)
class Extremo:
    x: float
    nombre: str


def pendiente_numerica(F, x, h=1e-4):
    """Pendiente de F en x usando solo F (sin f), para comprobar que coincide con f(x)."""
    return (F(x + h) - F(x - h)) / (2 * h)
