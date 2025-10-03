# =============================================================================
# EJERCICIO 1: MULTIPLICACIÓN DE MATRICES
# =============================================================================


def multiplicar_matrices(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Multiplica dos matrices A y B.

    Args:
        A: Matriz de dimensiones m×n
        B: Matriz de dimensiones n×p

    Returns:
        Matriz resultante C de dimensiones m×p

    Raises:
        ValueError: Si las matrices no pueden multiplicarse
    """
    if not A or not A[0] or not B or not B[0]:
        raise ValueError("Las matrices no pueden estar vacías")

    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])

    if columnas_A != filas_B:
        raise ValueError(f"Las matrices no pueden multiplicarse ({columnas_A} ≠ {filas_B})")

    for fila in A:
        if len(fila) != columnas_A:
            raise ValueError("La matriz A debe ser rectangular")

    for fila in B:
        if len(fila) != columnas_B:
            raise ValueError("La matriz B debe ser rectangular")

    C = [[0.0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


# =============================================================================
# EJERCICIO 2: PRODUCTO PUNTO DE VECTORES
# =============================================================================


def producto_punto(v: list[float], u: list[float]) -> float:
    """
    Calcula el producto punto de dos vectores.

    Args:
        v: Primer vector
        u: Segundo vector

    Returns:
        Producto punto como número escalar

    Raises:
        ValueError: Si los vectores tienen diferente longitud
    """
    if len(v) != len(u):
        raise ValueError("Los vectores deben tener la misma longitud")

    if len(v) == 0:
        raise ValueError("Los vectores no pueden estar vacíos")

    resultado = 0.0
    for i in range(len(v)):
        resultado += v[i] * u[i]

    return resultado


# =============================================================================
# EJERCICIO 3: PRODUCTO HADAMARD DE MATRICES
# =============================================================================


def producto_hadamard(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Calcula el producto Hadamard (elemento por elemento) de dos matrices.

    Args:
        A: Primera matriz
        B: Segunda matriz

    Returns:
        Matriz resultado del producto Hadamard

    Raises:
        ValueError: Si las matrices no tienen las mismas dimensiones
    """
    if not A or not A[0] or not B or not B[0]:
        raise ValueError("Las matrices no pueden estar vacías")

    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])

    if filas_A != filas_B or columnas_A != columnas_B:
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    for fila in A:
        if len(fila) != columnas_A:
            raise ValueError("La matriz A debe ser rectangular")

    for fila in B:
        if len(fila) != columnas_B:
            raise ValueError("La matriz B debe ser rectangular")

    C = [[0.0 for _ in range(columnas_A)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_A):
            C[i][j] = A[i][j] * B[i][j]

    return C


# =============================================================================
# EJERCICIO 4: CÁLCULO DE FRECUENCIAS
# =============================================================================


def calcular_frecuencias(elements: list) -> dict:
    """
    Calcula las frecuencias de aparición de cada elemento en una lista.

    Args:
        elements: Lista de elementos de cualquier tipo

    Returns:
        Diccionario con elemento como clave y frecuencia como valor
    """
    frecuencias = {}

    for elemento in elements:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    return frecuencias


# =============================================================================
# EJERCICIO 5: PROMEDIO DE LECTURAS DE SENSOR
# =============================================================================


def promedio_por_hora(lecturas: list[dict]) -> dict[str, float]:
    """
    Calcula el promedio de humedad por hora.

    Args:
        lecturas: Lista de diccionarios con lecturas del sensor

    Returns:
        Diccionario con hora como clave y promedio como valor
    """
    if not lecturas:
        return {}

    lecturas_por_hora = {}

    for lectura in lecturas:
        hora = lectura["hora"][:2]  # Extraer solo la hora (primeros 2 caracteres)
        humedad = lectura["humedad"]

        if hora not in lecturas_por_hora:
            lecturas_por_hora[hora] = []

        lecturas_por_hora[hora].append(humedad)

    promedios = {}
    for hora, humedades in lecturas_por_hora.items():
        promedio = sum(humedades) / len(humedades)
        promedios[hora] = round(promedio, 2)

    return promedios


def promedio_por_dia(lecturas: list[dict[str, any]]) -> dict[str, float]:
    """
    Calcula el promedio de humedad por día.

    Args:
        lecturas: Lista de diccionarios con lecturas del sensor

    Returns:
        Diccionario con fecha como clave y promedio como valor
    """
    if not lecturas:
        return {}

    lecturas_por_dia = {}

    for lectura in lecturas:
        fecha = lectura["fecha"]
        humedad = lectura["humedad"]

        if fecha not in lecturas_por_dia:
            lecturas_por_dia[fecha] = []

        lecturas_por_dia[fecha].append(humedad)

    promedios = {}
    for fecha, humedades in lecturas_por_dia.items():
        promedio = sum(humedades) / len(humedades)
        promedios[fecha] = round(promedio, 2)

    return promedios


# =============================================================================
# FUNCIONES DE VERIFICACIÓN Y PRUEBAS
# =============================================================================


def verificar_ejercicio_1():
    """Verifica todos los ejemplos del ejercicio 1."""
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado = multiplicar_matrices(A, B)
    esperado = [[19.0, 22.0], [43.0, 50.0]]
    assert resultado == esperado, f"Ejemplo 1 falló: {resultado} != {esperado}"

    A = [[1, 2, 3]]  # 1×3
    B = [[4, 5]]  # 1×2
    try:
        resultado = multiplicar_matrices(A, B)
        assert False, "Ejemplo 2: Debería haber lanzado excepción"
    except ValueError:
        pass  # Comportamiento esperado

    A = [[1, 2, 3], [4, 5, 6]]  # 2×3
    B = [[7, 8], [9, 10], [11, 12]]  # 3×2
    resultado = multiplicar_matrices(A, B)
    esperado = [[58.0, 64.0], [139.0, 154.0]]
    assert resultado == esperado, f"Ejemplo 3 falló: {resultado} != {esperado}"


def verificar_ejercicio_2():
    """Verifica todos los ejemplos del ejercicio 2."""
    v = [1, 2, 3]
    u = [4, 5, 6]
    resultado = producto_punto(v, u)
    esperado = 32.0
    assert resultado == esperado, f"Ejemplo 1 falló: {resultado} != {esperado}"

    v = [1, 2, 3]
    u = [4, 5]
    try:
        resultado = producto_punto(v, u)
        assert False, "Ejemplo 2: Debería haber lanzado excepción"
    except ValueError:
        pass  # Comportamiento esperado

    v = [1.5, 2.5, 3.5]
    u = [2.0, 3.0, 4.0]
    resultado = producto_punto(v, u)
    esperado = 24.5
    assert resultado == esperado, f"Ejemplo 3 falló: {resultado} != {esperado}"


def verificar_ejercicio_3():
    """Verifica todos los ejemplos del ejercicio 3."""
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado = producto_hadamard(A, B)
    esperado = [[5, 12], [21, 32]]
    assert resultado == esperado, f"Ejemplo 1 falló: {resultado} != {esperado}"

    A = [[1, 2, 3]]  # 1×3
    B = [[4, 5], [6, 7]]  # 2×2
    try:
        resultado = producto_hadamard(A, B)
        assert False, "Ejemplo 2: Debería haber lanzado excepción"
    except ValueError:
        pass  # Comportamiento esperado

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
    resultado = producto_hadamard(A, B)
    esperado = [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
    assert resultado == esperado, f"Ejemplo 3 falló: {resultado} != {esperado}"


def verificar_ejercicio_4():
    """Verifica todos los ejemplos del ejercicio 4."""
    elementos = [1, 2, 3, 2, 1, 3, 3, 1]
    resultado = calcular_frecuencias(elementos)
    esperado = {1: 3, 2: 2, 3: 3}
    assert resultado == esperado, f"Ejemplo 1 falló: {resultado} != {esperado}"

    elementos = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
    resultado = calcular_frecuencias(elementos)
    esperado = {"manzana": 3, "banana": 2, "naranja": 1}
    assert resultado == esperado, f"Ejemplo 2 falló: {resultado} != {esperado}"

    elementos = [1, "a", 1, "b", "a", 2.5, 2.5]
    resultado = calcular_frecuencias(elementos)
    esperado = {1: 2, "a": 2, "b": 1, 2.5: 2}
    assert resultado == esperado, f"Ejemplo 3 falló: {resultado} != {esperado}"

    elementos = []
    resultado = calcular_frecuencias(elementos)
    esperado = {}
    assert resultado == esperado, f"Ejemplo 4 falló: {resultado} != {esperado}"


def verificar_ejercicio_5():
    """Verifica todos los ejemplos del ejercicio 5."""
    lecturas = [
        {"fecha": "15/09/2025", "hora": "08:30", "humedad": 65.5},
        {"fecha": "15/09/2025", "hora": "08:45", "humedad": 67.2},
        {"fecha": "15/09/2025", "hora": "09:15", "humedad": 63.8},
        {"fecha": "15/09/2025", "hora": "09:30", "humedad": 64.1},
        {"fecha": "16/09/2025", "hora": "08:20", "humedad": 70.3},
        {"fecha": "16/09/2025", "hora": "09:10", "humedad": 68.7},
        {"fecha": "16/09/2025", "hora": "10:00", "humedad": 62.5},
    ]

    resultado_hora = promedio_por_hora(lecturas)
    esperado_hora = {"08": 67.67, "09": 65.53, "10": 62.5}
    assert resultado_hora == esperado_hora, (
        f"Promedio por hora falló: {resultado_hora} != {esperado_hora}"
    )

    resultado_dia = promedio_por_dia(lecturas)
    esperado_dia = {"15/09/2025": 65.15, "16/09/2025": 67.17}
    assert resultado_dia == esperado_dia, (
        f"Promedio por día falló: {resultado_dia} != {esperado_dia}"
    )

    lecturas_vacias = []
    resultado_hora_vacia = promedio_por_hora(lecturas_vacias)
    resultado_dia_vacia = promedio_por_dia(lecturas_vacias)
    esperado_vacio = {}
    assert resultado_hora_vacia == esperado_vacio, (
        f"Hora vacía falló: {resultado_hora_vacia} != {esperado_vacio}"
    )
    assert resultado_dia_vacia == esperado_vacio, (
        f"Día vacía falló: {resultado_dia_vacia} != {esperado_vacio}"
    )


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================


def main():
    """Ejecuta todas las verificaciones."""
    print("Running verification tests...")

    try:
        verificar_ejercicio_1()
        print("✓ Ejercicio 1: Multiplicación de matrices - PASSED")

        verificar_ejercicio_2()
        print("✓ Ejercicio 2: Producto punto de vectores - PASSED")

        verificar_ejercicio_3()
        print("✓ Ejercicio 3: Producto Hadamard - PASSED")

        verificar_ejercicio_4()
        print("✓ Ejercicio 4: Cálculo de frecuencias - PASSED")

        verificar_ejercicio_5()
        print("✓ Ejercicio 5: Promedio de lecturas de sensor - PASSED")

        print("\n🎉 ALL TESTS PASSED SUCCESSFULLY!")

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        raise
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback

        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
