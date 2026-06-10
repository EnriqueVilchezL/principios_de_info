"""
Plantilla del Juego de la Vida de Conway para completar en clase.

Objetivo para el estudiantado:
- Rellenar las funciones marcadas con TODO para que la simulación funcione correctamente.
- Implementar un autómata celular que evoluciona según las reglas del Juego de la Vida.

Contexto:
El Juego de la Vida de Conway es un autómata celular que simula la evolución
de poblaciones de células vivas y muertas en una cuadrícula bidimensional.

🔧 Solo se permite importar el módulo «time» para pausas entre generaciones.
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
# FUNCIONES QUE EL ESTUDIANTADO DEBE IMPLEMENTAR
# =============================================================================


def crear_tablero(dimensiones: tuple[int, int], celdas_vivas: list[tuple[int, int]]) -> list[list[int]]:
    """TODO: Crear e inicializar el tablero del Juego de la Vida.

    Proceso:
    1. Extrae el número de filas y columnas de la tupla dimensiones
    2. Crea una lista de listas con todas las celdas inicializadas a 0 (muertas)
    3. Para cada coordenada en celdas_vivas:
       - Verifica que la coordenada esté dentro de los límites del tablero
       - Si es válida, cambia el valor de esa celda a 1 (viva)
       - Si está fuera de límites, ignórala y continúa

    Parámetros:
        dimensiones: Tupla con (filas, columnas) del tablero
                    Ej: (10, 20) significa 10 filas y 20 columnas
        celdas_vivas: Lista de tuplas con coordenadas (fila, columna) de celdas vivas
                     Ej: [(0, 1), (1, 2), (2, 0)] significa que las celdas en
                         posición (0,1), (1,2) y (2,0) están vivas

    Retorna:
        list[list[int]]: Tablero inicializado como lista de listas
                        Ej: [[0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [1, 0, 0, 0]]
                        donde 1 = celda viva, 0 = celda muerta

    Ejemplo de uso:
        tablero = crear_tablero((3, 4), [(0, 1), (1, 2), (2, 0)])
        # Crea un tablero de 3x4 con tres celdas vivas
    """
    raise NotImplementedError("Implementa crear_tablero")


def imprimir_tablero(tablero: list[list[int]]) -> None:
    """TODO: Imprimir una representación visual del tablero en la consola.

    Proceso:
    1. Recorre cada fila del tablero
    2. Para cada celda en la fila:
       - Si el valor es 1 (viva), imprime '■' (cuadrado lleno)
       - Si el valor es 0 (muerta), imprime '·' (punto medio)
    3. Agrega un espacio entre cada símbolo para mejor legibilidad
    4. Al final de cada fila, imprime un salto de línea

    Pistas:
    - Usa print() con el parámetro end=' ' para evitar saltos de línea automáticos
    - Usa print() sin parámetros al final de cada fila para el salto de línea

    Parámetros:
        tablero: Lista de listas representando el estado actual
                Ej: [[0, 1, 0],
                     [1, 1, 0],
                     [0, 0, 1]]

    Retorna:
        None: Solo imprime en consola (no retorna ningún valor)

    Ejemplo de salida esperada:
        · ■ ·
        ■ ■ ·
        · · ■
    """
    raise NotImplementedError("Implementa imprimir_tablero")


def contar_vecinos(tablero: list[list[int]], fila: int, col: int) -> int:
    """TODO: Contar cuántas celdas vecinas están vivas.

    Una celda tiene 8 vecinos posibles (arriba, abajo, izquierda, derecha y las 4 diagonales).
    Este algoritmo debe verificar cada posición vecina y contar solo las que están vivas.

    Proceso:
    1. Obtén las dimensiones del tablero (número de filas y columnas)
    2. Inicializa un contador en 0
    3. Define los 8 desplazamientos de vecinos:
       - Arriba: (-1, 0), Abajo: (1, 0)
       - Izquierda: (0, -1), Derecha: (0, 1)
       - Diagonal superior izquierda: (-1, -1), Diagonal superior derecha: (-1, 1)
       - Diagonal inferior izquierda: (1, -1), Diagonal inferior derecha: (1, 1)
    4. Para cada desplazamiento:
       - Calcula la posición del vecino: (fila + df, col + dc)
       - Verifica que esté dentro de los límites del tablero
       - Si está dentro y el valor es 1, incrementa el contador
    5. Retorna el contador

    Parámetros:
        tablero: Lista de listas con el estado actual
                Ej: [[0, 1, 0],
                     [1, 1, 1],
                     [0, 0, 0]]
        fila: Índice de la fila de la celda (0-indexed)
             Ej: 1
        col: Índice de la columna de la celda (0-indexed)
            Ej: 1

    Retorna:
        int: Número de vecinos vivos (0 a 8)
             Ej: 3 (si la celda en (1,1) tiene tres vecinos vivos)

    Ejemplo de uso:
        tablero = [[0, 1, 0],
                   [1, 1, 1],
                   [0, 0, 0]]
        vecinos = contar_vecinos(tablero, 1, 1)  # → 3
        # La celda central (1,1) tiene 3 vecinos vivos: (0,1), (1,0), (1,2)
    """
    raise NotImplementedError("Implementa contar_vecinos")


def calcular_siguiente_generacion(tablero_actual: list[list[int]]) -> list[list[int]]:
    """TODO: Calcular el estado del tablero en la siguiente generación.

    ⚠️ IMPORTANTE: NO modifiques tablero_actual directamente. Crea un nuevo tablero.

    Reglas del Juego de la Vida:
    1. Una celda VIVA con < 2 vecinos vivos MUERE (subpoblación)
    2. Una celda VIVA con 2 o 3 vecinos vivos SOBREVIVE
    3. Una celda VIVA con > 3 vecinos vivos MUERE (sobrepoblación)
    4. Una celda MUERTA con exactamente 3 vecinos vivos NACE (reproducción)

    Proceso:
    1. Crea un nuevo tablero del mismo tamaño, inicializado todo a 0
    2. Para cada celda (f, c) en tablero_actual:
       - Cuenta sus vecinos vivos usando contar_vecinos()
       - Aplica las reglas para determinar el nuevo estado:
         * Si la celda actual está VIVA (valor = 1):
           - Si tiene 2 o 3 vecinos → nueva celda = 1 (sobrevive)
           - Si tiene < 2 o > 3 vecinos → nueva celda = 0 (muere)
         * Si la celda actual está MUERTA (valor = 0):
           - Si tiene exactamente 3 vecinos → nueva celda = 1 (nace)
           - Si no → nueva celda = 0 (sigue muerta)
       - Asigna el nuevo estado a la celda (f, c) en el nuevo tablero
    3. Retorna el nuevo tablero

    Parámetros:
        tablero_actual: Lista de listas con el estado de la generación actual
                       Ej: [[0, 1, 0],
                            [1, 1, 1],
                            [0, 0, 0]]

    Retorna:
        list[list[int]]: Nuevo tablero con el estado de la siguiente generación
                        Ej: [[1, 1, 1],
                             [1, 0, 1],
                             [0, 1, 0]]

    Ejemplo de transición:
        Generación 0:          Generación 1:
        · ■ ·                  ■ ■ ■
        ■ ■ ■        →         ■ · ■
        · · ·                  · ■ ·
    """
    raise NotImplementedError("Implementa calcular_siguiente_generacion")


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
    
    try:
        ejecutar_simulacion()
    except NotImplementedError as e:
        print("⚠️  Esta es solo una plantilla. Completa las funciones antes de ejecutar.")
        print("📝 Funciones por implementar:")
        print("   1. crear_tablero()")
        print("   2. imprimir_tablero()")
        print("   3. contar_vecinos()")
        print("   4. calcular_siguiente_generacion()")
        print("\n💡 Cuando todas las funciones estén implementadas, el juego ejecutará automáticamente.")
        print()
        print(f"🚫 Error: {e}")
        print("   Complete las funciones marcadas con TODO para ejecutar la simulación.")
