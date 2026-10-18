"""Datos editables del grupo: nombres, narradores, audios y fuentes."""

NOMBRES = [
    "Benjamin Cantero",
    "Ricardo Garces",
    "Juan Pablo Valdebenito",
]
CURSO = "MAT1188 – Cálculo Intermedio"
GRUPO = "Grupo 17"

# Índice en NOMBRES de quién narra cada escena. Todos deben narrar (rúbrica V6b).
HABLA = {
    "portada": 0,
    "definicion": 0,
    "dos_graficas": 1,
    "franja": 2,
    "calculo": 2,
    "contraejemplo": 1,
    "cierre": 0,
}

# Archivos dentro de audios/.
AUDIOS = {
    "portada": "Benja1.mp4",
    "definicion": "Benja2.mp4",
    "dos_graficas": "Ricardo1.ogg",
    "franja": "Juan1.ogg",
    "calculo": "Juan2.ogg",
    "contraejemplo": "Ricardo2.ogg",
    "cierre": "Benja3.mp4",
}

FUENTES = [
    "Universidad Católica de Temuco (2026). Introducción a la integral. Apunte MAT1188.",
    "Stewart, J. (2018). Cálculo de una variable: trascendentes tempranas (8.ª ed.). Cengage. Sección 5.3.",
    "Thomas, G. B., Weir, M. D. y Hass, J. (2015). Cálculo. Una variable (13.ª ed.). Pearson. Secc. 5.4.",
    "Manim Community v0.22.0 — docs.manim.community (licencia MIT).",
]
DECLARACION_IA = [
    "Uso de IA: se usó Claude (Anthropic) como apoyo para el borrador y la organización del código.",
    "El grupo revisó y verificó a mano todos los cálculos, y revisó cada escena del video.",
]
