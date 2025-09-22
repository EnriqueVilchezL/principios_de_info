#!/usr/bin/env python3
"""
Soluciones para Práctica de Examen: Estructuras de Datos Fundamentales
====================================================================

Este archivo contiene las implementaciones de todos los ejercicios
con sus respectivas pruebas de verificación.

Autor: Solución para práctica de examen
Fecha: Septiembre 2025
"""

from typing import List, Dict, Any


# =============================================================================
# EJERCICIO 1: MULTIPLICACIÓN DE MATRICES
# =============================================================================

def multiplicar_matrices(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
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
    # Verificar que las matrices no estén vacías
    if not A or not A[0] or not B or not B[0]:
        raise ValueError("Las matrices no pueden estar vacías")
    
    # Obtener dimensiones
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    
    # Verificar que el número de columnas de A = número de filas de B
    if columnas_A != filas_B:
        raise ValueError(f"Las matrices no pueden multiplicarse ({columnas_A} ≠ {filas_B})")
    
    # Verificar que todas las filas tengan el mismo número de columnas
    for fila in A:
        if len(fila) != columnas_A:
            raise ValueError("La matriz A debe ser rectangular")
    
    for fila in B:
        if len(fila) != columnas_B:
            raise ValueError("La matriz B debe ser rectangular")
    
    # Crear matriz resultado C de dimensiones filas_A × columnas_B
    C = [[0.0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    # Realizar la multiplicación
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


# =============================================================================
# EJERCICIO 2: PRODUCTO PUNTO DE VECTORES
# =============================================================================

def producto_punto(v: List[float], u: List[float]) -> float:
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

def producto_hadamard(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
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
    # Verificar que las matrices no estén vacías
    if not A or not A[0] or not B or not B[0]:
        raise ValueError("Las matrices no pueden estar vacías")
    
    # Obtener dimensiones
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    
    # Verificar que las dimensiones sean iguales
    if filas_A != filas_B or columnas_A != columnas_B:
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    # Verificar que todas las filas tengan el mismo número de columnas
    for fila in A:
        if len(fila) != columnas_A:
            raise ValueError("La matriz A debe ser rectangular")
    
    for fila in B:
        if len(fila) != columnas_B:
            raise ValueError("La matriz B debe ser rectangular")
    
    # Crear matriz resultado
    C = [[0.0 for _ in range(columnas_A)] for _ in range(filas_A)]
    
    # Realizar la multiplicación elemento por elemento
    for i in range(filas_A):
        for j in range(columnas_A):
            C[i][j] = A[i][j] * B[i][j]
    
    return C


# =============================================================================
# EJERCICIO 4: CÁLCULO DE FRECUENCIAS
# =============================================================================

def calcular_frecuencias(elements: List[Any]) -> Dict[Any, int]:
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

def promedio_por_hora(lecturas: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calcula el promedio de humedad por hora.
    
    Args:
        lecturas: Lista de diccionarios con lecturas del sensor
    
    Returns:
        Diccionario con hora como clave y promedio como valor
    """
    if not lecturas:
        return {}
    
    # Agrupar lecturas por hora
    lecturas_por_hora = {}
    
    for lectura in lecturas:
        hora = lectura["hora"][:2]  # Extraer solo la hora (primeros 2 caracteres)
        humedad = lectura["humedad"]
        
        if hora not in lecturas_por_hora:
            lecturas_por_hora[hora] = []
        
        lecturas_por_hora[hora].append(humedad)
    
    # Calcular promedios
    promedios = {}
    for hora, humedades in lecturas_por_hora.items():
        promedio = sum(humedades) / len(humedades)
        promedios[hora] = round(promedio, 2)
    
    return promedios


def promedio_por_dia(lecturas: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calcula el promedio de humedad por día.
    
    Args:
        lecturas: Lista de diccionarios con lecturas del sensor
    
    Returns:
        Diccionario con fecha como clave y promedio como valor
    """
    if not lecturas:
        return {}
    
    # Agrupar lecturas por día
    lecturas_por_dia = {}
    
    for lectura in lecturas:
        fecha = lectura["fecha"]
        humedad = lectura["humedad"]
        
        if fecha not in lecturas_por_dia:
            lecturas_por_dia[fecha] = []
        
        lecturas_por_dia[fecha].append(humedad)
    
    # Calcular promedios
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
    print("="*60)
    print("VERIFICACIÓN EJERCICIO 1: MULTIPLICACIÓN DE MATRICES")
    print("="*60)
    
    # Ejemplo 1: Multiplicación válida
    print("\n--- Ejemplo 1: Multiplicación válida ---")
    A = [[1, 2],
         [3, 4]]
    B = [[5, 6],
         [7, 8]]
    
    resultado = multiplicar_matrices(A, B)
    esperado = [[19, 22], [43, 50]]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 2: Multiplicación no válida
    print("\n--- Ejemplo 2: Multiplicación no válida ---")
    A = [[1, 2, 3]]      # 1×3
    B = [[4, 5]]         # 1×2
    
    try:
        resultado = multiplicar_matrices(A, B)
        print("❌ Error: Debería haber lanzado excepción")
    except ValueError as e:
        print(f"✓ Excepción correcta: {e}")
    
    # Ejemplo 3: Multiplicación rectangular
    print("\n--- Ejemplo 3: Multiplicación rectangular ---")
    A = [[1, 2, 3],
         [4, 5, 6]]      # 2×3
    B = [[7, 8],
         [9, 10],
         [11, 12]]       # 3×2
    
    resultado = multiplicar_matrices(A, B)
    esperado = [[58, 64], [139, 154]]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")


def verificar_ejercicio_2():
    """Verifica todos los ejemplos del ejercicio 2."""
    print("\n\n" + "="*60)
    print("VERIFICACIÓN EJERCICIO 2: PRODUCTO PUNTO DE VECTORES")
    print("="*60)
    
    # Ejemplo 1: Producto punto válido
    print("\n--- Ejemplo 1: Producto punto válido ---")
    v = [1, 2, 3]
    u = [4, 5, 6]
    
    resultado = producto_punto(v, u)
    esperado = 32.0
    
    print(f"v = {v}")
    print(f"u = {u}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 2: Vectores de diferente longitud
    print("\n--- Ejemplo 2: Vectores de diferente longitud ---")
    v = [1, 2, 3]
    u = [4, 5]
    
    try:
        resultado = producto_punto(v, u)
        print("❌ Error: Debería haber lanzado excepción")
    except ValueError as e:
        print(f"✓ Excepción correcta: {e}")
    
    # Ejemplo 3: Vectores con decimales
    print("\n--- Ejemplo 3: Vectores con decimales ---")
    v = [1.5, 2.5, 3.5]
    u = [2.0, 3.0, 4.0]
    
    resultado = producto_punto(v, u)
    esperado = 24.5
    
    print(f"v = {v}")
    print(f"u = {u}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")


def verificar_ejercicio_3():
    """Verifica todos los ejemplos del ejercicio 3."""
    print("\n\n" + "="*60)
    print("VERIFICACIÓN EJERCICIO 3: PRODUCTO HADAMARD DE MATRICES")
    print("="*60)
    
    # Ejemplo 1: Producto Hadamard válido
    print("\n--- Ejemplo 1: Producto Hadamard válido ---")
    A = [[1, 2],
         [3, 4]]
    B = [[5, 6],
         [7, 8]]
    
    resultado = producto_hadamard(A, B)
    esperado = [[5, 12], [21, 32]]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 2: Matrices de diferentes dimensiones
    print("\n--- Ejemplo 2: Matrices de diferentes dimensiones ---")
    A = [[1, 2, 3]]      # 1×3
    B = [[4, 5],
         [6, 7]]         # 2×2
    
    try:
        resultado = producto_hadamard(A, B)
        print("❌ Error: Debería haber lanzado excepción")
    except ValueError as e:
        print(f"✓ Excepción correcta: {e}")
    
    # Ejemplo 3: Matrices 3×3
    print("\n--- Ejemplo 3: Matrices 3×3 ---")
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [[2, 2, 2],
         [3, 3, 3],
         [4, 4, 4]]
    
    resultado = producto_hadamard(A, B)
    esperado = [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")


def verificar_ejercicio_4():
    """Verifica todos los ejemplos del ejercicio 4."""
    print("\n\n" + "="*60)
    print("VERIFICACIÓN EJERCICIO 4: CÁLCULO DE FRECUENCIAS")
    print("="*60)
    
    # Ejemplo 1: Lista de números
    print("\n--- Ejemplo 1: Lista de números ---")
    elementos = [1, 2, 3, 2, 1, 3, 3, 1]
    
    resultado = calcular_frecuencias(elementos)
    esperado = {1: 3, 2: 2, 3: 3}
    
    print(f"Elementos: {elementos}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 2: Lista de strings
    print("\n--- Ejemplo 2: Lista de strings ---")
    elementos = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
    
    resultado = calcular_frecuencias(elementos)
    esperado = {"manzana": 3, "banana": 2, "naranja": 1}
    
    print(f"Elementos: {elementos}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 3: Lista mixta
    print("\n--- Ejemplo 3: Lista mixta ---")
    elementos = [1, "a", 1, "b", "a", 2.5, 2.5]
    
    resultado = calcular_frecuencias(elementos)
    esperado = {1: 2, "a": 2, "b": 1, 2.5: 2}
    
    print(f"Elementos: {elementos}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")
    
    # Ejemplo 4: Lista vacía
    print("\n--- Ejemplo 4: Lista vacía ---")
    elementos = []
    
    resultado = calcular_frecuencias(elementos)
    esperado = {}
    
    print(f"Elementos: {elementos}")
    print(f"Resultado: {resultado}")
    print(f"Esperado:  {esperado}")
    print(f"✓ Correcto: {resultado == esperado}")


def verificar_ejercicio_5():
    """Verifica todos los ejemplos del ejercicio 5."""
    print("\n\n" + "="*60)
    print("VERIFICACIÓN EJERCICIO 5: PROMEDIO DE LECTURAS DE SENSOR")
    print("="*60)
    
    # Datos de entrada
    lecturas = [
        {"fecha": "15/09/2025", "hora": "08:30", "humedad": 65.5},
        {"fecha": "15/09/2025", "hora": "08:45", "humedad": 67.2},
        {"fecha": "15/09/2025", "hora": "09:15", "humedad": 63.8},
        {"fecha": "15/09/2025", "hora": "09:30", "humedad": 64.1},
        {"fecha": "16/09/2025", "hora": "08:20", "humedad": 70.3},
        {"fecha": "16/09/2025", "hora": "09:10", "humedad": 68.7},
        {"fecha": "16/09/2025", "hora": "10:00", "humedad": 62.5}
    ]
    
    print(f"\nDatos de entrada: {len(lecturas)} lecturas")
    for lectura in lecturas:
        print(f"  {lectura}")
    
    # Función 1: promedio_por_hora
    print("\n--- Función 1: promedio_por_hora ---")
    resultado_hora = promedio_por_hora(lecturas)
    esperado_hora = {"08": 67.67, "09": 65.53, "10": 62.5}
    
    print(f"Resultado: {resultado_hora}")
    print(f"Esperado:  {esperado_hora}")
    print(f"✓ Correcto: {resultado_hora == esperado_hora}")
    
    # Función 2: promedio_por_dia
    print("\n--- Función 2: promedio_por_dia ---")
    resultado_dia = promedio_por_dia(lecturas)
    esperado_dia = {"15/09/2025": 65.15, "16/09/2025": 67.17}
    
    print(f"Resultado: {resultado_dia}")
    print(f"Esperado:  {esperado_dia}")
    print(f"✓ Correcto: {resultado_dia == esperado_dia}")
    
    # Caso especial: Lista vacía
    print("\n--- Caso especial: Lista vacía ---")
    lecturas_vacias = []
    
    resultado_hora_vacia = promedio_por_hora(lecturas_vacias)
    resultado_dia_vacia = promedio_por_dia(lecturas_vacias)
    esperado_vacio = {}
    
    print(f"Resultado hora vacía: {resultado_hora_vacia}")
    print(f"Resultado día vacía:  {resultado_dia_vacia}")
    print(f"Esperado:  {esperado_vacio}")
    print(f"✓ Correcto hora: {resultado_hora_vacia == esperado_vacio}")
    print(f"✓ Correcto día:  {resultado_dia_vacia == esperado_vacio}")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

def main():
    """Ejecuta todas las verificaciones."""
    print("VERIFICACIÓN COMPLETA DE EJERCICIOS")
    print("Estructuras de Datos Fundamentales")
    print("Fecha:", "21/09/2025")
    
    try:
        verificar_ejercicio_1()
        verificar_ejercicio_2()
        verificar_ejercicio_3()
        verificar_ejercicio_4()
        verificar_ejercicio_5()
        
        print("\n\n" + "="*60)
        print("🎉 TODAS LAS VERIFICACIONES COMPLETADAS EXITOSAMENTE")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error durante la verificación: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()