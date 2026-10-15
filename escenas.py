"""
MAT1188 Cálculo Intermedio — Proyecto Manim (EID)
Grupo 17: «La pendiente de la acumulación»

Pregunta central:
    ¿Cómo se relaciona el valor de f(x) con la pendiente de la función
    de acumulación A(x) = ∫_a^x f(t) dt ?

Punto de entrada para manim. El código vive en el paquete `video/`:
    video/datos_grupo.py          nombres, narradores, fuentes (EDITAR AQUÍ)
    video/dominio/                matemática pura (f, A, signos), sin manim
    video/presentacion/estilo.py  colores y tipografía
    video/presentacion/escenas/   una escena por archivo

Manim solo detecta escenas definidas en este archivo, por eso cada una se
registra abajo como subclase de una línea.

Renderizar todo (ver render.sh):
    manim -qh escenas.py Escena1_Portada Escena2_Definicion ...
Vista rápida de una escena en baja calidad:
    manim -pql escenas.py Escena3_DosGraficas
Tests del dominio (no requieren manim):
    python -m unittest

Versión probada: Manim Community v0.22.0
"""

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
