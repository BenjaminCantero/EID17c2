"""Punto de entrada de manim. Manim solo detecta escenas definidas en este
archivo, por eso cada una se registra abajo como subclase de una línea."""

from video.presentacion.escenas.e1_portada import Portada
from video.presentacion.escenas.e2_definicion import Definicion
from video.presentacion.escenas.e3_dos_graficas import DosGraficas
from video.presentacion.escenas.e4_franja import Franja
from video.presentacion.escenas.e5_calculo import Calculo
from video.presentacion.escenas.e6_contraejemplo import Contraejemplo
from video.presentacion.escenas.e7_cierre import Cierre


class Escena1_Portada(Portada): pass
class Escena2_Definicion(Definicion): pass
class Escena3_DosGraficas(DosGraficas): pass
class Escena4_Franja(Franja): pass
class Escena5_Calculo(Calculo): pass
class Escena6_Contraejemplo(Contraejemplo): pass
class Escena7_Cierre(Cierre): pass


ESCENAS = [
    "Escena1_Portada",
    "Escena2_Definicion",
    "Escena3_DosGraficas",
    "Escena4_Franja",
    "Escena5_Calculo",
    "Escena6_Contraejemplo",
    "Escena7_Cierre",
]
