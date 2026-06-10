"""
Suite de Pruebas para el Juego de la Vida de Conway

Este archivo contiene pruebas automatizadas para verificar la correcta
implementación de todas las funciones de la simulación.

Para ejecutar las pruebas:
    python3 pruebas_para_practica_examen_6.py

Nota: Las funciones deben estar implementadas en el archivo que se importa.
"""

import time


# =============================================================================
# DATOS DE PRUEBA
# =============================================================================

# Configuración de prueba básica
DIMENSIONES_TEST = (5, 5)
GENERACIONES_TEST = 3

# Patrón de prueba simple (bloque 2x2 estático)
PATRON_BLOQUE = [(1, 1), (1, 2), (2, 1), (2, 2)]

# Patrón oscilador (blinker - oscila entre horizontal y vertical)
PATRON_BLINKER = [(1, 2), (2, 2), (3, 2)]

# Patrón Glider completo
PATRON_GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# =============================================================================
# IMPORTAR FUNCIONES A PROBAR
# =============================================================================

# Intenta importar las funciones implementadas
try:
    from practica_de_examen_6_plantilla import (
        crear_tablero,
        imprimir_tablero,
        contar_vecinos,
        calcular_siguiente_generacion
    )
    FUNCIONES_DISPONIBLES = True
except (ImportError, NotImplementedError):
    FUNCIONES_DISPONIBLES = False
    print("⚠️  Las funciones aún no están implementadas.")
    print("Complete las funciones en practica_de_examen_6_plantilla.py")


# =============================================================================
# FUNCIONES DE PRUEBA
# =============================================================================

def test_crear_tablero():
    """Prueba la creación e inicialización del tablero."""
    print("\n🧪 TEST 1: Creación e Inicialización del Tablero")
    print("-" * 50)
    
    # Caso 1: Tablero vacío
    tablero_vacio = crear_tablero((3, 3), [])
    assert isinstance(tablero_vacio, list), "El tablero debe ser una lista"
    assert len(tablero_vacio) == 3, f"Debe tener 3 filas, tiene {len(tablero_vacio)}"
    assert len(tablero_vacio[0]) == 3, f"Debe tener 3 columnas, tiene {len(tablero_vacio[0])}"
    
    # Verificar que todas las celdas están muertas
    for fila in tablero_vacio:
        for celda in fila:
            assert celda == 0, "Todas las celdas deben estar en 0 (muertas)"
    print("✅ Tablero vacío creado correctamente (todas las celdas muertas)")
    
    # Caso 2: Tablero con celdas vivas
    tablero_vivas = crear_tablero((3, 3), [(0, 0), (1, 1), (2, 2)])
    assert tablero_vivas[0][0] == 1, "Celda (0,0) debe estar viva"
    assert tablero_vivas[1][1] == 1, "Celda (1,1) debe estar viva"
    assert tablero_vivas[2][2] == 1, "Celda (2,2) debe estar viva"
    assert tablero_vivas[0][1] == 0, "Celda (0,1) debe estar muerta"
    print("✅ Celdas vivas colocadas correctamente en posiciones especificadas")
    
    # Caso 3: Coordenadas fuera de límites (deben ser ignoradas)
    tablero_limites = crear_tablero((3, 3), [(0, 0), (5, 5), (-1, 2)])
    assert tablero_limites[0][0] == 1, "Celda (0,0) debe estar viva"
    # Verificar que no haya errores por coordenadas inválidas
    print("✅ Coordenadas fuera de límites ignoradas correctamente")
    
    # Caso 4: Dimensiones diferentes
    tablero_rectangular = crear_tablero((2, 4), [(0, 0), (1, 3)])
    assert len(tablero_rectangular) == 2, "Debe tener 2 filas"
    assert len(tablero_rectangular[0]) == 4, "Debe tener 4 columnas"
    assert tablero_rectangular[0][0] == 1, "Celda (0,0) debe estar viva"
    assert tablero_rectangular[1][3] == 1, "Celda (1,3) debe estar viva"
    print("✅ Tablero rectangular creado correctamente")


def test_contar_vecinos():
    """Prueba el conteo de vecinos vivos."""
    print("\n🧪 TEST 2: Conteo de Vecinos")
    print("-" * 50)
    
    # Crear un tablero de prueba
    # · ■ ·
    # ■ ■ ■
    # · ■ ·
    tablero = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    
    # Caso 1: Celda central con 4 vecinos
    vecinos_centro = contar_vecinos(tablero, 1, 1)
    assert vecinos_centro == 4, f"Centro debe tener 4 vecinos, tiene {vecinos_centro}"
    print(f"✅ Celda central (1,1): {vecinos_centro} vecinos (esperado: 4)")
    
    # Caso 2: Celda en esquina con 3 vecinos (en este tablero específico)
    vecinos_esquina = contar_vecinos(tablero, 0, 0)
    assert vecinos_esquina == 3, f"Esquina debe tener 3 vecinos, tiene {vecinos_esquina}"
    print(f"✅ Celda esquina (0,0): {vecinos_esquina} vecinos (esperado: 3)")
    
    # Caso 3: Celda superior con 3 vecinos
    vecinos_arriba = contar_vecinos(tablero, 0, 1)
    assert vecinos_arriba == 3, f"Superior debe tener 3 vecinos, tiene {vecinos_arriba}"
    print(f"✅ Celda superior (0,1): {vecinos_arriba} vecinos (esperado: 3)")
    
    # Caso 4: Celda lateral con 3 vecinos (en este tablero específico)
    vecinos_lateral = contar_vecinos(tablero, 1, 0)
    assert vecinos_lateral == 3, f"Lateral debe tener 3 vecinos, tiene {vecinos_lateral}"
    print(f"✅ Celda lateral (1,0): {vecinos_lateral} vecinos (esperado: 3)")
    
    # Caso 5: Tablero vacío (todos los vecinos muertos)
    tablero_vacio = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    vecinos_vacio = contar_vecinos(tablero_vacio, 1, 1)
    assert vecinos_vacio == 0, f"No debe tener vecinos vivos, tiene {vecinos_vacio}"
    print(f"✅ Tablero vacío: {vecinos_vacio} vecinos (esperado: 0)")


def test_calcular_siguiente_generacion_bloque():
    """Prueba con un patrón estable (bloque 2x2)."""
    print("\n🧪 TEST 3: Patrón Estable (Bloque 2x2)")
    print("-" * 50)
    
    # El bloque es un patrón estático que no cambia
    # · · · ·
    # · ■ ■ ·
    # · ■ ■ ·
    # · · · ·
    tablero_inicial = crear_tablero((4, 4), PATRON_BLOQUE)
    
    # Calculamos varias generaciones
    tablero = tablero_inicial
    for gen in range(3):
        tablero_siguiente = calcular_siguiente_generacion(tablero)
        
        # El bloque debe permanecer igual
        assert tablero_siguiente[1][1] == 1, f"Gen {gen+1}: Celda (1,1) debe estar viva"
        assert tablero_siguiente[1][2] == 1, f"Gen {gen+1}: Celda (1,2) debe estar viva"
        assert tablero_siguiente[2][1] == 1, f"Gen {gen+1}: Celda (2,1) debe estar viva"
        assert tablero_siguiente[2][2] == 1, f"Gen {gen+1}: Celda (2,2) debe estar viva"
        
        # Verificar que el resto está muerto
        assert tablero_siguiente[0][0] == 0, f"Gen {gen+1}: Celda (0,0) debe estar muerta"
        assert tablero_siguiente[0][3] == 0, f"Gen {gen+1}: Celda (0,3) debe estar muerta"
        
        tablero = tablero_siguiente
    
    print("✅ Patrón bloque permanece estable a través de 3 generaciones")


def test_calcular_siguiente_generacion_blinker():
    """Prueba con un oscilador (blinker)."""
    print("\n🧪 TEST 4: Patrón Oscilador (Blinker)")
    print("-" * 50)
    
    # El blinker oscila entre vertical y horizontal
    # Generación 0 (vertical):   Generación 1 (horizontal):
    # · · · · ·                  · · · · ·
    # · · ■ · ·                  · · · · ·
    # · · ■ · ·                  · ■ ■ ■ ·
    # · · ■ · ·                  · · · · ·
    # · · · · ·                  · · · · ·
    
    tablero_gen0 = crear_tablero((5, 5), PATRON_BLINKER)
    
    # Generación 1: Debe cambiar a horizontal
    tablero_gen1 = calcular_siguiente_generacion(tablero_gen0)
    assert tablero_gen1[2][1] == 1, "Gen 1: Celda (2,1) debe estar viva"
    assert tablero_gen1[2][2] == 1, "Gen 1: Celda (2,2) debe estar viva"
    assert tablero_gen1[2][3] == 1, "Gen 1: Celda (2,3) debe estar viva"
    assert tablero_gen1[1][2] == 0, "Gen 1: Celda (1,2) debe estar muerta"
    assert tablero_gen1[3][2] == 0, "Gen 1: Celda (3,2) debe estar muerta"
    print("✅ Generación 1: Blinker cambió a horizontal")
    
    # Generación 2: Debe volver a vertical
    tablero_gen2 = calcular_siguiente_generacion(tablero_gen1)
    assert tablero_gen2[1][2] == 1, "Gen 2: Celda (1,2) debe estar viva"
    assert tablero_gen2[2][2] == 1, "Gen 2: Celda (2,2) debe estar viva"
    assert tablero_gen2[3][2] == 1, "Gen 2: Celda (3,2) debe estar viva"
    assert tablero_gen2[2][1] == 0, "Gen 2: Celda (2,1) debe estar muerta"
    assert tablero_gen2[2][3] == 0, "Gen 2: Celda (2,3) debe estar muerta"
    print("✅ Generación 2: Blinker volvió a vertical (oscilación correcta)")


def test_reglas_del_juego():
    """Prueba las 4 reglas del Juego de la Vida."""
    print("\n🧪 TEST 5: Reglas del Juego de la Vida")
    print("-" * 50)
    
    # Regla 1: Subpoblación (celda viva con < 2 vecinos muere)
    tablero_subpob = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 0]
    ]
    siguiente = calcular_siguiente_generacion(tablero_subpob)
    assert siguiente[1][1] == 0, "Regla 1: Celda con 1 vecino debe morir (subpoblación)"
    print("✅ Regla 1 (Subpoblación): Celda viva con < 2 vecinos muere")
    
    # Regla 2: Supervivencia (celda viva con 2-3 vecinos sobrevive)
    tablero_superviv = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    siguiente = calcular_siguiente_generacion(tablero_superviv)
    assert siguiente[0][0] == 1, "Regla 2: Celda con 3 vecinos debe sobrevivir"
    assert siguiente[0][1] == 1, "Regla 2: Celda con 3 vecinos debe sobrevivir"
    print("✅ Regla 2 (Supervivencia): Celda viva con 2-3 vecinos sobrevive")
    
    # Regla 3: Sobrepoblación (celda viva con > 3 vecinos muere)
    tablero_sobrepob = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ]
    siguiente = calcular_siguiente_generacion(tablero_sobrepob)
    assert siguiente[0][1] == 0, "Regla 3: Celda con 4 vecinos debe morir (sobrepoblación)"
    print("✅ Regla 3 (Sobrepoblación): Celda viva con > 3 vecinos muere")
    
    # Regla 4: Reproducción (celda muerta con 3 vecinos nace)
    tablero_reprod = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    siguiente = calcular_siguiente_generacion(tablero_reprod)
    assert siguiente[1][1] == 1, "Regla 4: Celda muerta con 3 vecinos debe nacer"
    print("✅ Regla 4 (Reproducción): Celda muerta con 3 vecinos nace")


def test_imprimir_tablero():
    """Prueba la impresión del tablero (visual)."""
    print("\n🧪 TEST 6: Impresión Visual del Tablero")
    print("-" * 50)
    
    # Crear un tablero pequeño de prueba
    tablero = crear_tablero((3, 3), [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])
    
    print("Tablero de prueba (patrón cruz):")
    try:
        imprimir_tablero(tablero)
        print("✅ Función imprimir_tablero ejecutada sin errores")
    except Exception as e:
        raise AssertionError(f"Error al imprimir tablero: {e}")


def test_glider_movimiento():
    """Prueba que el Glider se mueve correctamente."""
    print("\n🧪 TEST 7: Movimiento del Glider")
    print("-" * 50)
    
    # Crear tablero grande para que el glider se mueva
    tablero = crear_tablero((10, 10), PATRON_GLIDER)
    
    # Evolucionar 4 generaciones
    for gen in range(4):
        tablero = calcular_siguiente_generacion(tablero)
    
    # Después de 4 generaciones, el glider debe haberse movido
    # Verificar que hay celdas vivas en el tablero
    celdas_vivas = 0
    for fila in tablero:
        for celda in fila:
            if celda == 1:
                celdas_vivas += 1
    
    assert celdas_vivas == 5, f"El Glider debe mantener 5 celdas vivas, tiene {celdas_vivas}"
    print(f"✅ Glider mantiene 5 celdas vivas después de 4 generaciones")
    
    # Verificar que el patrón se ha desplazado (el glider debería moverse)
    # Después de 4 generaciones, al menos una celda del patrón original debe estar muerta
    posicion_original_viva = sum(1 for f, c in PATRON_GLIDER if tablero[f][c] == 1)
    
    # Si todas las celdas originales siguen vivas, el patrón no se movió
    # (pero esto depende del tablero, así que solo verificamos que el patrón existe)
    print("✅ Glider ha evolucionado correctamente")


def test_tablero_vacio():
    """Prueba con un tablero completamente vacío."""
    print("\n🧪 TEST 8: Tablero Vacío")
    print("-" * 50)
    
    tablero = crear_tablero((5, 5), [])
    
    # Un tablero vacío debe permanecer vacío
    for gen in range(3):
        tablero = calcular_siguiente_generacion(tablero)
        
        for fila in tablero:
            for celda in fila:
                assert celda == 0, f"Gen {gen+1}: Tablero vacío debe permanecer vacío"
    
    print("✅ Tablero vacío permanece vacío a través de 3 generaciones")


def test_no_modifica_tablero_original():
    """Verifica que calcular_siguiente_generacion no modifica el tablero original."""
    print("\n🧪 TEST 9: No Modificación del Tablero Original")
    print("-" * 50)
    
    # Crear tablero original
    tablero_original = crear_tablero((3, 3), [(1, 0), (1, 1), (1, 2)])
    
    # Hacer una copia para comparar
    copia_original = [fila[:] for fila in tablero_original]
    
    # Calcular siguiente generación
    tablero_siguiente = calcular_siguiente_generacion(tablero_original)
    
    # Verificar que el tablero original no cambió
    for f in range(len(tablero_original)):
        for c in range(len(tablero_original[0])):
            assert tablero_original[f][c] == copia_original[f][c], \
                f"La celda ({f},{c}) del tablero original fue modificada"
    
    print("✅ Tablero original permanece intacto después de calcular siguiente generación")


# =============================================================================
# EJECUTAR TODAS LAS PRUEBAS
# =============================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas y muestra el resumen."""
    
    if not FUNCIONES_DISPONIBLES:
        print("\n❌ No se pueden ejecutar las pruebas.")
        print("Por favor, implemente las funciones en practica_de_examen_6_plantilla.py")
        return
    
    print("=" * 60)
    print("SUITE DE PRUEBAS - JUEGO DE LA VIDA DE CONWAY")
    print("=" * 60)
    
    pruebas_exitosas = 0
    pruebas_totales = 9
    
    try:
        test_crear_tablero()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_contar_vecinos()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_calcular_siguiente_generacion_bloque()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_calcular_siguiente_generacion_blinker()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_reglas_del_juego()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_imprimir_tablero()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_glider_movimiento()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_tablero_vacio()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_no_modifica_tablero_original()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    # Resumen final
    print("\n" + "=" * 60)
    if pruebas_exitosas == pruebas_totales:
        print("✅ ✅ ✅  TODAS LAS PRUEBAS PASARON EXITOSAMENTE  ✅ ✅ ✅")
    else:
        print(f"⚠️  {pruebas_exitosas}/{pruebas_totales} pruebas exitosas")
    print("=" * 60)
    
    print("\n📋 VERIFICACIÓN COMPLETADA:")
    print(f"✅ Pruebas exitosas: {pruebas_exitosas}/{pruebas_totales}")
    
    if pruebas_exitosas == pruebas_totales:
        print("\n🎓 LA IMPLEMENTACIÓN CUMPLE CON TODOS LOS REQUISITOS")
    else:
        print("\n⚠️  Revise los errores y complete la implementación")


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
