"""Datos editables del grupo. Es el único archivo que hay que tocar para
poner los nombres reales, cambiar quién narra o actualizar las fuentes."""

NOMBRES = [
    "Benjamin Cantero",
    "Ricargo Garces",
    "Juan Pablo valdevenito",
]
CURSO = "MAT1188 – Cálculo Intermedio"
GRUPO = "Grupo 17"

# Quién narra cada escena (índice dentro de NOMBRES).
# Si el grupo tiene 3 integrantes, cambien los índices para que todos hablen.
HABLA = {
    "portada": 1,
    "definicion": 1,
    "dos_graficas": 1,
    "franja": 2,
    "calculo": 2,
    "contraejemplo": 3,
    "cierre": 3,
}

FUENTES = [
    "Apunte del curso MAT1188 – Cálculo Intermedio (sección: Teorema Fundamental del Cálculo).",
    "Stewart, J. (2018). Cálculo de una variable: trascendentes tempranas (8.ª ed.). Cengage. Sección 5.3.",
    "Thomas, G. B. (2015). Cálculo. Una variable (13.ª ed.). Pearson. Sección 5.4.",
    "Manim Community v0.22.0 — docs.manim.community (licencia MIT).",
]
DECLARACION_IA = [
    "Uso de IA: se usó Claude (Anthropic) como apoyo para el borrador del código",
    "El grupo revisó y verificó todos los cálculos a mano y cada escena.",
]
