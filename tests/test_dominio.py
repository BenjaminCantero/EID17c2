"""Tests de la capa de dominio. Corren sin manim: `python -m unittest`."""

import unittest

from video.datos_grupo import HABLA, NOMBRES
from video.dominio.ejemplos import A, A_INICIO, EXTREMOS, G, TRAMOS, X_FIN, f, g
from video.dominio.signo import Signo, clasificar_signo, pendiente_numerica


def rango(inicio, fin, pasos=200):
    return [inicio + (fin - inicio) * i / pasos for i in range(pasos + 1)]


class TestEjemploPrincipal(unittest.TestCase):
    def test_A_parte_en_cero(self):
        self.assertAlmostEqual(A(A_INICIO), 0)

    def test_pendiente_de_A_es_f(self):
        for x in rango(A_INICIO, X_FIN):
            self.assertAlmostEqual(pendiente_numerica(A, x), f(x), places=6)

    def test_valores_en_extremos(self):
        self.assertAlmostEqual(A(-1), 7 / 3)
        self.assertAlmostEqual(A(3), -25 / 3)
        for extremo in EXTREMOS:
            self.assertAlmostEqual(f(extremo.x), 0)

    def test_tramos_cubren_el_intervalo(self):
        self.assertEqual(TRAMOS[0].inicio, A_INICIO)
        self.assertEqual(TRAMOS[-1].fin, X_FIN)
        for anterior, siguiente in zip(TRAMOS, TRAMOS[1:]):
            self.assertEqual(anterior.fin, siguiente.inicio)

    def test_signo_de_f_en_cada_tramo(self):
        for tramo in TRAMOS:
            medio = (tramo.inicio + tramo.fin) / 2
            self.assertEqual(clasificar_signo(f(medio)), tramo.signo)


class TestContraejemplo(unittest.TestCase):
    def test_pendiente_de_G_es_g(self):
        for x in rango(-1.5, 1.5):
            self.assertAlmostEqual(pendiente_numerica(G, x), g(x), places=6)


class TestDatosGrupo(unittest.TestCase):
    def test_indices_de_narradores_validos(self):
        for escena, indice in HABLA.items():
            self.assertIn(indice, range(len(NOMBRES)), f"HABLA['{escena}'] fuera de rango")

    def test_todos_narran(self):
        self.assertEqual(set(HABLA.values()), set(range(len(NOMBRES))))


class TestClasificarSigno(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(clasificar_signo(1), Signo.POSITIVO)
        self.assertEqual(clasificar_signo(-1), Signo.NEGATIVO)
        self.assertEqual(clasificar_signo(0.1), Signo.CERO)
        self.assertEqual(clasificar_signo(-0.15), Signo.CERO)


if __name__ == "__main__":
    unittest.main()
