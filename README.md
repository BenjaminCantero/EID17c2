# La pendiente de la acumulación

Proyecto EID de **MAT1188 – Cálculo Intermedio**, Grupo 17.
Video hecho con [Manim Community v0.22.0](https://docs.manim.community).

**Tema:** función de acumulación y Teorema Fundamental del Cálculo (parte 1).

| Integrante | Cuenta GitHub | Rol principal |
|---|---|---|
| Benjamin Cantero | [@BenjaminCantero](https://github.com/BenjaminCantero) | _completar_ |
| Ricardo Garces | [@RicardoAndrees](https://github.com/RicardoAndrees)
| Juan Pablo Valdebenito | [@Juan-Valdebenito](https://github.com/Juan-Valdebenito) | _completar_ |

Los roles a repartir son: matemática y explicación; visualización y código; revisión e integración del video.

## Pregunta central

¿Cómo se relaciona el valor de f(x) con la pendiente de la función de acumulación

$$A(x) = \int_a^x f(t)\,dt\ ?$$

**Respuesta:** por el Teorema Fundamental del Cálculo (parte 1), si f es continua, entonces A'(x) = f(x).
El valor de f en x **es** la pendiente de A en x:

- si f(x) > 0, A crece;
- si f(x) < 0, A decrece;
- si f(x) = 0, la tangente es horizontal, y hay un extremo solo si f cambia de signo.

## Ejemplo del video

$$f(t) = t^2 - 2t - 3 = (t-3)(t+1), \qquad a = -2, \qquad x \in [-2, 4]$$

$$A(x) = \frac{x^3}{3} - x^2 - 3x + \frac{2}{3}, \qquad A'(x) = f(x)$$

| x | (−2, −1) | −1 | (−1, 3) | 3 | (3, 4) |
|---|---|---|---|---|---|
| f(x) = A'(x) | + | 0 | − | 0 | + |
| A(x) | crece | máx. local, A(−1) = 7/3 | decrece | mín. local, A(3) = −25/3 | crece |

Contraejemplo: con f(t) = t² y A(x) = x³/3, se cumple f(0) = 0, pero A no tiene extremo en 0 porque f no cambia de signo.

## Escenas

| Escena | Contenido | Narra | Duración |
|---|---|---|---|
| 1. Portada | Título, integrantes y pregunta central | Benjamin | 30 s |
| 2. Definición | Definición de A, significado de cada símbolo, hipótesis y enunciado del TFC | Benjamin | 55 s |
| 3. Dos gráficas | f y A sincronizadas: área con signo, tangente de pendiente f(x) y valores numéricos | Ricardo | 87 s |
| 4. Franja | Por qué A'(x) = f(x): la franja de ancho h y el cociente incremental que converge | Juan Pablo | 55 s |
| 5. Cálculo | Cálculo exacto de A, su derivada, ceros de f y tabla de signos | Juan Pablo | 52 s |
| 6. Contraejemplo | f = 0 no siempre da un extremo | Ricardo | 24 s |
| 7. Cierre | Respuesta a la pregunta central, fuentes y uso de IA | Benjamin | 40 s |

Duración total: **5 min 42 s**.

## Cómo generar el video

### Versiones y dependencias

| Herramienta | Versión usada |
|---|---|
| Python | 3.14.7 |
| Manim Community | 0.22.0 (`requirements.txt`) |
| LaTeX | TeX Live (para `MathTex` y `MathTable`) |
| ffmpeg | 9.0 (Manim lo usa para generar los videos; `render.sh`, para unir las escenas) |

En Linux también se necesitan las bibliotecas de sistema `cairo` y `pango`. Ver la [guía de instalación de Manim](https://docs.manim.community/en/stable/installation.html).

### Pasos

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
./render.sh          # 1080p60 → MAT1188_EID_G17_2026.mp4
./render.sh l        # 480p15, para revisar rápido
```

Para ver una sola escena:

```bash
.venv/bin/manim -pql escenas.py Escena3_DosGraficas
```

Para comprobar los cálculos y que todos los integrantes narren alguna escena (no requiere manim):

```bash
python -m unittest
```

## Estructura del código

```
escenas.py                     punto de entrada de manim (registra las 7 escenas)
render.sh                      renderiza todo y une las escenas en MAT1188_EID_G17_2026.mp4
video/
  datos_grupo.py               nombres, quién narra cada escena, fuentes y declaración de IA
  dominio/                     matemática pura, sin manim
    ejemplos.py                f, A, tramos de signo, extremos y el contraejemplo
    signo.py                   clasificación del signo y pendiente numérica
  presentacion/
    estilo.py                  colores (verde: f > 0, rojo: f < 0, amarillo: f = 0)
    componentes.py             rótulo "Explica: ..." y clase base de las escenas
    escenas/e1_portada.py ...  una escena por archivo
tests/test_dominio.py          comprueba A' = f, los valores de A y el reparto de narradores
```

### Parámetros clave

| Parámetro | Archivo | Qué controla en el video |
|---|---|---|
| `x_t` | `e3_dos_graficas.py` | `ValueTracker` con la posición de x; al animarlo se mueven a la vez el área, la curva de A, la tangente, los puntos y el panel numérico |
| `MEDIO_ANCHO` | `e3_dos_graficas.py` | Mitad del largo del segmento tangente a A |
| `pendiente_numerica` | `dominio/signo.py` | Calcula la pendiente de A solo con valores de A, (A(x+h) − A(x−h)) / 2h; el panel muestra que coincide con f(x) |
| `TOL_CERO` | `dominio/signo.py` | Bajo este valor, \|f(x)\| se considera cero: color amarillo y "tangente horizontal" |
| `h_t` | `e4_franja.py` | Ancho h de la franja; al achicarlo de 0,5 a 0,02, el cociente (A(x+h) − A(x)) / h converge a f(−1,6) = 2,76 |
| `TRAMOS` | `dominio/ejemplos.py` | Intervalos donde f es positiva o negativa; definen los colores del área y el resumen "crece / decrece" |

## Fuentes

- Universidad Católica de Temuco (2026). *Introducción a la integral* [Apunte del curso MAT1188 – Cálculo Intermedio]. Disponible en el Blackboard del curso. Usado para la definición de A(x) y el TFC.
- Stewart, J. (2018). *Cálculo de una variable: trascendentes tempranas* (8.ª ed.). Cengage Learning. Sección 5.3, «El Teorema Fundamental del Cálculo». <https://www.cengage.com>
- Thomas, G. B., Weir, M. D. y Hass, J. (2015). *Cálculo. Una variable* (13.ª ed.). Pearson Educación. Sección 5.4. <https://www.pearson.com>
- The Manim Community Developers (consultado en 2026). *Manim Community v0.22.0, documentación oficial*. Licencia MIT. <https://docs.manim.community>

No se usaron imágenes, música ni código de terceros aparte de Manim. Todas las animaciones son propias.

## Uso de IA

- **Herramienta:** Claude (Anthropic), mediante Claude Code.
- **Finalidad:** apoyo en la programación de las escenas de Manim y en la organización del repositorio.
- **Partes apoyadas:**
  - borrador del código de las escenas;
  - separación del código en las carpetas `dominio/` y `presentacion/`;
  - script `render.sh`;
  - tests;
  - borrador de este README.
- **Partes no apoyadas:** la elección del tema, del ejemplo y del contraejemplo, y la narración del video.
- **Verificación:**
  - Calculamos a mano A(x), A'(x), los ceros de f, A(−1) = 7/3, A(3) = −25/3 y f(−1,6) = 2,76.
  - Comparamos esos valores con lo que muestra el video.
  - `python -m unittest` comprueba numéricamente que A' = f.
  - Revisamos cada escena renderizada.

La IA no reemplazó las fuentes: la teoría proviene del apunte y de los libros citados.
