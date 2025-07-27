---
marp: true
theme: uncover
backgroundImage: url("../resources/templates/2/Template_page-0018.jpg")
style: |
    header {
        position: absolute;
        top: 10px;
        left: 0;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 40px;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    header img {
        height: 150px;
        width: 180px;
    }

    .triple {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 100%;
    }
    .triple > div {
        flex: 1;
    }
    .left   { text-align: left; }
    .center { text-align: center; }
    .right  { text-align: right; }

paginate: true
---
                    
<!-- _header: ![Logo UCR](../resources/ucr.png) Principios de informática ![Logo ECCI](../resources/ecci.png) -->

# 3. Operadores y expresiones ➕➖

---

# ¡Bienvenido al mundo de las operaciones! 🧠

---

**Hoy aprenderemos a:**
*   Realizar **cálculos** con operadores aritméticos. 🔢
*   Hacer **comparaciones** lógicas. ✅❌
*   Combinar **condiciones**. 🚦
*   Guardar y actualizar **valores**. 💾
*   Entender el **orden** de las operaciones. 🚀

---

# ¿Qué son los Operadores? 🛠️

---

Los **operadores** son símbolos especiales que realizan operaciones sobre uno o más valores (llamados operandos).

---

**Operando + Operador + Operando = Resultado**
`5` `+` `3` `=` `8`

---

# Tipos de Operadores en Python 🐍

---

## ➕➖ Operadores Aritméticos

---

Nos permiten realizar **cálculos matemáticos** básicos.
Son como las funciones de una calculadora. 🧮

---

**Tabla de Operadores Aritméticos:**

| Operador | Nombre         | Ejemplo       | Resultado |
|----------|----------------|---------------|-----------|
| `+`      | Suma           | `5 + 3`       | `8`       |
| `-`      | Resta          | `10 - 4`      | `6`       |
| `*`      | Multiplicación | `2 * 6`       | `12`      |

---

**Más Operadores Aritméticos:**

| Operador | Nombre           | Ejemplo         | Resultado |
|----------|------------------|-----------------|-----------|
| `/`      | División         | `10 / 3`        | `3.33...` |
| `//`     | División Entera  | `10 // 3`       | `3`       |
| `%`      | Módulo (Resto)   | `10 % 3`        | `1`       |

---

**Y el más potente...**

| Operador | Nombre           | Ejemplo         | Resultado |
|----------|------------------|-----------------|-----------|
| `**`     | Exponenciación   | `2 ** 3`        | `8`       |
|          |                  | (2 elevado a 3) |           |

---

**Ejemplo Práctico:**
```python
a = 15
b = 4

print(f"Suma: {a + b}")       # 19
print(f"Resta: {a - b}")      # 11
print(f"Multiplicación: {a * b}") # 60
print(f"División: {a / b}")     # 3.75
print(f"División Entera: {a // b}") # 3
print(f"Módulo: {a % b}")      # 3 (15 = 4*3 + 3)
print(f"Potencia: {a ** 2}")   # 225 (15 al cuadrado)
```

---

**Ejercicio: Calculadora de Área** 📐

---

**Consigna:**
Calcula el área de un rectángulo.
1.  Define una variable `ancho` con valor `7.5`.
2.  Define una variable `alto` con valor `4`.
3.  Usa el operador de multiplicación para calcular el área.
4.  Imprime el resultado.

---

**Solución al Ejercicio:** ✅

```python
ancho = 7.5
alto = 4

area = ancho * alto
print(f"El área del rectángulo es: {area}") # Output: El área del rectángulo es: 30.0
```

---

## ⚖️ Operadores Relacionales (Comparación)

---

Nos permiten **comparar** dos valores.
El resultado de una comparación siempre es un valor **booleano**: `True` o `False`. ✅❌

---

**Tabla de Operadores Relacionales:**

| Operador | Nombre                   | Ejemplo       | Resultado |
|----------|--------------------------|---------------|-----------|
| `==`     | Igual a                  | `5 == 5`      | `True`    |
| `!=`     | Diferente de (No igual a)| `10 != 5`     | `True`    |
| `>`      | Mayor que                | `7 > 3`       | `True`    |

---

**Más Operadores Relacionales:**

| Operador | Nombre             | Ejemplo       | Resultado |
|----------|--------------------|---------------|-----------|
| `<`      | Menor que          | `2 < 8`       | `True`    |
| `>=`     | Mayor o igual que  | `5 >= 5`      | `True`    |
| `<=`     | Menor o igual que  | `4 <= 2`      | `False`   |

---

**Ejemplo Práctico:**
```python
edad_juan = 20
edad_maria = 25

print(f"¿Juan es mayor que María? {edad_juan > edad_maria}") # False
print(f"¿Juan y María tienen la misma edad? {edad_juan == edad_maria}") # False
print(f"¿María es mayor o igual que Juan? {edad_maria >= edad_juan}") # True

nombre = "Ana"
otro_nombre = "ana"
print(f"¿Son los nombres iguales? {nombre == otro_nombre}") # False (sensible a mayúsculas)
```

---

**Ejercicio: ¿Aprobado o Reprobado?** 🎓

---

**Consigna:**
Determina si un estudiante aprobó o no.
1.  Define una variable `calificacion` con valor `75`.
2.  Define una variable `minimo_aprobacion` con valor `70`.
3.  Usa un operador relacional para verificar si `calificacion` es mayor o igual que `minimo_aprobacion`.
4.  Imprime el resultado booleano.

---

**Solución al Ejercicio:** ✅

```python
calificacion = 75
minimo_aprobacion = 70

aprobado = calificacion >= minimo_aprobacion
print(f"¿El estudiante aprobó? {aprobado}") # Output: ¿El estudiante aprobó? True
```

---

## 💡 Operadores Lógicos

---

Nos permiten **combinar** o **modificar** expresiones booleanas.
Son esenciales para tomar decisiones complejas en tu código. 🚦

---

**Los tres operadores lógicos principales:**
*   `and` (Y lógico)
*   `or` (O lógico)
*   `not` (Negación lógica)

---

**`and` (Y lógico):**
Retorna `True` si **AMBAS** condiciones son `True`.
Si una es `False`, el resultado es `False`.

**Tabla de `and`:**

| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| `True`      | `True`      | `True`    |
| `True`      | `False`     | `False`   |
| `False`     | `True`      | `False`   |
| `False`     | `False`     | `False`   |

---

**`or` (O lógico):**
Retorna `True` si **AL MENOS UNA** de las condiciones es `True`.
Solo es `False` si **AMBAS** son `False`.

**Tabla de `or`:**

| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| `True`      | `True`      | `True`    |
| `True`      | `False`     | `True`    |
| `False`     | `True`      | `True`    |
| `False`     | `False`     | `False`   |

---

**`not` (Negación lógica):**
Invierte el valor booleano. `True` se vuelve `False` y viceversa.

**Tabla de `not`:**

| Condición | Resultado |
|-----------|-----------|
| `True`    | `False`   |
| `False`   | `True`    |

---

**Ejemplo Práctico:**
```python
es_dia_soleado = True
tengo_sombrilla = False
voy_a_playa = True

# ¿Puedo ir a la playa SI hace sol Y tengo sombrilla?
print(f"¿Playa con sol y sombrilla? {es_dia_soleado and tengo_sombrilla}") # False

# ¿Puedo ir al cine SI hace sol O tengo sombrilla?
print(f"¿Cine con sol o sombrilla? {es_dia_soleado or tengo_sombrilla}") # True

# ¿NO voy a la playa?
print(f"¿No voy a la playa? {not voy_a_playa}") # False
```

---

**Ejercicio: Acceso al Sistema** 🔐

---

**Consigna:**
Un usuario puede acceder si su contraseña es correcta Y su cuenta no está bloqueada.
1.  Define `contrasena_correcta` como `True`.
2.  Define `cuenta_bloqueada` como `False`.
3.  Usa operadores lógicos para determinar si el usuario tiene acceso.
4.  Imprime el resultado.

---

**Solución al Ejercicio:** ✅

```python
contrasena_correcta = True
cuenta_bloqueada = False

# El usuario tiene acceso si la contraseña es correcta Y la cuenta NO está bloqueada.
tiene_acceso = contrasena_correcta and (not cuenta_bloqueada)
print(f"¿Tiene acceso el usuario? {tiene_acceso}") # Output: ¿Tiene acceso el usuario? True
```

---

## ➡️ Operadores de Asignación

---

Sirven para **asignar un valor a una variable**.
El operador `=` es el más básico.

---

**Operador de Asignación Simple:**
`variable = valor`

```python
contador = 0 # Asigna el valor 0 a la variable 'contador'
```

---

**Operadores de Asignación Compuesta:**
Son atajos para realizar una operación y luego asignar el resultado.

**Tabla de Operadores de Asignación Compuesta:**

| Operador | Equivalente a    | Ejemplo       | Resultado |
|----------|------------------|---------------|-----------|
| `+=`     | `x = x + y`      | `x += 5`      | `x = x + 5` |
| `-=`     | `x = x - y`      | `x -= 2`      | `x = x - 2` |
| `*=`     | `x = x * y`      | `x *= 3`      | `x = x * 3` |
| `/=`     | `x = x / y`      | `x /= 2`      | `x = x / 2` |

---

**Más Operadores de Asignación Compuesta:**

| Operador | Equivalente a    | Ejemplo       | Resultado |
|----------|------------------|---------------|-----------|
| `//=`    | `x = x // y`     | `x //= 4`     | `x = x // 4` |
| `%=`     | `x = x % y`      | `x %= 3`      | `x = x % 3` |
| `**=`    | `x = x ** y`     | `x **= 2`     | `x = x ** 2` |

---

**Ejemplo Práctico:**
```python
saldo = 100 # Saldo inicial

saldo += 50 # saldo = saldo + 50 (saldo ahora es 150)
print(f"Saldo después de depósito: {saldo}")

saldo -= 20 # saldo = saldo - 20 (saldo ahora es 130)
print(f"Saldo después de retiro: {saldo}")

multiplicador = 2
multiplicador *= 3 # multiplicador = multiplicador * 3 (multiplicador ahora es 6)
print(f"Multiplicador actualizado: {multiplicador}")
```

---

**Ejercicio: Contador de Puntos** 🎮

---

**Consigna:**
Un jugador obtiene puntos en un juego.
1.  Define una variable `puntuacion` con valor `0`.
2.  El jugador gana 100 puntos. Usa un operador de asignación para actualizar `puntuacion`.
3.  Luego, la puntuación se duplica por un bonus. Usa otro operador de asignación para esto.
4.  Imprime la `puntuacion` final.

---

**Solución al Ejercicio:** ✅

```python
puntuacion = 0

# El jugador gana 100 puntos
puntuacion += 100 # puntuacion ahora es 100

# La puntuación se duplica
puntuacion *= 2 # puntuacion ahora es 200

print(f"Puntuación final: {puntuacion}") # Output: Puntuación final: 200
```

---

## 🔍 Operadores de Membresía (`in`, `not in`)

---

Nos permiten verificar si un valor se encuentra **dentro de una secuencia** (como una cadena de texto, una lista o una tupla).
Piensa: "¿Está 'manzana' en mi cesta de frutas?" 🍎🧺

---

**Operadores de Membresía:**
*   `in`: Retorna `True` si el valor está presente en la secuencia.
*   `not in`: Retorna `True` si el valor **NO** está presente en la secuencia.

---

**Ejemplo Práctico:**
```python
frutas = ["manzana", "banana", "cereza"]
texto = "Hola mundo Python"

print(f"¿'banana' está en frutas? {'banana' in frutas}") # True
print(f"¿'uva' está en frutas? {'uva' in frutas}")     # False

print(f"¿'mundo' está en texto? {'mundo' in texto}")   # True
print(f"¿'java' no está en texto? {'java' not in texto}") # True

letra = "o"
print(f"¿La letra 'o' está en 'Python'? {letra in 'Python'}") # True
```

---

**Ejercicio: Buscador de Palabras** 📚

---

**Consigna:**
Verifica si una palabra clave está presente en una frase.
1.  Define `frase = "Python es un lenguaje de programación poderoso"`.
2.  Define `palabra_clave = "lenguaje"`.
3.  Usa el operador `in` para verificar si `palabra_clave` está en `frase`.
4.  Imprime el resultado.

---

**Solución al Ejercicio:** ✅

```python
frase = "Python es un lenguaje de programación poderoso"
palabra_clave = "lenguaje"

esta_presente = palabra_clave in frase
print(f"¿La palabra '{palabra_clave}' está en la frase? {esta_presente}")
# Output: ¿La palabra 'lenguaje' está en la frase? True
```

---

## 🆔 Operadores de Identidad (`is`, `is not`)

---

Nos permiten verificar si dos variables se refieren al **mismo objeto en memoria**.
Es diferente de `==` que compara solo los *valores*.
Piensa: "¿Son estas dos llaves exactamente la MISMA llave?" 🔑🔑

---

**Operadores de Identidad:**
*   `is`: Retorna `True` si ambos operandos son el mismo objeto.
*   `is not`: Retorna `True` si ambos operandos **NO** son el mismo objeto.

---

**Diferencia clave: `is` vs `==`**
*   `==` compara **valores**.
*   `is` compara **identidad** (si es el mismo objeto).

```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3] # Nueva lista, mismo contenido
lista3 = lista1    # 'lista3' ahora apunta al MISMO objeto que 'lista1'

print(f"lista1 == lista2: {lista1 == lista2}") # True (mismo valor)
print(f"lista1 is lista2: {lista1 is lista2}") # False (objetos diferentes en memoria)

print(f"lista1 == lista3: {lista1 == lista3}") # True (mismo valor)
print(f"lista1 is lista3: {lista1 is lista3}") # True (es el mismo objeto)
```

---

**Ejemplo con números y cadenas (inmutables):**
Para tipos inmutables (números, cadenas), Python a veces optimiza y usa el mismo objeto para valores idénticos.
Pero no siempre debes confiar en `is` para comparar valores de inmutables. Usa `==`.

```python
a = 10
b = 10
print(f"a is b: {a is b}") # True (Python optimiza enteros pequeños)

s1 = "Hola"
s2 = "Hola"
print(f"s1 is s2: {s1 is s2}") # True (Python optimiza cadenas cortas)

s3 = "Esta es una cadena muy larga que Python no siempre optimiza igual"
s4 = "Esta es una cadena muy larga que Python no siempre optimiza igual"
print(f"s3 is s4: {s3 is s4}") # Puede ser True o False, depende de la implementación de Python
```

---

**Ejercicio: ¿Mismo Objeto?** 👯

---

**Consigna:**
1.  Crea una lista `mi_primer_lista = [10, 20]`.
2.  Crea una segunda lista `mi_segunda_lista = [10, 20]`.
3.  Crea una tercera variable `referencia_lista = mi_primer_lista`.
4.  Usa `is` para comparar `mi_primer_lista` con `mi_segunda_lista`.
5.  Usa `is` para comparar `mi_primer_lista` con `referencia_lista`.
6.  Imprime ambos resultados.

---

**Solución al Ejercicio:** ✅

```python
mi_primer_lista = [10, 20]
mi_segunda_lista = [10, 20]
referencia_lista = mi_primer_lista

print(f"¿'mi_primer_lista' es el mismo objeto que 'mi_segunda_lista'? {mi_primer_lista is mi_segunda_lista}")
# Output: False (son dos listas diferentes en memoria, aunque con el mismo contenido)

print(f"¿'mi_primer_lista' es el mismo objeto que 'referencia_lista'? {mi_primer_lista is referencia_lista}")
# Output: True ('referencia_lista' apunta al mismo objeto que 'mi_primer_lista')
```

---

# Evaluación de Expresiones 🧠

---

Cuando tienes una expresión con varios operadores, ¿en qué orden se ejecutan?
¡Aquí entran la **precedencia** y la **asociatividad**!

---

## Precedencia de Operadores 🏆

---

La **precedencia** determina el orden en que se evalúan los operadores.
Es como el "orden de las operaciones" en matemáticas (PEMDAS/BODMAS).

---

**Orden general (de mayor a menor precedencia):**
1.  **Paréntesis `()`**: ¡Lo que está dentro se evalúa primero! 🚀
2.  **Exponenciación `**`**
3.  **Multiplicación `*`, División `/`, División Entera `//`, Módulo `%`**
4.  **Suma `+`, Resta `-`**
5.  **Comparación `==`, `!=`, `>`, `<`, `>=`, `<=`**
6.  **Identidad `is`, `is not`**
7.  **Membresía `in`, `not in`**
8.  **Negación lógica `not`**
9.  **AND lógico `and`**
10. **OR lógico `or`**

---

**Ejemplo de Precedencia:**
```python
resultado = 5 + 3 * 2 # ¿Es 16 o 11?
# Multiplicación (*) tiene mayor precedencia que Suma (+)
# 1. 3 * 2 = 6
# 2. 5 + 6 = 11
resultado = 11
print(resultado)
```

---

**Usando Paréntesis para Forzar el Orden:**
```python
resultado_forzado = (5 + 3) * 2
# Paréntesis se evalúa primero
# 1. (5 + 3) = 8
# 2. 8 * 2 = 16
resultado_forzado = 16
print(resultado_forzado)
```
¡Los paréntesis son tus amigos para la claridad! 😉

---

## Asociatividad de Operadores ↔️

---

La **asociatividad** determina cómo se evalúan los operadores de la **misma precedencia**.
¿De izquierda a derecha o de derecha a izquierda?

---

**Mayoría de operadores en Python:**
Son **asociativos de izquierda a derecha**.
Ejemplo: `10 - 5 - 2`
` (10 - 5) - 2 ` -> ` 5 - 2 ` -> ` 3 `

---

**Excepción importante: Exponenciación `**`**
Es **asociativa de derecha a izquierda**.
Ejemplo: `2 ** 3 ** 2`
` 2 ** (3 ** 2) ` -> ` 2 ** 9 ` -> ` 512 `

---

**Ejemplo de Asociatividad:**
```python
print(10 - 5 - 2) # (10 - 5) - 2 = 5 - 2 = 3
print(2 ** 3 ** 2) # 2 ** (3 ** 2) = 2 ** 9 = 512
```

---

**Ejercicio: Evaluación Compleja** 🤯

---

**Consigna:**
Evalúa la siguiente expresión y predice su resultado. Luego, verifica con Python.
`resultado = 10 + 2 * 5 - (8 / 4) ** 2`

---

**Solución al Ejercicio:** ✅

**Paso a paso:**
1.  **Paréntesis:** `(8 / 4)` -> `2.0`
    Expresión: `10 + 2 * 5 - 2.0 ** 2`
2.  **Exponenciación:** `2.0 ** 2` -> `4.0`
    Expresión: `10 + 2 * 5 - 4.0`
3.  **Multiplicación:** `2 * 5` -> `10`
    Expresión: `10 + 10 - 4.0`
4.  **Suma/Resta (de izquierda a derecha):**
    `10 + 10` -> `20`
    `20 - 4.0` -> `16.0`

**Código:**
```python
resultado = 10 + 2 * 5 - (8 / 4) ** 2
print(f"El resultado es: {resultado}") # Output: El resultado es: 16.0
```

---

# ¡Excelente trabajo! 🚀

---

**Hoy dominamos:**
*   **Operadores aritméticos:** para cálculos.
*   **Operadores relacionales:** para comparaciones.
*   **Operadores lógicos:** para decisiones.
*   **Operadores de asignación:** para guardar y actualizar.
*   **Operadores de membresía e identidad:** para verificar contenido y objetos.
*   **Precedencia y asociatividad:** para entender el orden de las operaciones.

---

**¡Sigue explorando!**
¡Los operadores son la base de toda lógica de programación! 🌟