"""
Solución Completa del Sistema de Análisis de Datos Meteorológicos del IMN

Este archivo contiene la solución completa con comentarios detallados para
estudiantes principiantes.

Autor: Sistema de Monitoreo IMN
Fecha: Octubre 2025
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
# FUNCIONES IMPLEMENTADAS CON COMENTARIOS EDUCATIVOS
# =============================================================================


def validar_y_limpiar_lecturas(
    lecturas_brutas: list[dict],
    estaciones_validas: dict[str, tuple[str, int]]
) -> list[dict]:
    """
    Valida y limpia los datos de lecturas meteorológicas.
    
    Esta función recibe datos "sucios" y retorna solo los datos válidos y limpios.
    """
    
    # Lista donde guardaremos las lecturas válidas
    lecturas_limpias = []
    
    # Recorremos cada lectura de la lista
    for lectura in lecturas_brutas:
        
        # --- PASO 1: VALIDACIÓN DE ESTACIÓN Y SENSOR ---
        
        # Obtenemos el código de la estación (puede tener espacios)
        codigo_estacion = lectura['estacion'].strip()  # .strip() quita espacios al inicio/final
        
        # Verificamos que la estación exista en nuestro diccionario de estaciones válidas
        if codigo_estacion not in estaciones_validas:
            # Si la estación no existe, descartamos esta lectura y pasamos a la siguiente
            continue
        
        # Verificamos que el sensor esté operativo
        if lectura['estado_sensor'] != 'OPERATIVO':
            # Si el sensor no está operativo, descartamos esta lectura
            continue
        
        # --- PASO 2: VALIDACIÓN DE TEMPERATURA ---
        
        # La temperatura puede venir como número o como texto (por error de entrada)
        # Usamos try-except para manejar el caso donde no se puede convertir a float
        try:
            # Intentamos convertir la temperatura a float
            temperatura = float(lectura['temperatura_celsius'])
        except (ValueError, TypeError):
            # Si no se puede convertir (por ejemplo, es un texto), descartamos la lectura
            continue
        
        # Verificamos que la temperatura esté en un rango realista (-10.0 a 45.0)
        if temperatura < -10.0 or temperatura > 45.0:
            # Si está fuera del rango, descartamos la lectura
            continue
        
        # --- PASO 3: VALIDACIÓN DE HUMEDAD ---
        
        # La humedad debe estar entre 0.0 y 100.0 (es un porcentaje)
        humedad = lectura['humedad_relativa']
        if humedad < 0.0 or humedad > 100.0:
            # Si está fuera del rango, descartamos la lectura
            continue
        
        # --- PASO 4: VALIDACIÓN DE PRECIPITACIÓN ---
        
        # La precipitación no puede ser negativa (no puede llover "hacia arriba")
        precipitacion = lectura['precipitacion_mm']
        if precipitacion < 0.0:
            # Si es negativa, descartamos la lectura
            continue
        
        # --- PASO 5: LIMPIEZA DE DATOS ---
        
        # Si llegamos aquí, la lectura es válida
        # Creamos una copia del diccionario para no modificar el original
        lectura_limpia = lectura.copy()
        
        # Limpiamos el código de la estación (quitamos espacios)
        lectura_limpia['estacion'] = codigo_estacion
        
        # Aseguramos que la temperatura sea float (por si venía como string válido)
        lectura_limpia['temperatura_celsius'] = temperatura
        
        # Agregamos esta lectura limpia a nuestra lista de resultados
        lecturas_limpias.append(lectura_limpia)
    
    # Retornamos la lista con solo las lecturas válidas y limpias
    return lecturas_limpias


def calcular_promedios_por_estacion(lecturas_validas: list[dict]) -> dict[str, dict[str, float]]:
    """
    Calcula la temperatura y humedad promedio para cada estación.
    
    Promedio = (suma de todos los valores) / (cantidad de valores)
    """
    
    # Diccionario para acumular las sumas y contar las lecturas
    # Estructura: {codigo_estacion: {'suma_temp': float, 'suma_humedad': float, 'contador': int}}
    acumuladores = {}
    
    # --- PASO 1: ACUMULAR DATOS ---
    
    # Recorremos cada lectura válida
    for lectura in lecturas_validas:
        # Obtenemos el código de la estación
        estacion = lectura['estacion']
        
        # Si es la primera vez que vemos esta estación, la inicializamos
        if estacion not in acumuladores:
            acumuladores[estacion] = {
                'suma_temp': 0.0,      # Suma de todas las temperaturas
                'suma_humedad': 0.0,   # Suma de todas las humedades
                'contador': 0          # Cantidad de lecturas
            }
        
        # Acumulamos los valores de esta lectura
        acumuladores[estacion]['suma_temp'] += lectura['temperatura_celsius']
        acumuladores[estacion]['suma_humedad'] += lectura['humedad_relativa']
        acumuladores[estacion]['contador'] += 1
    
    # --- PASO 2: CALCULAR PROMEDIOS ---
    
    # Diccionario para guardar los resultados finales
    promedios = {}
    
    # Para cada estación que encontramos
    for estacion, datos in acumuladores.items():
        # Calculamos el promedio dividiendo la suma entre el contador
        temp_promedio = datos['suma_temp'] / datos['contador']
        humedad_promedio = datos['suma_humedad'] / datos['contador']
        
        # Guardamos los promedios en el formato requerido
        promedios[estacion] = {
            'temperatura_promedio': temp_promedio,
            'humedad_promedio': humedad_promedio
        }
    
    # Retornamos el diccionario con los promedios
    return promedios


def identificar_eventos_extremos(lecturas_validas: list[dict]) -> set[str]:
    """
    Identifica lecturas con eventos meteorológicos extremos.
    
    Un evento es extremo si:
    - La temperatura es mayor a 35.0 grados, O
    - La precipitación es mayor a 20.0 mm
    """
    
    # Usamos un conjunto (set) para garantizar que no haya IDs duplicados
    eventos_extremos = set()
    
    # Recorremos cada lectura
    for lectura in lecturas_validas:
        # Obtenemos los valores que nos interesan
        temperatura = lectura['temperatura_celsius']
        precipitacion = lectura['precipitacion_mm']
        
        # Verificamos si cumple alguna condición de evento extremo
        # Nota: Usamos el operador "or" porque con que cumpla UNA condición es suficiente
        if temperatura > 35.0 or precipitacion > 20.0:
            # Si es un evento extremo, agregamos su ID al conjunto
            eventos_extremos.add(lectura['id_lectura'])
    
    # Retornamos el conjunto con los IDs de eventos extremos
    return eventos_extremos


def resumir_precipitacion_por_provincia(
    lecturas_validas: list[dict],
    estaciones: dict[str, tuple[str, int]]
) -> dict[str, float]:
    """
    Calcula la precipitación total acumulada para cada provincia.
    
    Usamos el diccionario de estaciones para saber a qué provincia pertenece cada lectura.
    """
    
    # Diccionario para acumular la precipitación por provincia
    precipitacion_provincial = {}
    
    # Recorremos cada lectura válida
    for lectura in lecturas_validas:
        # Obtenemos el código de la estación
        codigo_estacion = lectura['estacion']
        
        # Buscamos la información de esta estación en el diccionario
        # estaciones[codigo_estacion] es una tupla: (provincia, altitud)
        # Por ejemplo: ('San José', 1172)
        info_estacion = estaciones[codigo_estacion]
        
        # La provincia es el primer elemento de la tupla (índice 0)
        provincia = info_estacion[0]
        
        # Obtenemos la precipitación de esta lectura
        precipitacion = lectura['precipitacion_mm']
        
        # Si es la primera vez que vemos esta provincia, la inicializamos en 0
        if provincia not in precipitacion_provincial:
            precipitacion_provincial[provincia] = 0.0
        
        # Acumulamos la precipitación de esta lectura
        precipitacion_provincial[provincia] += precipitacion
    
    # Retornamos el diccionario con la precipitación total por provincia
    return precipitacion_provincial


def encontrar_lectura_mas_fria(
    lecturas_validas: list[dict],
    codigo_estacion: str
) -> str | None:
    """
    Encuentra la lectura con la temperatura más baja de una estación específica.
    
    Retorna el ID de esa lectura, o None si no hay lecturas para esa estación.
    """
    
    # --- PASO 1: FILTRAR LECTURAS DE LA ESTACIÓN ---
    
    # Creamos una lista solo con las lecturas de la estación que nos interesa
    lecturas_estacion = []
    
    for lectura in lecturas_validas:
        # Si esta lectura es de la estación que buscamos
        if lectura['estacion'] == codigo_estacion:
            # La agregamos a nuestra lista filtrada
            lecturas_estacion.append(lectura)
    
    # --- PASO 2: VERIFICAR SI HAY LECTURAS ---
    
    # Si no hay lecturas para esta estación, retornamos None
    if len(lecturas_estacion) == 0:
        return None
    
    # --- PASO 3: ENCONTRAR LA MÁS FRÍA ---
    
    # Usamos la función min() para encontrar el mínimo
    # El parámetro "key" indica qué valor usar para comparar
    # lambda es una función anónima que extrae la temperatura de cada lectura
    lectura_mas_fria = min(lecturas_estacion, key=lambda x: x['temperatura_celsius'])
    
    # Retornamos el ID de la lectura más fría
    return lectura_mas_fria['id_lectura']


def imprimir_reporte_climatico(
    promedios: dict[str, dict[str, float]],
    eventos: set[str],
    precipitacion_provincial: dict[str, float],
    reporte_clave: str | None
) -> None:
    """
    Imprime el reporte climático completo en un formato profesional.
    
    Esta función solo imprime, no retorna ningún valor.
    """
    
    # --- ENCABEZADO DEL REPORTE ---
    
    print("=" * 60)
    print("*** REPORTE CLIMÁTICO DIARIO - IMN ***")
    print("=" * 60)
    
    # --- SECCIÓN 1: PROMEDIOS POR ESTACIÓN ---
    
    print("\n--- Promedios por Estación ---\n")
    
    # Recorremos cada estación y sus promedios
    for codigo_estacion, datos in promedios.items():
        print(f"> {codigo_estacion}:")
        print(f"  - Temperatura Promedio: {datos['temperatura_promedio']:.1f} °C")
        print(f"  - Humedad Promedio: {datos['humedad_promedio']:.1f} %")
        print()  # Línea en blanco para separar estaciones
    
    # --- SECCIÓN 2: EVENTOS EXTREMOS ---
    
    print("--- Alerta de Eventos Meteorológicos Extremos ---\n")
    
    # Verificamos si hay eventos extremos
    if len(eventos) > 0:
        print("Se identificaron los siguientes IDs de lecturas con eventos extremos:")
        # Recorremos el conjunto de eventos (sets no tienen orden garantizado)
        for id_evento in sorted(eventos):  # sorted() ordena alfabéticamente
            print(f"* {id_evento}")
    else:
        print("No se identificaron eventos extremos en este período.")
    
    # --- SECCIÓN 3: PRECIPITACIÓN POR PROVINCIA ---
    
    print("\n--- Precipitación Acumulada por Provincia ---\n")
    print("> Precipitación total (mm):")
    
    # Recorremos cada provincia y su precipitación
    for provincia, total_mm in precipitacion_provincial.items():
        print(f"  - {provincia}: {total_mm} mm")
    
    # --- SECCIÓN 4: PUNTO DE INTERÉS CLIMÁTICO ---
    
    print("\n--- Punto de Interés Climático ---\n")
    
    # Verificamos si se encontró una lectura clave
    if reporte_clave is not None:
        print(f"> Lectura más fría para la estación 'EST-03-CRT':")
        print(f"  - ID de la Lectura: {reporte_clave}")
    else:
        print("> No se encontraron lecturas para la estación de interés.")
    
    # --- PIE DEL REPORTE ---
    
    print("\n" + "=" * 60)
    print("*** Fin del Reporte ***")
    print("=" * 60)


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
    ejecutar_sistema()
