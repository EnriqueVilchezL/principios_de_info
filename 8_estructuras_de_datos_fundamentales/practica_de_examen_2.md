# Práctica para Examen: ejercicios cortos de estructuras de datos fundamentales
***

## 1. Multiplicación de Matrices

Implemente una función `multiplicar_matrices(A:list[list[float]], B:list[list[float]]) -> list[list[float]]` que multiplique dos matrices. Debe generar una excepción si las matrices no pueden multiplicarse.

### Lógica
Para multiplicar dos matrices, $A$ y $B$, y obtener una matriz resultante $C$, es indispensable que el **número de columnas de la matriz $A$ sea igual al número de filas de la matriz $B$**.

Si la matriz $A$ tiene dimensiones $m \times n$ (m filas, n columnas) y la matriz $B$ tiene dimensiones $n \times p$ (n filas, p columnas), la matriz resultante $C$ tendrá dimensiones $m \times p$.

El valor de cada elemento $C_{ij}$ en la matriz resultante se calcula como el producto punto de la fila $i$ de la matriz $A$ y la columna $j$ de la matriz $B$. La fórmula matemática es:

$$C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}$$

### Ejemplos

**Ejemplo 1: Multiplicación válida**
```python
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

resultado = multiplicar_matrices(A, B)
# Salida: [[19, 22], [43, 50]]
```

**Ejemplo 2: Multiplicación no válida**
```python
A = [[1, 2, 3]]      # 1×3
B = [[4, 5]]         # 1×2

resultado = multiplicar_matrices(A, B)
# Excepción: Las matrices no pueden multiplicarse (3 ≠ 1)
```

**Ejemplo 3: Multiplicación rectangular**
```python
A = [[1, 2, 3],
     [4, 5, 6]]      # 2×3

B = [[7, 8],
     [9, 10],
     [11, 12]]       # 3×2

resultado = multiplicar_matrices(A, B)
# Salida: [[58, 64], [139, 154]]
```

***

## 2. Producto Punto de Vectores

Implemente una función `producto_punto(v: list[float], u: list[float]) -> float` que calcule el producto punto de dos vectores. Levante una excepción si hay errores.

### Lógica
El producto punto (o producto escalar) de dos vectores, $\mathbf{v}$ y $\mathbf{u}$, es una operación que resulta en un único número escalar. Para que la operación sea válida, ambos vectores deben tener la **misma longitud** (el mismo número de componentes).

El cálculo consiste en multiplicar los componentes correspondientes de cada vector y luego sumar todos esos productos. Si tenemos los vectores $\mathbf{v} = [v_1, v_2, \dots, v_n]$ y $\mathbf{u} = [u_1, u_2, \dots, u_n]$, su producto punto se define como:

$$\mathbf{v} \cdot \mathbf{u} = \sum_{i=1}^{n} v_i u_i = v_1u_1 + v_2u_2 + \dots + v_nu_n$$

### Ejemplos

**Ejemplo 1: Producto punto válido**
```python
v = [1, 2, 3]
u = [4, 5, 6]

resultado = producto_punto(v, u)
# Salida: 32.0
# Cálculo: (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32
```

**Ejemplo 2: Vectores de diferente longitud**
```python
v = [1, 2, 3]
u = [4, 5]

resultado = producto_punto(v, u)
# Excepción: Los vectores deben tener la misma longitud
```

**Ejemplo 3: Vectores con decimales**
```python
v = [1.5, 2.5, 3.5]
u = [2.0, 3.0, 4.0]

resultado = producto_punto(v, u)
# Salida: 24.5
# Cálculo: (1.5×2.0) + (2.5×3.0) + (3.5×4.0) = 3.0 + 7.5 + 14.0 = 24.5
```

***

## 3. Producto Hadamard de Matrices

Implemente una función `producto_hadamard(A: list[list[float]], B: list[list[float]]) -> list[list[float]]`.

### Lógica
El producto Hadamard, también conocido como producto de Schur o producto por elementos (*element-wise product*), es una operación entre dos matrices que tienen las **mismas dimensiones**.

El resultado es una nueva matriz de las mismas dimensiones, donde cada elemento $(C_{ij})$ es simplemente el producto de los elementos correspondientes de las matrices originales, $(A_{ij})$ y $(B_{ij})$. La fórmula es:

$$(A \circ B)_{ij} = A_{ij} \cdot B_{ij}$$

### Ejemplos

**Ejemplo 1: Producto Hadamard válido**
```python
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

resultado = producto_hadamard(A, B)
# Salida: [[5, 12], [21, 32]]
# Cálculo elemento por elemento: [[1×5, 2×6], [3×7, 4×8]]
```

**Ejemplo 2: Matrices de diferentes dimensiones**
```python
A = [[1, 2, 3]]      # 1×3
B = [[4, 5],
     [6, 7]]         # 2×2

resultado = producto_hadamard(A, B)
# Excepción: Las matrices deben tener las mismas dimensiones
```

**Ejemplo 3: Matrices 3×3**
```python
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

resultado = producto_hadamard(A, B)
# Salida: [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
```

***

## 4. Cálculo de Frecuencias

Implemente una función que, dada una lista de elementos, calcule sus frecuencias: `calcular_frecuencias(elements: list[Any]) -> dict[Any, int]`.

### Ejemplos

**Ejemplo 1: Lista de números**
```python
elementos = [1, 2, 3, 2, 1, 3, 3, 1]

resultado = calcular_frecuencias(elementos)
# Salida: {1: 3, 2: 2, 3: 3}
```

**Ejemplo 2: Lista de strings**
```python
elementos = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]

resultado = calcular_frecuencias(elementos)
# Salida: {"manzana": 3, "banana": 2, "naranja": 1}
```

**Ejemplo 3: Lista mixta**
```python
elementos = [1, "a", 1, "b", "a", 2.5, 2.5]

resultado = calcular_frecuencias(elementos)
# Salida: {1: 2, "a": 2, "b": 1, 2.5: 2}
```

**Ejemplo 4: Lista vacía**
```python
elementos = []

resultado = calcular_frecuencias(elementos)
# Salida: {}
```

***

## 5. Promedio de Lecturas de Sensor

Dada una lista de lecturas de un sensor de humedad de la forma `{"fecha": "dia/mes/año", "hora": "hh:mm", "humedad": numero.float}`, escriba una función para calcular los promedios por hora y otra por día.

### Ejemplos

**Datos de entrada:**
```python
lecturas = [
    {"fecha": "15/09/2025", "hora": "08:30", "humedad": 65.5},
    {"fecha": "15/09/2025", "hora": "08:45", "humedad": 67.2},
    {"fecha": "15/09/2025", "hora": "09:15", "humedad": 63.8},
    {"fecha": "15/09/2025", "hora": "09:30", "humedad": 64.1},
    {"fecha": "16/09/2025", "hora": "08:20", "humedad": 70.3},
    {"fecha": "16/09/2025", "hora": "09:10", "humedad": 68.7},
    {"fecha": "16/09/2025", "hora": "10:00", "humedad": 62.5}
]
```

**Función 1: `promedio_por_hora(lecturas)`**
```python
resultado = promedio_por_hora(lecturas)
# Salida: 
# {
#     "08": 67.67,  # (65.5 + 67.2 + 70.3) / 3
#     "09": 65.53,  # (63.8 + 64.1 + 68.7) / 3
#     "10": 62.5    # (62.5) / 1
# }
```

**Función 2: `promedio_por_dia(lecturas)`**
```python
resultado = promedio_por_dia(lecturas)
# Salida:
# {
#     "15/09/2025": 65.15,  # (65.5 + 67.2 + 63.8 + 64.1) / 4
#     "16/09/2025": 67.17   # (70.3 + 68.7 + 62.5) / 3
# }
```

**Caso especial: Lista vacía**
```python
lecturas_vacias = []

resultado_hora = promedio_por_hora(lecturas_vacias)
resultado_dia = promedio_por_dia(lecturas_vacias)
# Salida para ambos: {}
```