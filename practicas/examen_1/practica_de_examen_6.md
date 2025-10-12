# Práctica de Examen: Simulación del Juego de la Vida de Conway

-----

## Contexto del Problema

El **Juego de la Vida**, concebido por el matemático John Horton Conway en 1970, no es un juego en el sentido convencional. Es un **autómata celular**, un "juego de cero jugadores" que evoluciona por sí solo a partir de un estado inicial. A pesar de sus reglas simples, da lugar a patrones emergentes increíblemente complejos y es un problema clásico en la computación y la simulación.

Usted ha sido encargado de crear una simulación basada en texto en Python que modele el comportamiento de este autómata celular en una cuadrícula bidimensional.

Puede ver los siguientes videos para entender el juego: [Video 1](https://www.youtube.com/watch?v=RPnLlSLAJMM) y [Video 2](https://www.youtube.com/watch?v=omMcrvVGTMs)

-----

## Objetivo General del Ejercicio

Desarrollar un programa en Python que simule el Juego de la Vida. El programa debe inicializar un tablero con un patrón de celdas vivas, calcular su evolución a lo largo de un número determinado de generaciones, e imprimir el estado del tablero en cada paso en la consola.

-----

## 1\. Modelo de Datos y Reglas

### Modelo del Tablero

El universo del juego es una **cuadrícula bidimensional finita**.

- El tablero se representará como una **lista de listas**.
- Cada celda en el tablero puede tener uno de dos estados:
  - **Viva**: Representada por el número entero `1`.
  - **Muerta**: Representada por el número entero `0`.
- El estado inicial del tablero se definirá mediante una **lista de tuplas**, donde cada tupla `(fila, columna)` indica la posición de una celda viva.

### Reglas de Evolución

Para cada generación, el estado de una celda en la siguiente generación se determina aplicando las siguientes reglas a su estado actual:

1. **Subpoblación**: Una celda **viva** con **menos de dos** vecinos vivos muere.
2. **Supervivencia**: Una celda **viva** con **dos o tres** vecinos vivos sobrevive a la siguiente generación.
3. **Sobrepoblación**: Una celda **viva** con **más de tres** vecinos vivos muere.
4. **Reproducción**: Una celda **muerta** con **exactamente tres** vecinos vivos se convierte en una celda viva.

Un "vecino" es cualquiera de las ocho celdas que rodean a la celda actual (horizontal, vertical y diagonalmente).

-----

## 2\. Requisitos Funcionales y Modularización

Su programa debe estar descompuesto en las siguientes funciones para asegurar un diseño limpio y comprobable.

### Función 1: `crear_tablero(dimensiones, celdas_vivas)`

**Parámetros:**

- `dimensiones`: Una tupla `(filas, columnas)` que define el tamaño del tablero.
- `celdas_vivas`: Una lista de tuplas, donde cada tupla `(f, c)` es la coordenada de una celda que debe iniciar como viva (`1`).

**Lógica:**

- Crear una lista de listas (un tablero) con las dimensiones dadas, inicializando todas las celdas a `0` (muertas).
- Iterar sobre la lista `celdas_vivas` y cambiar el estado de las celdas correspondientes en el tablero a `1` (vivas).
- **Manejo de errores**: Si una coordenada en `celdas_vivas` está fuera de los límites del tablero, debe ignorarla y continuar.

**Retorno:**

- El tablero (lista de listas) completamente inicializado.

-----

### Función 2: `imprimir_tablero(tablero)`

**Parámetros:**

- `tablero`: La lista de listas que representa el estado actual del juego.

**Lógica:**

- Iterar sobre cada fila y cada celda del tablero.
- Imprimir un carácter para representar cada estado. Por ejemplo:
  - `o` para una celda viva.
  - `·` para una celda muerta.
- El resultado debe ser una representación visual clara del tablero en la consola.

**Retorno:**

- Esta función no retorna ningún valor (`None`).

-----

### Función 3: `contar_vecinos(tablero, fila, col)`

**Parámetros:**

- `tablero`: El estado actual del juego.
- `fila`, `col`: Las coordenadas de la celda cuyo vecindario se va a analizar.

**Lógica:**

- Obtener las dimensiones del tablero.
- Iterar sobre las 8 posiciones vecinas a la celda `(fila, col)`.
- Para cada vecino, debe **verificar que sus coordenadas estén dentro de los límites del tablero** antes de intentar acceder a su estado.
- Sumar los estados de los vecinos válidos (el resultado será el número de vecinos vivos).

**Retorno:**

- Un número entero que representa la cantidad de vecinos vivos.

-----

### Función 4: `calcular_siguiente_generacion(tablero_actual)`

**Parámetros:**

- `tablero_actual`: La lista de listas que representa la generación actual.

**Lógica:**

- **Punto crítico**: Debe crear un **nuevo tablero** completamente vacío (con ceros) del mismo tamaño que `tablero_actual`. **No modifique el `tablero_actual` mientras lo recorre**, ya que esto corromperá el cálculo de los vecinos para las celdas posteriores.
- Iterar sobre cada celda `(f, c)` del `tablero_actual`.
- Para cada celda, usar su función `contar_vecinos` para obtener el número de vecinos vivos.
- Aplicar las cuatro reglas del Juego de la Vida para determinar si la celda `(f, c)` estará viva o muerta en la siguiente generación.
- Asignar el nuevo estado (`0` o `1`) a la celda `(f, c)` en el **nuevo tablero**.

**Retorno:**

- El nuevo tablero (lista de listas) que representa la siguiente generación.

-----

## 3\. Flujo Principal del Programa

En la sección principal de su script (fuera de las funciones), usted debe:

1. Definir las constantes de la simulación: `DIMENSIONES` (tupla), `GENERACIONES` (entero) y `PATRON_INICIAL` (lista de tuplas).
2. Llamar a `crear_tablero` para generar el estado inicial del juego.
3. Iniciar un bucle `for` que se ejecute desde la generación 0 hasta `GENERACIONES - 1`.
4. Dentro del bucle:
    a. Imprimir un encabezado que indique el número de la generación actual.
    b. Llamar a `imprimir_tablero` para mostrar el estado actual del tablero.
    c. Llamar a `calcular_siguiente_generacion` para computar el tablero de la siguiente generación.
    d. Actualizar la variable que contiene el tablero con el nuevo tablero calculado.
    e. **(Opcional)**: Para una mejor visualización, puede importar el módulo `time` y usar `time.sleep(0.5)` para pausar la ejecución medio segundo entre generaciones.

-----

## 4\. Datos de Entrada de Ejemplo

Use estos datos para probar su programa con un patrón clásico llamado "Glider" (Planeador).

```python
# --- Configuración de la Simulación ---
DIMENSIONES = (10, 20)  # 10 filas, 20 columnas
GENERACIONES = 15

# Patrón inicial "Glider" que se mueve diagonalmente
PATRON_INICIAL = [
    (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)
]
```

-----

## 5\. Salida Esperada en Consola

El programa deberá imprimir el tablero en cada una de las 15 generaciones. La salida para las dos primeras generaciones debería verse así (usando los caracteres sugeridos):

```txt
--- Generación 0 ---
· o · · · · · · · · · · · · · · · · · ·
· · o · · · · · · · · · · · · · · · · ·
o o o · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·

--- Generación 1 ---
· · · · · · · · · · · · · · · · · · · ·
o · o · · · · · · · · · · · · · · · · ·
· o o · · · · · · · · · · · · · · · · ·
· o · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
```

... y así sucesivamente para las siguientes generaciones. Se debe observar cómo el patrón "Glider" se desplaza por el tablero.
