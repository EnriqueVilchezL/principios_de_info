"""
Solución Completa del Juego de la Vida de Conway

Este archivo contiene la solución completa con comentarios detallados para
estudiantes principiantes.

Autor: Sistema de Simulación Conway
Fecha: Octubre 2025
"""

import time


# =============================================================================
# DATOS DE CONFIGURACIÓN (YA PROPORCIONADOS)
# =============================================================================

# Dimensiones del tablero (filas, columnas)
DIMENSIONES = (10, 20)  # 10 filas, 20 columnas

# Número de generaciones a simular
GENERACIONES = 15

# Patrón inicial "Glider" (Planeador) - Se mueve diagonalmente
PATRON_INICIAL = [
    (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)
]


# =============================================================================
# FUNCIONES IMPLEMENTADAS CON COMENTARIOS EDUCATIVOS
# =============================================================================


def crear_tablero(dimensiones: tuple[int, int], celdas_vivas: list[tuple[int, int]]) -> list[list[int]]:
    """
    Crea e inicializa el tablero del Juego de la Vida.
    
    El tablero es una cuadrícula donde cada celda puede estar viva (1) o muerta (0).
    """
    
    # --- PASO 1: EXTRAER DIMENSIONES ---
    
    # La tupla dimensiones contiene (filas, columnas)
    # Usamos desempaquetado para obtener estos valores
    filas, columnas = dimensiones
    
    # --- PASO 2: CREAR TABLERO VACÍO ---
    
    # Creamos una lista de listas, inicializada toda con ceros (celdas muertas)
    # Esto se hace en dos pasos:
    # 1. Creamos una fila: [0, 0, 0, ..., 0] con 'columnas' ceros
    # 2. Repetimos esa fila 'filas' veces para formar el tablero completo
    
    tablero = []
    for f in range(filas):
        # Creamos una fila nueva llena de ceros
        fila = []
        for c in range(columnas):
            fila.append(0)
        # Agregamos esta fila al tablero
        tablero.append(fila)
    
    # Nota: Lo anterior también se puede hacer en una sola línea así:
    # tablero = [[0 for c in range(columnas)] for f in range(filas)]
    
    # --- PASO 3: MARCAR CELDAS VIVAS ---
    
    # Ahora recorremos la lista de celdas que deben estar vivas
    for coordenada in celdas_vivas:
        # Cada coordenada es una tupla (fila, columna)
        f, c = coordenada
        
        # IMPORTANTE: Verificar que la coordenada esté dentro de los límites
        # - La fila debe estar entre 0 y (filas - 1)
        # - La columna debe estar entre 0 y (columnas - 1)
        if 0 <= f < filas and 0 <= c < columnas:
            # Si la coordenada es válida, marcamos esa celda como viva (1)
            tablero[f][c] = 1
        # Si la coordenada está fuera de límites, simplemente la ignoramos
        # (no hacemos nada, continuamos con la siguiente)
    
    # Retornamos el tablero completamente inicializado
    return tablero


def imprimir_tablero(tablero: list[list[int]]) -> None:
    """
    Imprime una representación visual del tablero en la consola.
    
    Usa símbolos para representar celdas vivas (■) y muertas (·).
    """
    
    # Recorremos cada fila del tablero
    for fila in tablero:
        # Para cada celda en esta fila
        for celda in fila:
            # Verificamos si la celda está viva o muerta
            if celda == 1:
                # Celda viva: imprimimos un cuadrado lleno
                # end=' ' hace que no haya salto de línea, solo un espacio
                print('■', end=' ')
            else:
                # Celda muerta: imprimimos un punto medio
                print('·', end=' ')
        
        # Al terminar una fila, imprimimos un salto de línea
        # (para pasar a la siguiente fila del tablero)
        print()  # print() sin argumentos hace un salto de línea


def contar_vecinos(tablero: list[list[int]], fila: int, col: int) -> int:
    """
    Cuenta cuántas celdas vecinas están vivas.
    
    Cada celda tiene hasta 8 vecinos: arriba, abajo, izquierda, derecha y las 4 diagonales.
    """
    
    # --- PASO 1: OBTENER DIMENSIONES DEL TABLERO ---
    
    # len(tablero) nos da el número de filas
    filas = len(tablero)
    # len(tablero[0]) nos da el número de columnas (asumiendo que todas las filas tienen el mismo tamaño)
    columnas = len(tablero[0])
    
    # --- PASO 2: DEFINIR LOS 8 DESPLAZAMIENTOS POSIBLES ---
    
    # Cada vecino se puede encontrar sumando un desplazamiento a (fila, col)
    # Por ejemplo, el vecino de arriba está en (fila-1, col)
    desplazamientos = [
        (-1, -1),  # Diagonal superior izquierda
        (-1,  0),  # Arriba
        (-1,  1),  # Diagonal superior derecha
        ( 0, -1),  # Izquierda
        ( 0,  1),  # Derecha
        ( 1, -1),  # Diagonal inferior izquierda
        ( 1,  0),  # Abajo
        ( 1,  1),  # Diagonal inferior derecha
    ]
    
    # --- PASO 3: CONTAR VECINOS VIVOS ---
    
    # Inicializamos el contador en cero
    vecinos_vivos = 0
    
    # Para cada desplazamiento posible
    for df, dc in desplazamientos:
        # Calculamos la posición del vecino
        fila_vecino = fila + df
        col_vecino = col + dc
        
        # Verificamos que el vecino esté dentro de los límites del tablero
        # - La fila del vecino debe estar entre 0 y (filas - 1)
        # - La columna del vecino debe estar entre 0 y (columnas - 1)
        if 0 <= fila_vecino < filas and 0 <= col_vecino < columnas:
            # Si el vecino está dentro de los límites, verificamos si está vivo
            if tablero[fila_vecino][col_vecino] == 1:
                # Si está vivo, incrementamos el contador
                vecinos_vivos += 1
    
    # Retornamos el número total de vecinos vivos
    return vecinos_vivos


def calcular_siguiente_generacion(tablero_actual: list[list[int]]) -> list[list[int]]:
    """
    Calcula el estado del tablero en la siguiente generación.
    
    Aplica las 4 reglas del Juego de la Vida de Conway a cada celda.
    """
    
    # --- PASO 1: OBTENER DIMENSIONES ---
    
    filas = len(tablero_actual)
    columnas = len(tablero_actual[0])
    
    # --- PASO 2: CREAR NUEVO TABLERO VACÍO ---
    
    # ⚠️ IMPORTANTE: NO modificamos tablero_actual directamente
    # Creamos un nuevo tablero completamente independiente
    nuevo_tablero = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(0)
        nuevo_tablero.append(fila)
    
    # --- PASO 3: CALCULAR EL ESTADO DE CADA CELDA ---
    
    # Recorremos cada celda del tablero actual
    for f in range(filas):
        for c in range(columnas):
            # Obtenemos el estado actual de esta celda
            estado_actual = tablero_actual[f][c]
            
            # Contamos cuántos vecinos vivos tiene
            vecinos = contar_vecinos(tablero_actual, f, c)
            
            # --- APLICAR LAS REGLAS DEL JUEGO DE LA VIDA ---
            
            # Caso 1: La celda está VIVA actualmente
            if estado_actual == 1:
                # Regla de supervivencia: con 2 o 3 vecinos, sobrevive
                if vecinos == 2 or vecinos == 3:
                    nuevo_tablero[f][c] = 1  # Sobrevive
                else:
                    # Con menos de 2 vecinos: muere por subpoblación
                    # Con más de 3 vecinos: muere por sobrepoblación
                    nuevo_tablero[f][c] = 0  # Muere
            
            # Caso 2: La celda está MUERTA actualmente
            else:
                # Regla de reproducción: con exactamente 3 vecinos, nace
                if vecinos == 3:
                    nuevo_tablero[f][c] = 1  # Nace
                else:
                    # Si no tiene exactamente 3 vecinos, sigue muerta
                    nuevo_tablero[f][c] = 0  # Sigue muerta
    
    # Retornamos el nuevo tablero con la siguiente generación
    return nuevo_tablero


# =============================================================================
# FUNCIÓN PRINCIPAL (YA IMPLEMENTADA COMO GUÍA)
# =============================================================================


def ejecutar_simulacion():
    """Ejecuta la simulación completa del Juego de la Vida."""
    
    # Paso 1: Crear el tablero inicial con el patrón
    print("🎮 Iniciando simulación del Juego de la Vida de Conway")
    print(f"📐 Dimensiones: {DIMENSIONES[0]} filas × {DIMENSIONES[1]} columnas")
    print(f"🔄 Generaciones: {GENERACIONES}")
    print(f"🧬 Patrón inicial: Glider (Planeador)\n")
    
    tablero = crear_tablero(DIMENSIONES, PATRON_INICIAL)
    
    # Paso 2: Simular cada generación
    for generacion in range(GENERACIONES):
        # Imprimir encabezado de la generación
        print(f"--- Generación {generacion} ---")
        
        # Mostrar el estado actual del tablero
        imprimir_tablero(tablero)
        
        # Calcular la siguiente generación
        tablero = calcular_siguiente_generacion(tablero)
        
        # Pequeña pausa para visualizar mejor (opcional)
        print()  # Línea en blanco entre generaciones
        time.sleep(0.5)  # Pausa de medio segundo
    
    print("✅ Simulación completada")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    ejecutar_simulacion()
