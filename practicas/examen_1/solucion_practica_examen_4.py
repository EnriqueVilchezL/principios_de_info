"""
Solución del Sistema de Monitoreo de Fauna para el SINAC

Este archivo contiene la implementación completa de todas las funciones
del sistema de monitoreo de fauna.

Autor: Sistema de Monitoreo SINAC
Fecha: Octubre 2025
"""

import math


# =============================================================================
# DATOS DE REFERENCIA GEOGRÁFICA
# =============================================================================

coordenadas_parques_ejemplo = {
    'Parque Nacional Corcovado': (8.55, -83.60),
    'Parque Nacional Manuel Antonio': (9.40, -84.15),
    'Parque Nacional Tortuguero': (10.53, -83.50)
}

radio_valido_km_ejemplo = 40.0


# =============================================================================
# DATOS DE CAMPO DE EJEMPLO
# =============================================================================

avistamientos_brutos_ejemplo = [
    {
        'id_reporte': 'RPT001',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Panthera onca',
        'cantidad': 2,
        'coordenadas': (8.47, -83.59),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'En Peligro'
    },
    {
        'id_reporte': 'RPT002',
        'parque': 'Parque Nacional Manuel Antonio ',
        'especie': 'Iguana iguana',
        'cantidad': '45',
        'coordenadas': (9.39, -84.14),
        'guardaparque': 'GP-07',
        'estado_conservacion': 'Preocupación Menor'
    },
    {
        'id_reporte': 'RPT003',
        'parque': ' Parque Nacional Corcovado ',
        'especie': 'Tapirus bairdii',
        'cantidad': 12,
        'coordenadas': (9.52, -83.68),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'En Peligro'
    },
    {
        'id_reporte': 'RPT004',
        'parque': 'Parque Nacional Tortuguero',
        'especie': 'Chelonia mydas',
        'cantidad': 150,
        'coordenadas': (10.53, -83.50),
        'guardaparque': 'GP-11',
        'estado_conservacion': 'Vulnerable'
    },
    {
        'id_reporte': 'RPT005',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Panthera onca',
        'cantidad': '3',
        'coordenadas': (8.49, -83.61),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'En Peligro'
    },
    {
        'id_reporte': 'RPT006',
        'parque': 'Parque Nacional Manuel Antonio',
        'especie': 'Saimiri oerstedii',
        'cantidad': 30,
        'coordenadas': (9.40, -84.15),
        'guardaparque': 'GP-07',
        'estado_conservacion': 'Vulnerable'
    },
    {
        'id_reporte': 'RPT007',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Puma concolor',
        'cantidad': 'no_valido',
        'coordenadas': (8.50, -83.60),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'Preocupación Menor'
    },
    {
        'id_reporte': 'RPT008',
        'parque': 'Parque Nacional Chirripó',
        'especie': 'Sylvilagus dicei',
        'cantidad': 10,
        'coordenadas': (9.48, -83.48),
        'guardaparque': 'GP-15',
        'estado_conservacion': 'En Peligro'
    },
]


# =============================================================================
# FUNCIONES IMPLEMENTADAS
# =============================================================================


def calcular_distancia(coords1: tuple[float, float], coords2: tuple[float, float]) -> float:
    """Calcular la distancia entre dos puntos geográficos usando la aproximación Equirectangular.
    
    Parámetros:
        coords1: Tupla (latitud, longitud) del primer punto
        coords2: Tupla (latitud, longitud) del segundo punto
    
    Retorna:
        float: Distancia en kilómetros
    """
    # Radio de la Tierra en kilómetros
    R = 6371.0
    
    # Desempaquetar coordenadas
    lat1, lon1 = coords1
    lat2, lon2 = coords2
    
    # Convertir de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Calcular componentes x e y
    x = (lon2_rad - lon1_rad) * math.cos((lat1_rad + lat2_rad) / 2)
    y = lat2_rad - lat1_rad
    
    # Calcular distancia
    distancia = math.sqrt(x**2 + y**2) * R
    
    return distancia


def validar_y_limpiar_datos(
    avistamientos_brutos: list[dict],
    coords_parques: dict,
    radio_maximo: float
) -> list[dict]:
    """Validar y limpiar los datos de avistamientos.
    
    Parámetros:
        avistamientos_brutos: Lista de diccionarios con datos sin procesar
        coords_parques: Diccionario {nombre_parque: (lat, lon)}
        radio_maximo: Radio de validez en kilómetros
    
    Retorna:
        list: Lista de avistamientos válidos y limpios
    """
    avistamientos_validos = []
    
    for avistamiento in avistamientos_brutos:
        # 1. Validación de Cantidad
        try:
            cantidad = int(avistamiento['cantidad'])
            if cantidad <= 0:
                continue  # Descartar si es <= 0
        except (ValueError, TypeError):
            continue  # Descartar si no se puede convertir a entero
        
        # 2. Validación Geográfica
        # Limpiar el nombre del parque para la búsqueda
        parque_limpio = avistamiento['parque'].strip()
        
        # Verificar que el parque existe
        if parque_limpio not in coords_parques:
            continue  # Descartar si el parque no existe
        
        # Calcular distancia desde el centro del parque
        coords_parque = coords_parques[parque_limpio]
        coords_avistamiento = avistamiento['coordenadas']
        distancia = calcular_distancia(coords_parque, coords_avistamiento)
        
        if distancia > radio_maximo:
            continue  # Descartar si está fuera del radio
        
        # 3. Limpieza de Datos
        # Crear una copia limpia del avistamiento
        avistamiento_limpio = avistamiento.copy()
        avistamiento_limpio['parque'] = parque_limpio
        avistamiento_limpio['especie'] = avistamiento['especie'].strip()
        avistamiento_limpio['cantidad'] = cantidad
        
        avistamientos_validos.append(avistamiento_limpio)
    
    return avistamientos_validos


def generar_reporte_por_parque(avistamientos_validos: list) -> dict:
    """Generar reporte de individuos por especie en cada parque.
    
    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
    
    Retorna:
        dict: {nombre_parque: {nombre_especie: total_individuos}}
    """
    reporte = {}
    
    for avistamiento in avistamientos_validos:
        parque = avistamiento['parque']
        especie = avistamiento['especie']
        cantidad = avistamiento['cantidad']
        
        # Si el parque no existe en el reporte, crear un diccionario vacío
        if parque not in reporte:
            reporte[parque] = {}
        
        # Si la especie no existe en ese parque, inicializar en 0
        if especie not in reporte[parque]:
            reporte[parque][especie] = 0
        
        # Sumar la cantidad de individuos
        reporte[parque][especie] += cantidad
    
    return reporte


def obtener_especies_unicas_en_riesgo(avistamientos_validos: list) -> set:
    """Identificar especies en riesgo de conservación.
    
    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
    
    Retorna:
        set: Conjunto con nombres de especies en riesgo
    """
    especies_riesgo = set()
    
    for avistamiento in avistamientos_validos:
        estado = avistamiento['estado_conservacion']
        
        # Verificar si está en peligro o vulnerable
        if estado in ['En Peligro', 'Vulnerable']:
            especies_riesgo.add(avistamiento['especie'])
    
    return especies_riesgo


def analizar_contribuciones_guardaparques(avistamientos_validos: list) -> dict:
    """Contar reportes válidos por guardaparque.
    
    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
    
    Retorna:
        dict: {codigo_guardaparque: numero_de_reportes}
    """
    contribuciones = {}
    
    for avistamiento in avistamientos_validos:
        guardaparque = avistamiento['guardaparque']
        
        # Si el guardaparque no está en el diccionario, inicializar en 0
        if guardaparque not in contribuciones:
            contribuciones[guardaparque] = 0
        
        # Incrementar el contador
        contribuciones[guardaparque] += 1
    
    return contribuciones


def encontrar_avistamiento_norte(
    avistamientos_validos: list,
    especie_objetivo: str
) -> str | None:
    """Encontrar el avistamiento más al norte de una especie.
    
    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
        especie_objetivo: Nombre de la especie de interés
    
    Retorna:
        str | None: ID del reporte más al norte, o None si no hay avistamientos
    """
    # Filtrar avistamientos de la especie objetivo
    avistamientos_especie = [
        av for av in avistamientos_validos 
        if av['especie'] == especie_objetivo
    ]
    
    # Si no hay avistamientos de la especie, retornar None
    if not avistamientos_especie:
        return None
    
    # Encontrar el avistamiento con la latitud más alta
    # La latitud es el primer elemento de la tupla 'coordenadas'
    avistamiento_norte = max(
        avistamientos_especie,
        key=lambda av: av['coordenadas'][0]
    )
    
    return avistamiento_norte['id_reporte']


def imprimir_informe_final(
    reporte_parques: dict,
    especies_riesgo: set,
    contribuciones_guardaparques: dict,
    reporte_clave: str | None
) -> None:
    """Imprimir el informe completo formateado.
    
    Parámetros:
        reporte_parques: Diccionario de parques y especies
        especies_riesgo: Conjunto de especies en riesgo
        contribuciones_guardaparques: Diccionario de guardaparques
        reporte_clave: ID del reporte clave (o None)
    
    Retorna:
        None: Solo imprime en consola
    """
    print("=" * 60)
    print("*** INFORME DE MONITOREO DE FAUNA - SINAC ***")
    print("=" * 60)
    
    # Sección 1: Reporte de Avistamientos por Parque Nacional
    print("\n--- Reporte de Avistamientos por Parque Nacional ---\n")
    
    for parque, especies in reporte_parques.items():
        print(f"> {parque}:")
        for especie, cantidad in especies.items():
            print(f"  - {especie}: {cantidad} individuos")
        print()
    
    # Sección 2: Alerta de Especies en Riesgo
    print("--- Alerta de Especies en Riesgo ---\n")
    print("Las siguientes especies requieren atención especial:")
    
    for especie in sorted(especies_riesgo):
        print(f"* {especie}")
    
    # Sección 3: Contribuciones por Guardaparque
    print("\n--- Contribuciones por Guardaparque ---\n")
    print("> Reportes válidos por guardaparque:")
    
    for guardaparque, cantidad in sorted(contribuciones_guardaparques.items()):
        print(f"  - {guardaparque}: {cantidad} reportes")
    
    # Sección 4: Punto de Interés Geográfico
    print("\n--- Punto de Interés Geográfico ---\n")
    
    if reporte_clave:
        print(f"> Avistamiento más al norte de 'Panthera onca':")
        print(f"  - ID del Reporte: {reporte_clave}")
    else:
        print("> No se encontraron avistamientos de la especie objetivo")
    
    print("\n" + "=" * 60)
    print("*** Fin del Informe ***")
    print("=" * 60)


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================


def ejecutar_sistema():
    """Ejecuta el flujo completo del sistema de monitoreo."""
    
    # Paso 1: Validar y limpiar datos
    print("🔍 Procesando datos de avistamientos...")
    avistamientos_validos = validar_y_limpiar_datos(
        avistamientos_brutos_ejemplo,
        coordenadas_parques_ejemplo,
        radio_valido_km_ejemplo
    )
    print(f"✅ {len(avistamientos_validos)} reportes válidos de {len(avistamientos_brutos_ejemplo)} totales\n")
    
    # Paso 2: Generar reporte por parque
    reporte_parques = generar_reporte_por_parque(avistamientos_validos)
    
    # Paso 3: Identificar especies en riesgo
    especies_riesgo = obtener_especies_unicas_en_riesgo(avistamientos_validos)
    
    # Paso 4: Analizar contribuciones de guardaparques
    contribuciones = analizar_contribuciones_guardaparques(avistamientos_validos)
    
    # Paso 5: Encontrar avistamiento más al norte de especie clave
    especie_clave = 'Panthera onca'
    reporte_norte = encontrar_avistamiento_norte(avistamientos_validos, especie_clave)
    
    # Paso 6: Imprimir informe final
    imprimir_informe_final(
        reporte_parques,
        especies_riesgo,
        contribuciones,
        reporte_norte
    )


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    ejecutar_sistema()
