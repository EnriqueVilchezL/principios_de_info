"""
Plantilla del Sistema de Monitoreo de Fauna para el SINAC para completar en clase.

Objetivo para el estudiantado:
- Rellenar las funciones marcadas con TODO para que el sistema funcione correctamente.
- Procesar reportes de avistamientos, validar datos y generar informes estadísticos.

Contexto:
El Sistema Nacional de Áreas de Conservación (SINAC) necesita procesar datos de
avistamientos de fauna recolectados por guardaparques en Parques Nacionales.

🔧 Solo se permite importar el módulo «math» según la consigna original.
"""

import math


# =============================================================================
# DATOS DE REFERENCIA GEOGRÁFICA (YA PROPORCIONADOS)
# =============================================================================

# Coordenadas centrales de cada Parque Nacional (latitud, longitud)
coordenadas_parques_ejemplo = {
    'Parque Nacional Corcovado': (8.55, -83.60),
    'Parque Nacional Manuel Antonio': (9.40, -84.15),
    'Parque Nacional Tortuguero': (10.53, -83.50)
}

# Radio máximo de validez en kilómetros
radio_valido_km_ejemplo = 40.0


# =============================================================================
# DATOS DE CAMPO DE EJEMPLO (YA PROPORCIONADOS)
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
    # Este reporte está geográficamente fuera del radio de Corcovado
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
    # Este reporte tiene una cantidad inválida
    {
        'id_reporte': 'RPT007',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Puma concolor',
        'cantidad': 'no_valido',
        'coordenadas': (8.50, -83.60),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'Preocupación Menor'
    },
    # Este reporte corresponde a un parque no registrado
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
# FUNCIONES QUE EL ESTUDIANTADO DEBE IMPLEMENTAR
# =============================================================================


def calcular_distancia(coords1: tuple[float, float], coords2: tuple[float, float]) -> float:
    """TODO: Calcular la distancia entre dos puntos geográficos.

    Usa la aproximación Equirectangular:
    1. Convierte latitudes y longitudes de grados a radianes usando math.radians().
    2. Calcula x = (lon2_rad - lon1_rad) * cos((lat1_rad + lat2_rad) / 2)
    3. Calcula y = (lat2_rad - lat1_rad)
    4. La distancia es: d = sqrt(x² + y²) * R, donde R = 6371 km (radio de la Tierra)

    Parámetros:
        coords1: Tupla (latitud, longitud) del primer punto
                 Ej: (8.55, -83.60)
        coords2: Tupla (latitud, longitud) del segundo punto
                 Ej: (8.47, -83.59)

    Retorna:
        float: Distancia en kilómetros
               Ej: 8.9

    Ejemplo de uso:
        coords1 = (8.55, -83.60)  # Centro de Parque Corcovado
        coords2 = (8.47, -83.59)  # Avistamiento RPT001
        distancia = calcular_distancia(coords1, coords2)  # → 8.9 km
    """
    raise NotImplementedError("Implementa calcular_distancia")


def validar_y_limpiar_datos(
    avistamientos_brutos: list[dict],
    coords_parques: dict,
    radio_maximo: float
) -> list[dict]:
    """TODO: Validar y limpiar los datos de avistamientos.

    Proceso de validación (en orden):
    1. Validación de Cantidad:
       - Intenta convertir 'cantidad' a entero positivo
       - Si falla o es <= 0, descarta el avistamiento
       - Usa try-except para manejar errores de conversión

    2. Validación Geográfica:
       - Verifica que el parque exista en coords_parques
       - Calcula distancia entre coordenadas del avistamiento y centro del parque
       - Si distancia > radio_maximo, descarta el avistamiento

    3. Limpieza de Datos:
       - Aplica .strip() a los nombres de parques
       - Aplica .strip() a los nombres de especies
       - Convierte 'cantidad' a entero si aún es cadena

    Parámetros:
        avistamientos_brutos: Lista de diccionarios con datos sin procesar
                              Ej: [{'id_reporte': 'RPT001', 'parque': 'Parque Nacional Corcovado',
                                    'especie': 'Panthera onca', 'cantidad': 2,
                                    'coordenadas': (8.47, -83.59), 'guardaparque': 'GP-04',
                                    'estado_conservacion': 'En Peligro'}, ...]
        coords_parques: Diccionario {nombre_parque: (lat, lon)}
                        Ej: {'Parque Nacional Corcovado': (8.55, -83.60),
                             'Parque Nacional Manuel Antonio': (9.40, -84.15)}
        radio_maximo: Radio de validez en kilómetros
                      Ej: 40.0

    Retorna:
        list: Lista de avistamientos válidos y limpios
              Ej: [{'id_reporte': 'RPT001', 'parque': 'Parque Nacional Corcovado',
                    'especie': 'Panthera onca', 'cantidad': 2,
                    'coordenadas': (8.47, -83.59), 'guardaparque': 'GP-04',
                    'estado_conservacion': 'En Peligro'}, ...]
              (Solo 5 reportes válidos de los 8 originales)

    Ejemplo de descarte:
        RPT003: Distancia ≈ 108 km > 40 km → DESCARTADO
        RPT007: cantidad = 'no_valido' → DESCARTADO
        RPT008: Parque 'Chirripó' no existe → DESCARTADO
    """
    raise NotImplementedError("Implementa validar_y_limpiar_datos")


def generar_reporte_por_parque(avistamientos_validos: list) -> dict:
    """TODO: Generar reporte de individuos por especie en cada parque.

    Proceso:
    1. Crea un diccionario vacío para el resultado
    2. Recorre cada avistamiento
    3. Si el parque no existe en el diccionario, créalo con un diccionario vacío
    4. Si la especie no existe en ese parque, inicialízala en 0
    5. Suma la cantidad de individuos a esa especie en ese parque

    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
                               Ej: [{'id_reporte': 'RPT001', 'parque': 'Parque Nacional Corcovado',
                                     'especie': 'Panthera onca', 'cantidad': 2, ...},
                                    {'id_reporte': 'RPT005', 'parque': 'Parque Nacional Corcovado',
                                     'especie': 'Panthera onca', 'cantidad': 3, ...}]

    Retorna:
        dict: {nombre_parque: {nombre_especie: total_individuos}}
              Ej: {'Parque Nacional Corcovado': {'Panthera onca': 5},
                   'Parque Nacional Manuel Antonio': {'Iguana iguana': 45,
                                                       'Saimiri oerstedii': 30},
                   'Parque Nacional Tortuguero': {'Chelonia mydas': 150}}
    """
    raise NotImplementedError("Implementa generar_reporte_por_parque")


def obtener_especies_unicas_en_riesgo(avistamientos_validos: list) -> set:
    """TODO: Identificar especies en riesgo de conservación.

    Proceso:
    1. Crea un conjunto (set) vacío
    2. Recorre cada avistamiento
    3. Si el estado_conservacion es 'En Peligro' o 'Vulnerable':
       - Agrega la especie al conjunto

    Nota: Usa un conjunto (set) para garantizar que no haya duplicados

    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
                               Ej: [{'especie': 'Panthera onca',
                                     'estado_conservacion': 'En Peligro', ...},
                                    {'especie': 'Iguana iguana',
                                     'estado_conservacion': 'Preocupación Menor', ...}]

    Retorna:
        set: Conjunto con nombres de especies en riesgo
             Ej: {'Panthera onca', 'Chelonia mydas', 'Saimiri oerstedii'}
    """
    raise NotImplementedError("Implementa obtener_especies_unicas_en_riesgo")


def analizar_contribuciones_guardaparques(avistamientos_validos: list) -> dict:
    """TODO: Contar reportes válidos por guardaparque.

    Proceso:
    1. Crea un diccionario vacío
    2. Recorre cada avistamiento
    3. Si el código del guardaparque no está en el diccionario, inicialízalo en 0
    4. Incrementa el contador para ese guardaparque

    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
                               Ej: [{'guardaparque': 'GP-04', ...},
                                    {'guardaparque': 'GP-04', ...},
                                    {'guardaparque': 'GP-07', ...}]

    Retorna:
        dict: {codigo_guardaparque: numero_de_reportes}
              Ej: {'GP-04': 2, 'GP-07': 2, 'GP-11': 1}
    """
    raise NotImplementedError("Implementa analizar_contribuciones_guardaparques")


def encontrar_avistamiento_norte(
    avistamientos_validos: list,
    especie_objetivo: str
) -> str | None:
    """TODO: Encontrar el avistamiento más al norte de una especie.

    Proceso:
    1. Filtra los avistamientos que correspondan a la especie_objetivo
    2. Entre ellos, encuentra el que tiene la latitud más alta
    3. La latitud es el primer elemento de la tupla 'coordenadas'
    4. Retorna el 'id_reporte' de ese avistamiento
    5. Si no hay avistamientos de esa especie, retorna None

    Pista: Puedes usar max() con una función key que extraiga la latitud

    Parámetros:
        avistamientos_validos: Lista de avistamientos limpios
                               Ej: [{'id_reporte': 'RPT001', 'especie': 'Panthera onca',
                                     'coordenadas': (8.47, -83.59), ...},
                                    {'id_reporte': 'RPT005', 'especie': 'Panthera onca',
                                     'coordenadas': (8.49, -83.61), ...}]
        especie_objetivo: Nombre de la especie de interés
                          Ej: 'Panthera onca'

    Retorna:
        str | None: ID del reporte más al norte, o None si no hay avistamientos
                    Ej: 'RPT005'

    Ejemplo de ejecución:
        Para 'Panthera onca':
        - RPT001: coordenadas = (8.47, -83.59) → lat = 8.47
        - RPT005: coordenadas = (8.49, -83.61) → lat = 8.49 ← MÁS AL NORTE
        Retorna: 'RPT005'
    """
    raise NotImplementedError("Implementa encontrar_avistamiento_norte")


def imprimir_informe_final(
    reporte_parques: dict,
    especies_riesgo: set,
    contribuciones_guardaparques: dict,
    reporte_clave: str | None
) -> None:
    """TODO: Imprimir el informe completo formateado.

    El informe debe tener este formato EXACTO:

    ============================================================
    *** INFORME DE MONITOREO DE FAUNA - SINAC ***
    ============================================================

    --- Reporte de Avistamientos por Parque Nacional ---

    > Parque Nacional Corcovado:
      - Panthera onca: 5 individuos

    > Parque Nacional Manuel Antonio:
      - Iguana iguana: 45 individuos
      - Saimiri oerstedii: 30 individuos

    --- Alerta de Especies en Riesgo ---

    Las siguientes especies requieren atención especial:
    * Panthera onca
    * Chelonia mydas
    * Saimiri oerstedii

    --- Contribuciones por Guardaparque ---

    > Reportes válidos por guardaparque:
      - GP-04: 2 reportes
      - GP-07: 2 reportes
      - GP-11: 1 reporte

    --- Punto de Interés Geográfico ---

    > Avistamiento más al norte de 'Panthera onca':
      - ID del Reporte: RPT005

    ============================================================
    *** Fin del Informe ***
    ============================================================

    Pistas:
    - Usa print() para cada línea
    - Recorre los diccionarios con for
    - Para especies en riesgo, itera sobre el conjunto
    - Maneja el caso donde reporte_clave sea None

    Parámetros:
        reporte_parques: Diccionario de parques y especies
                         Ej: {'Parque Nacional Corcovado': {'Panthera onca': 5},
                              'Parque Nacional Manuel Antonio': {'Iguana iguana': 45,
                                                                  'Saimiri oerstedii': 30}}
        especies_riesgo: Conjunto de especies en riesgo
                         Ej: {'Panthera onca', 'Chelonia mydas', 'Saimiri oerstedii'}
        contribuciones_guardaparques: Diccionario de guardaparques
                                      Ej: {'GP-04': 2, 'GP-07': 2, 'GP-11': 1}
        reporte_clave: ID del reporte clave (o None)
                       Ej: 'RPT005' o None

    Retorna:
        None: Solo imprime en consola (no retorna ningún valor)
    """
    raise NotImplementedError("Implementa imprimir_informe_final")


# =============================================================================
# FUNCIÓN PRINCIPAL (YA IMPLEMENTADA COMO GUÍA)
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
    
    try: 
      ejecutar_sistema()
    except NotImplementedError as e:
        print("⚠️  Esta es solo una plantilla. Completa las funciones antes de ejecutar.")
        print("📝 Funciones por implementar:")
        print("   1. calcular_distancia()")
        print("   2. validar_y_limpiar_datos()")
        print("   3. generar_reporte_por_parque()")
        print("   4. obtener_especies_unicas_en_riesgo()")
        print("   5. analizar_contribuciones_guardaparques()")
        print("   6. encontrar_avistamiento_norte()")
        print("   7. imprimir_informe_final()")
        print("\n💡 Cuando todas las funciones estén implementadas, descomenta la línea:")
        print("   # ejecutar_sistema()")
        print()
        print(f"🚫 Error: {e}")
        print("   Complete las funciones marcadas con TODO para ejecutar el sistema.")
