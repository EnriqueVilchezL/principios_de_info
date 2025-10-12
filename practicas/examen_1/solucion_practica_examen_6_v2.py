"""
Solución Completa del Juego de la Vida de Conway
"""

import time


# =============================================================================
# FUNCIÓN PRINCIPAL (PUNTO DE ENTRADA)
# =============================================================================


def main():
    """
    Ejecuta la simulación completa del Juego de la Vida.
    Define todas las variables de configuración localmente.
    """
    
    # 1. DEFINICIÓN DE VARIABLES LOCALES (ANTERIORES CONSTANTES GLOBALES)
    
    # Dimensiones del tablero (filas, columnas)
    dimensiones = (10, 20)  # 10 filas, 20 columnas

    # Número de generaciones a simular
    generaciones = 15

    # Patrón inicial "Glider" (Planeador) - Se mueve diagonalmente
    patron_inicial = [
        (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)
    ]
    
    # Paso 1: Crear el tablero inicial con el patrón
    print("Iniciando simulación del Juego de la Vida de Conway")
    print(f"Dimensiones: {dimensiones[0]} filas × {dimensiones[1]} columnas")
    print(f"Generaciones: {generaciones}")
    print(f"Patrón inicial: Glider (Planeador)\n")

    # Se llama a la función pasando las variables locales
    tablero = crear_tablero(dimensiones, patron_inicial)
    
    # Paso 2: Simular cada generación
    for generacion in range(generaciones):
        # Imprimir encabezado de la generación
        print(f"--- Generación {generacion} ---")
        
        # Llama a la función de impresión
        imprimir_tablero(tablero)
        
        # Llama a la función de cálculo. Solo necesita el tablero_actual.
        tablero = calcular_siguiente_generacion(tablero)
        
        # Pequeña pausa para visualizar mejor (opcional)
        print()  # Línea en blanco entre generaciones
        time.sleep(0.5)  # Pausa de medio segundo
    
    print(" Simulación completada")


# =============================================================================
# FUNCIONES LLAMADAS DESDE main
# =============================================================================

def crear_tablero(dimensiones: tuple[int, int], celdas_vivas: list[tuple[int, int]]) -> list[list[int]]:
    """
    Crea e inicializa el tablero del Juego de la Vida.
    """
    
    # --- PASO 1: EXTRAER DIMENSIONES ---
    filas, columnas = dimensiones
    
    # --- PASO 2: CREAR TABLERO VACÍO ---
    tablero = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(0)
        tablero.append(fila)
    
    # --- PASO 3: MARCAR CELDAS VIVAS ---
    for coordenada in celdas_vivas:
        f, c = coordenada
        
        # Verificar que la coordenada esté dentro de los límites
        if 0 <= f < filas and 0 <= c < columnas:
            tablero[f][c] = 1
    
    return tablero


def imprimir_tablero(tablero: list[list[int]]) -> None:
    """
    Imprime una representación visual del tablero en la consola.
    """
    
    for fila in tablero:
        for celda in fila:
            if celda == 1:
                print('o', end=' ')
            else:
                print('·', end=' ')
        print()


def calcular_siguiente_generacion(tablero_actual: list[list[int]]) -> list[list[int]]:
    """
    Calcula el estado del tablero en la siguiente generación.
    """
    
    # --- PASO 1: OBTENER DIMENSIONES ---
    filas = len(tablero_actual)
    columnas = len(tablero_actual[0])
    
    # --- PASO 2: CREAR NUEVO TABLERO VACÍO ---
    # Creación de un tablero temporal para la próxima generación
    nuevo_tablero = []
    for f in range(filas):
        nuevo_tablero.append([0] * columnas) # Inicialización simplificada
    
    # --- PASO 3: CALCULAR EL ESTADO DE CADA CELDA ---
    for f in range(filas):
        for c in range(columnas):
            estado_actual = tablero_actual[f][c]
            
            # Llama a contar_vecinos
            vecinos = contar_vecinos(tablero_actual, f, c)
            
            # --- APLICAR LAS REGLAS DEL JUEGO DE LA VIDA ---
            if estado_actual == 1:
                if vecinos == 2 or vecinos == 3:
                    nuevo_tablero[f][c] = 1  # Sobrevive
                else:
                    nuevo_tablero[f][c] = 0  # Muere
            
            else:
                if vecinos == 3:
                    nuevo_tablero[f][c] = 1  # Nace
                else:
                    nuevo_tablero[f][c] = 0  # Sigue muerta
    
    return nuevo_tablero


# =============================================================================
# FUNCIONES LLAMADAS DESDE calcular_siguiente_generacion
# =============================================================================

def contar_vecinos(tablero: list[list[int]], fila: int, col: int) -> int:
    """
    Cuenta cuántas celdas vecinas están vivas.
    """
    
    # --- PASO 1: OBTENER DIMENSIONES DEL TABLERO ---
    filas = len(tablero)
    columnas = len(tablero[0])
    
    # --- PASO 2: DEFINIR LOS 8 DESPLAZAMIENTOS POSIBLES ---
    desplazamientos = [
        (-1, -1), (-1,  0), (-1,  1), 
        ( 0, -1), ( 0,  1), 
        ( 1, -1), ( 1,  0), ( 1,  1),
    ]
    
    # --- PASO 3: CONTAR VECINOS VIVOS ---
    vecinos_vivos = 0
    
    for df, dc in desplazamientos:
        fila_vecino = fila + df
        col_vecino = col + dc
        
        # Verificamos que el vecino esté dentro de los límites del tablero
        if 0 <= fila_vecino < filas and 0 <= col_vecino < columnas:
            # Si está dentro de los límites y está vivo
            if tablero[fila_vecino][col_vecino] == 1:
                vecinos_vivos += 1
    
    return vecinos_vivos


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

main()