"""
Plantilla del Sistema de Análisis de Datos Meteorológicos del IMN para completar en clase.

Objetivo para el estudiantado:
- Rellenar las funciones marcadas con TODO para que el sistema funcione correctamente.
- Procesar datos de estaciones meteorológicas, validar información y generar reportes climáticos.

Contexto:
El Instituto Meteorológico Nacional (IMN) de Costa Rica necesita procesar datos crudos
de estaciones automáticas que recopilan información climática crucial para pronósticos
y toma de decisiones.

🔧 Solo se permite importar el módulo «math» según la consigna original.
"""

import math


# =============================================================================
# DATOS DE REFERENCIA DE ESTACIONES (YA PROPORCIONADOS)
# =============================================================================

# Información de cada estación: {código: (provincia, altitud_msnm)}
info_estaciones_ejemplo = {
    'EST-01-SJO': ('San José', 1172),
    'EST-02-LIM': ('Limón', 3),
    'EST-03-CRT': ('Cartago', 1435),
    'EST-04-ALA': ('Alajuela', 952)
}


# =============================================================================
# DATOS DE LECTURAS DE EJEMPLO (YA PROPORCIONADOS)
# =============================================================================

lecturas_brutas_ejemplo = [
    {
        'id_lectura': 'LEC-001',
        'estacion': ' EST-01-SJO ',
        'timestamp': '08:00',
        'temperatura_celsius': 22.5,
        'humedad_relativa': 80.5,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    },
    {
        'id_lectura': 'LEC-002',
        'estacion': 'EST-02-LIM',
        'timestamp': '08:15',
        'temperatura_celsius': 30.1,
        'humedad_relativa': 88.0,
        'precipitacion_mm': 5.5,
        'estado_sensor': 'OPERATIVO'
    },
    # Temperatura no es un número, debe ser descartada
    {
        'id_lectura': 'LEC-003',
        'estacion': 'EST-03-CRT',
        'timestamp': '08:05',
        'temperatura_celsius': 'diecinueve',
        'humedad_relativa': 85.2,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    },
    # Humedad fuera de rango (mayor a 100), debe ser descartada
    {
        'id_lectura': 'LEC-004',
        'estacion': 'EST-01-SJO',
        'timestamp': '14:30',
        'temperatura_celsius': 26.8,
        'humedad_relativa': 102.0,
        'precipitacion_mm': 15.0,
        'estado_sensor': 'OPERATIVO'
    },
    {
        'id_lectura': 'LEC-005',
        'estacion': 'EST-03-CRT',
        'timestamp': '14:45',
        'temperatura_celsius': 18.9,
        'humedad_relativa': 90.0,
        'precipitacion_mm': 2.5,
        'estado_sensor': 'OPERATIVO'
    },
    # Estación no registrada, debe ser descartada
    {
        'id_lectura': 'LEC-006',
        'estacion': 'EST-05-HER',
        'timestamp': '15:00',
        'temperatura_celsius': 24.0,
        'humedad_relativa': 78.0,
        'precipitacion_mm': 1.0,
        'estado_sensor': 'OPERATIVO'
    },
    {
        'id_lectura': 'LEC-007',
        'estacion': 'EST-02-LIM',
        'timestamp': '15:10',
        'temperatura_celsius': 31.5,
        'humedad_relativa': 87.5,
        'precipitacion_mm': 25.3,
        'estado_sensor': 'OPERATIVO'
    },
    # Sensor con error, debe ser descartada
    {
        'id_lectura': 'LEC-008',
        'estacion': 'EST-04-ALA',
        'timestamp': '15:20',
        'temperatura_celsius': 28.0,
        'humedad_relativa': 70.1,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'ERROR'
    },
    {
        'id_lectura': 'LEC-009',
        'estacion': 'EST-03-CRT',
        'timestamp': '04:00',
        'temperatura_celsius': 16.5,
        'humedad_relativa': 92.3,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    },
    # Temperatura extrema (evento)
    {
        'id_lectura': 'LEC-010',
        'estacion': 'EST-04-ALA',
        'timestamp': '12:00',
        'temperatura_celsius': 36.2,
        'humedad_relativa': 65.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    },
]


# =============================================================================
# FUNCIONES QUE EL ESTUDIANTADO DEBE IMPLEMENTAR
# =============================================================================


def validar_y_limpiar_lecturas(
    lecturas_brutas: list[dict],
    estaciones_validas: dict[str, tuple[str, int]]
) -> list[dict]:
    """TODO: Validar y limpiar los datos de lecturas meteorológicas.

    Proceso de validación (en orden):
    1. Validación de Estación y Sensor:
       - Verifica que el código de 'estacion' exista en estaciones_validas
       - Verifica que 'estado_sensor' sea exactamente 'OPERATIVO'
       - Si alguna condición falla, descarta la lectura

    2. Validación de Tipos y Rangos:
       - Convierte 'temperatura_celsius' a float (usa try-except)
       - Valida que temperatura esté entre -10.0 y 45.0 grados
       - Valida que 'humedad_relativa' esté entre 0.0 y 100.0
       - Valida que 'precipitacion_mm' sea un número no negativo
       - Si alguna validación falla, descarta la lectura

    3. Limpieza de Datos:
       - Aplica .strip() al código de la estación
       - Asegura que temperatura_celsius sea float

    Parámetros:
        lecturas_brutas: Lista de diccionarios con datos sin procesar
                         Ej: [{'id_lectura': 'LEC-001', 'estacion': ' EST-01-SJO ',
                               'timestamp': '08:00', 'temperatura_celsius': 22.5,
                               'humedad_relativa': 80.5, 'precipitacion_mm': 0.0,
                               'estado_sensor': 'OPERATIVO'}, ...]
        estaciones_validas: Diccionario {código_estación: (provincia, altitud)}
                           Ej: {'EST-01-SJO': ('San José', 1172),
                                'EST-02-LIM': ('Limón', 3)}

    Retorna:
        list: Lista de lecturas válidas y limpias
              Ej: [{'id_lectura': 'LEC-001', 'estacion': 'EST-01-SJO',
                    'timestamp': '08:00', 'temperatura_celsius': 22.5,
                    'humedad_relativa': 80.5, 'precipitacion_mm': 0.0,
                    'estado_sensor': 'OPERATIVO'}, ...]
              (Solo 6 lecturas válidas de las 10 originales)

    Ejemplo de descarte:
        LEC-003: temperatura = 'diecinueve' (no numérico) → DESCARTADO
        LEC-004: humedad_relativa = 102.0 > 100.0 → DESCARTADO
        LEC-006: estacion 'EST-05-HER' no existe → DESCARTADO
        LEC-008: estado_sensor = 'ERROR' → DESCARTADO
    """
    raise NotImplementedError("Implementa validar_y_limpiar_lecturas")


def calcular_promedios_por_estacion(lecturas_validas: list[dict]) -> dict[str, dict[str, float]]:
    """TODO: Calcular temperatura y humedad promedio para cada estación.

    Proceso:
    1. Crea un diccionario vacío para el resultado
    2. Para cada estación, acumula las temperaturas y humedades
    3. Divide las sumas por el número de lecturas de cada estación
    4. Almacena los promedios en el diccionario de resultado

    Parámetros:
        lecturas_validas: Lista de lecturas limpias
                         Ej: [{'estacion': 'EST-01-SJO', 'temperatura_celsius': 22.5,
                               'humedad_relativa': 80.5, ...},
                              {'estacion': 'EST-02-LIM', 'temperatura_celsius': 30.1,
                               'humedad_relativa': 88.0, ...}]

    Retorna:
        dict: {código_estación: {'temperatura_promedio': float, 'humedad_promedio': float}}
              Ej: {'EST-01-SJO': {'temperatura_promedio': 22.5, 'humedad_promedio': 80.5},
                   'EST-02-LIM': {'temperatura_promedio': 30.8, 'humedad_promedio': 87.8}}

    Ejemplo de cálculo:
        EST-02-LIM tiene 2 lecturas:
        - LEC-002: temp=30.1, humedad=88.0
        - LEC-007: temp=31.5, humedad=87.5
        Promedio temp: (30.1 + 31.5) / 2 = 30.8
        Promedio humedad: (88.0 + 87.5) / 2 = 87.8
    """
    raise NotImplementedError("Implementa calcular_promedios_por_estacion")


def identificar_eventos_extremos(lecturas_validas: list[dict]) -> set[str]:
    """TODO: Identificar lecturas con eventos meteorológicos extremos.

    Proceso:
    1. Crea un conjunto (set) vacío
    2. Recorre cada lectura
    3. Si temperatura_celsius > 35.0 O precipitacion_mm > 20.0:
       - Agrega el id_lectura al conjunto

    Nota: Usa un conjunto (set) para garantizar IDs únicos

    Parámetros:
        lecturas_validas: Lista de lecturas limpias
                         Ej: [{'id_lectura': 'LEC-007', 'temperatura_celsius': 31.5,
                               'precipitacion_mm': 25.3, ...},
                              {'id_lectura': 'LEC-010', 'temperatura_celsius': 36.2,
                               'precipitacion_mm': 0.0, ...}]

    Retorna:
        set: Conjunto con IDs de lecturas extremas
             Ej: {'LEC-007', 'LEC-010'}

    Ejemplo de evento extremo:
        LEC-007: precipitacion_mm=25.3 > 20.0 → EXTREMO
        LEC-010: temperatura_celsius=36.2 > 35.0 → EXTREMO
    """
    raise NotImplementedError("Implementa identificar_eventos_extremos")


def resumir_precipitacion_por_provincia(
    lecturas_validas: list[dict],
    estaciones: dict[str, tuple[str, int]]
) -> dict[str, float]:
    """TODO: Calcular precipitación total acumulada por provincia.

    Proceso:
    1. Crea un diccionario vacío para el resultado
    2. Para cada lectura:
       - Obtiene el código de la estación
       - Usa el diccionario 'estaciones' para saber la provincia
       - Suma la precipitacion_mm a esa provincia
    3. Si la provincia no existe en el diccionario, inicialízala en 0.0

    Parámetros:
        lecturas_validas: Lista de lecturas limpias
                         Ej: [{'estacion': 'EST-02-LIM', 'precipitacion_mm': 5.5, ...},
                              {'estacion': 'EST-02-LIM', 'precipitacion_mm': 25.3, ...}]
        estaciones: Diccionario {código_estación: (provincia, altitud)}
                   Ej: {'EST-02-LIM': ('Limón', 3),
                        'EST-03-CRT': ('Cartago', 1435)}

    Retorna:
        dict: {nombre_provincia: precipitacion_total_mm}
              Ej: {'Limón': 30.8, 'Cartago': 2.5, 'San José': 0.0, 'Alajuela': 0.0}

    Ejemplo de cálculo:
        EST-02-LIM está en Limón:
        - LEC-002: 5.5 mm
        - LEC-007: 25.3 mm
        Total Limón: 5.5 + 25.3 = 30.8 mm
    """
    raise NotImplementedError("Implementa resumir_precipitacion_por_provincia")


def encontrar_lectura_mas_fria(
    lecturas_validas: list[dict],
    codigo_estacion: str
) -> str | None:
    """TODO: Encontrar la lectura con temperatura más baja de una estación.

    Proceso:
    1. Filtra las lecturas que correspondan a codigo_estacion
    2. Entre ellas, encuentra la que tiene la temperatura_celsius más baja
    3. Retorna el 'id_lectura' de esa lectura
    4. Si no hay lecturas para esa estación, retorna None

    Pista: Puedes usar min() con una función key que extraiga la temperatura

    Parámetros:
        lecturas_validas: Lista de lecturas limpias
                         Ej: [{'id_lectura': 'LEC-005', 'estacion': 'EST-03-CRT',
                               'temperatura_celsius': 18.9, ...},
                              {'id_lectura': 'LEC-009', 'estacion': 'EST-03-CRT',
                               'temperatura_celsius': 16.5, ...}]
        codigo_estacion: Código de la estación de interés
                        Ej: 'EST-03-CRT'

    Retorna:
        str | None: ID de la lectura más fría, o None si no hay lecturas
                    Ej: 'LEC-009'

    Ejemplo de ejecución:
        Para 'EST-03-CRT':
        - LEC-005: temperatura = 18.9
        - LEC-009: temperatura = 16.5 ← MÁS FRÍA
        Retorna: 'LEC-009'
    """
    raise NotImplementedError("Implementa encontrar_lectura_mas_fria")


def imprimir_reporte_climatico(
    promedios: dict[str, dict[str, float]],
    eventos: set[str],
    precipitacion_provincial: dict[str, float],
    reporte_clave: str | None
) -> None:
    """TODO: Imprimir el reporte climático completo formateado.

    El informe debe tener este formato EXACTO:

    ============================================================
    *** REPORTE CLIMÁTICO DIARIO - IMN ***
    ============================================================

    --- Promedios por Estación ---

    > EST-01-SJO:
      - Temperatura Promedio: 22.5 °C
      - Humedad Promedio: 80.5 %

    > EST-02-LIM:
      - Temperatura Promedio: 30.8 °C
      - Humedad Promedio: 87.8 %

    --- Alerta de Eventos Meteorológicos Extremos ---

    Se identificaron los siguientes IDs de lecturas con eventos extremos:
    * LEC-007
    * LEC-010

    --- Precipitación Acumulada por Provincia ---

    > Precipitación total (mm):
      - Limón: 30.8 mm
      - Cartago: 2.5 mm
      - San José: 0.0 mm
      - Alajuela: 0.0 mm

    --- Punto de Interés Climático ---

    > Lectura más fría para la estación 'EST-03-CRT':
      - ID de la Lectura: LEC-009

    ============================================================
    *** Fin del Reporte ***
    ============================================================

    Pistas:
    - Usa print() para cada línea
    - Recorre los diccionarios con for
    - Para eventos extremos, itera sobre el conjunto
    - Maneja el caso donde reporte_clave sea None

    Parámetros:
        promedios: Diccionario de promedios por estación
                  Ej: {'EST-01-SJO': {'temperatura_promedio': 22.5, 'humedad_promedio': 80.5},
                       'EST-02-LIM': {'temperatura_promedio': 30.8, 'humedad_promedio': 87.8}}
        eventos: Conjunto de IDs de lecturas con eventos extremos
                Ej: {'LEC-007', 'LEC-010'}
        precipitacion_provincial: Diccionario de precipitación por provincia
                                 Ej: {'Limón': 30.8, 'Cartago': 2.5, 'San José': 0.0}
        reporte_clave: ID de la lectura más fría (o None)
                      Ej: 'LEC-009' o None

    Retorna:
        None: Solo imprime en consola (no retorna ningún valor)
    """
    raise NotImplementedError("Implementa imprimir_reporte_climatico")


# =============================================================================
# FUNCIÓN PRINCIPAL (YA IMPLEMENTADA COMO GUÍA)
# =============================================================================


def ejecutar_sistema():
    """Ejecuta el flujo completo del sistema de análisis meteorológico."""
    
    # Paso 1: Validar y limpiar datos
    print("🔍 Procesando datos de estaciones meteorológicas...")
    lecturas_validas = validar_y_limpiar_lecturas(
        lecturas_brutas_ejemplo,
        info_estaciones_ejemplo
    )
    print(f"✅ {len(lecturas_validas)} lecturas válidas de {len(lecturas_brutas_ejemplo)} totales\n")
    
    # Paso 2: Calcular promedios por estación
    promedios = calcular_promedios_por_estacion(lecturas_validas)
    
    # Paso 3: Identificar eventos extremos
    eventos = identificar_eventos_extremos(lecturas_validas)
    
    # Paso 4: Resumir precipitación por provincia
    precipitacion_provincial = resumir_precipitacion_por_provincia(
        lecturas_validas,
        info_estaciones_ejemplo
    )
    
    # Paso 5: Encontrar lectura más fría de estación de interés
    estacion_interes = 'EST-03-CRT'
    lectura_mas_fria = encontrar_lectura_mas_fria(lecturas_validas, estacion_interes)
    
    # Paso 6: Imprimir reporte climático
    imprimir_reporte_climatico(
        promedios,
        eventos,
        precipitacion_provincial,
        lectura_mas_fria
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
        print("   1. validar_y_limpiar_lecturas()")
        print("   2. calcular_promedios_por_estacion()")
        print("   3. identificar_eventos_extremos()")
        print("   4. resumir_precipitacion_por_provincia()")
        print("   5. encontrar_lectura_mas_fria()")
        print("   6. imprimir_reporte_climatico()")
        print("\n💡 Cuando todas las funciones estén implementadas, el sistema ejecutará automáticamente.")
        print()
        print(f"🚫 Error: {e}")
        print("   Complete las funciones marcadas con TODO para ejecutar el sistema.")
