"""Datos editables del grupo. Es el único archivo que hay que tocar para
poner los nombres reales, cambiar quién narra o actualizar las fuentes."""

NOMBRES = [
    "Benjamin Cantero",
    "Ricardo Garces",
    "Juan Pablo Valdevenito",
]
CURSO = "MAT1188 – Cálculo Intermedio"
GRUPO = "Grupo 17"

# Quién narra cada escena (índice dentro de NOMBRES, empieza en 0).
# Todos deben aparecer al menos una vez (rúbrica V6b); lo comprueba
# tests/test_dominio.py. Reparto pensado para ~2 min de voz por persona.
HABLA = {
    "portada": 0,        # ~25 s
    "definicion": 0,     # ~55 s
    "dos_graficas": 1,   # ~95 s
    "franja": 2,         # ~60 s
    "calculo": 2,        # ~60 s
    "contraejemplo": 1,  # ~35 s
    "cierre": 0,         # ~55 s
}

FUENTES = [
    "Apunte «Introducción a la integral», MAT1188 – Cálculo Intermedio (Teorema Fundamental del Cálculo).",
    "Stewart, J. (2018). Cálculo de una variable: trascendentes tempranas (8.ª ed.). Cengage. Sección 5.3.",
    "Thomas, G. B. (2015). Cálculo. Una variable (13.ª ed.). Pearson. Sección 5.4.",
    "Manim Community v0.22.0 — docs.manim.community (licencia MIT).",
]
DECLARACION_IA = [
    "Uso de IA: se usó Claude (Anthropic) como apoyo para el borrador y la organización del código.",
    "El grupo revisó y verificó a mano todos los cálculos, y revisó cada escena del video.",
]
