"""
Suite de Pruebas para el Sistema de Análisis de Datos Meteorológicos del IMN

Este archivo contiene pruebas automatizadas para verificar la correcta
implementación de todas las funciones del sistema.

Para ejecutar las pruebas:
    python3 pruebas_para_practica_examen_5.py

Nota: Las funciones deben estar implementadas en el archivo que se importa.
"""

import math


# =============================================================================
# DATOS DE PRUEBA
# =============================================================================

# Información de estaciones para pruebas
info_estaciones_test = {
    'EST-01-SJO': ('San José', 1172),
    'EST-02-LIM': ('Limón', 3),
    'EST-03-CRT': ('Cartago', 1435),
    'EST-04-ALA': ('Alajuela', 952)
}

# Lecturas de prueba (incluye casos válidos e inválidos)
lecturas_test = [
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
# IMPORTAR FUNCIONES A PROBAR
# =============================================================================

# Intenta importar las funciones implementadas
try:
    from practica_de_examen_5_plantilla import (
        validar_y_limpiar_lecturas,
        calcular_promedios_por_estacion,
        identificar_eventos_extremos,
        resumir_precipitacion_por_provincia,
        encontrar_lectura_mas_fria,
        imprimir_reporte_climatico
    )
    FUNCIONES_DISPONIBLES = True
except (ImportError, NotImplementedError):
    FUNCIONES_DISPONIBLES = False
    print("⚠️  Las funciones aún no están implementadas.")
    print("Complete las funciones en practica_de_examen_5_plantilla.py")


# =============================================================================
# FUNCIONES DE PRUEBA
# =============================================================================

def test_validar_y_limpiar_lecturas():
    """Prueba la validación y limpieza de lecturas meteorológicas."""
    print("\n🧪 TEST 1: Validación y Limpieza de Lecturas")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    
    # Debe haber exactamente 6 lecturas válidas
    assert isinstance(validas, list), "El resultado debe ser una lista"
    assert len(validas) == 6, f"Deben quedar 6 lecturas válidas, se obtuvieron: {len(validas)}"
    print(f"✅ Cantidad correcta de lecturas válidas: {len(validas)}/10")
    
    # Verificar que los IDs correctos están presentes
    ids_validos = {r['id_lectura'] for r in validas}
    ids_esperados = {'LEC-001', 'LEC-002', 'LEC-005', 'LEC-007', 'LEC-009', 'LEC-010'}
    assert ids_validos == ids_esperados, f"IDs esperados: {ids_esperados}, obtenidos: {ids_validos}"
    print(f"✅ IDs de lecturas válidas correctos: {sorted(ids_validos)}")
    
    # Verificar que los descartados no están
    ids_descartados = {'LEC-003', 'LEC-004', 'LEC-006', 'LEC-008'}
    for id_desc in ids_descartados:
        assert id_desc not in ids_validos, f"{id_desc} debería haber sido descartado"
    print(f"✅ Lecturas descartadas correctamente: {sorted(ids_descartados)}")
    
    # Verificar limpieza de espacios en código de estación
    for lectura in validas:
        assert lectura['estacion'].strip() == lectura['estacion'], "Estación debe estar sin espacios"
    print("✅ Limpieza de espacios correcta")
    
    # Verificar que temperatura_celsius es float
    for lectura in validas:
        assert isinstance(lectura['temperatura_celsius'], float), f"Temperatura debe ser float: {lectura['id_lectura']}"
    print("✅ Tipo de dato temperatura_celsius correcto")


def test_calcular_promedios_por_estacion():
    """Prueba el cálculo de promedios por estación."""
    print("\n🧪 TEST 2: Cálculo de Promedios por Estación")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    promedios = calcular_promedios_por_estacion(validas)
    
    # Verificar estructura del resultado
    assert isinstance(promedios, dict), "El resultado debe ser un diccionario"
    assert len(promedios) == 4, f"Debe haber 4 estaciones, se encontraron: {len(promedios)}"
    print(f"✅ Número correcto de estaciones: {len(promedios)}")
    
    # Verificar EST-01-SJO (1 lectura)
    assert 'EST-01-SJO' in promedios, "Debe existir EST-01-SJO"
    sjo = promedios['EST-01-SJO']
    assert isinstance(sjo, dict), "Cada estación debe tener un diccionario de promedios"
    assert 'temperatura_promedio' in sjo, "Debe existir temperatura_promedio"
    assert 'humedad_promedio' in sjo, "Debe existir humedad_promedio"
    assert sjo['temperatura_promedio'] == 22.5, f"EST-01-SJO temp: esperado 22.5, obtenido {sjo['temperatura_promedio']}"
    assert sjo['humedad_promedio'] == 80.5, f"EST-01-SJO humedad: esperado 80.5, obtenido {sjo['humedad_promedio']}"
    print(f"✅ EST-01-SJO - Temp: {sjo['temperatura_promedio']}°C, Humedad: {sjo['humedad_promedio']}%")
    
    # Verificar EST-02-LIM (2 lecturas)
    assert 'EST-02-LIM' in promedios, "Debe existir EST-02-LIM"
    lim = promedios['EST-02-LIM']
    temp_esperada_lim = (30.1 + 31.5) / 2  # 30.8
    humedad_esperada_lim = (88.0 + 87.5) / 2  # 87.75
    assert abs(lim['temperatura_promedio'] - temp_esperada_lim) < 0.01, \
        f"EST-02-LIM temp: esperado {temp_esperada_lim}, obtenido {lim['temperatura_promedio']}"
    assert abs(lim['humedad_promedio'] - humedad_esperada_lim) < 0.01, \
        f"EST-02-LIM humedad: esperado {humedad_esperada_lim}, obtenido {lim['humedad_promedio']}"
    print(f"✅ EST-02-LIM - Temp: {lim['temperatura_promedio']:.1f}°C, Humedad: {lim['humedad_promedio']:.1f}%")
    
    # Verificar EST-03-CRT (2 lecturas)
    assert 'EST-03-CRT' in promedios, "Debe existir EST-03-CRT"
    crt = promedios['EST-03-CRT']
    temp_esperada_crt = (18.9 + 16.5) / 2  # 17.7
    humedad_esperada_crt = (90.0 + 92.3) / 2  # 91.15
    assert abs(crt['temperatura_promedio'] - temp_esperada_crt) < 0.01, \
        f"EST-03-CRT temp: esperado {temp_esperada_crt}, obtenido {crt['temperatura_promedio']}"
    assert abs(crt['humedad_promedio'] - humedad_esperada_crt) < 0.01, \
        f"EST-03-CRT humedad: esperado {humedad_esperada_crt}, obtenido {crt['humedad_promedio']}"
    print(f"✅ EST-03-CRT - Temp: {crt['temperatura_promedio']:.1f}°C, Humedad: {crt['humedad_promedio']:.1f}%")
    
    # Verificar EST-04-ALA (1 lectura)
    assert 'EST-04-ALA' in promedios, "Debe existir EST-04-ALA"
    ala = promedios['EST-04-ALA']
    assert ala['temperatura_promedio'] == 36.2, f"EST-04-ALA temp: esperado 36.2, obtenido {ala['temperatura_promedio']}"
    assert ala['humedad_promedio'] == 65.0, f"EST-04-ALA humedad: esperado 65.0, obtenido {ala['humedad_promedio']}"
    print(f"✅ EST-04-ALA - Temp: {ala['temperatura_promedio']}°C, Humedad: {ala['humedad_promedio']}%")


def test_identificar_eventos_extremos():
    """Prueba la identificación de eventos meteorológicos extremos."""
    print("\n🧪 TEST 3: Identificación de Eventos Extremos")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    eventos = identificar_eventos_extremos(validas)
    
    # Verificar que es un conjunto
    assert isinstance(eventos, set), "El resultado debe ser un conjunto (set)"
    print("✅ Tipo de dato correcto: set")
    
    # Verificar cantidad de eventos extremos
    assert len(eventos) == 2, f"Deben ser 2 eventos extremos, se encontraron: {len(eventos)}"
    print(f"✅ Cantidad de eventos extremos: {len(eventos)}")
    
    # Verificar IDs específicos
    ids_esperados = {'LEC-007', 'LEC-010'}
    assert eventos == ids_esperados, f"IDs esperados: {ids_esperados}, obtenidos: {eventos}"
    print(f"✅ IDs de eventos extremos correctos:")
    
    # Explicar por qué son extremos
    for lectura in validas:
        if lectura['id_lectura'] == 'LEC-007':
            print(f"   * LEC-007: precipitación {lectura['precipitacion_mm']} mm > 20.0 mm")
        if lectura['id_lectura'] == 'LEC-010':
            print(f"   * LEC-010: temperatura {lectura['temperatura_celsius']}°C > 35.0°C")


def test_resumir_precipitacion_por_provincia():
    """Prueba el resumen de precipitación por provincia."""
    print("\n🧪 TEST 4: Resumen de Precipitación por Provincia")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    precipitacion = resumir_precipitacion_por_provincia(validas, info_estaciones_test)
    
    # Verificar estructura
    assert isinstance(precipitacion, dict), "El resultado debe ser un diccionario"
    assert len(precipitacion) == 4, f"Deben ser 4 provincias, se encontraron: {len(precipitacion)}"
    print(f"✅ Número de provincias: {len(precipitacion)}")
    
    # Verificar precipitación por provincia
    # Limón: LEC-002 (5.5) + LEC-007 (25.3) = 30.8
    assert 'Limón' in precipitacion, "Debe existir Limón"
    assert abs(precipitacion['Limón'] - 30.8) < 0.01, \
        f"Limón: esperado 30.8, obtenido {precipitacion['Limón']}"
    print(f"✅ Limón: {precipitacion['Limón']} mm")
    
    # Cartago: LEC-005 (2.5) + LEC-009 (0.0) = 2.5
    assert 'Cartago' in precipitacion, "Debe existir Cartago"
    assert abs(precipitacion['Cartago'] - 2.5) < 0.01, \
        f"Cartago: esperado 2.5, obtenido {precipitacion['Cartago']}"
    print(f"✅ Cartago: {precipitacion['Cartago']} mm")
    
    # San José: LEC-001 (0.0) = 0.0
    assert 'San José' in precipitacion, "Debe existir San José"
    assert precipitacion['San José'] == 0.0, \
        f"San José: esperado 0.0, obtenido {precipitacion['San José']}"
    print(f"✅ San José: {precipitacion['San José']} mm")
    
    # Alajuela: LEC-010 (0.0) = 0.0
    assert 'Alajuela' in precipitacion, "Debe existir Alajuela"
    assert precipitacion['Alajuela'] == 0.0, \
        f"Alajuela: esperado 0.0, obtenido {precipitacion['Alajuela']}"
    print(f"✅ Alajuela: {precipitacion['Alajuela']} mm")


def test_encontrar_lectura_mas_fria():
    """Prueba la búsqueda de la lectura más fría por estación."""
    print("\n🧪 TEST 5: Lectura Más Fría por Estación")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    
    # Caso 1: EST-03-CRT (2 lecturas: 18.9 y 16.5)
    id_mas_fria_crt = encontrar_lectura_mas_fria(validas, 'EST-03-CRT')
    assert id_mas_fria_crt == 'LEC-009', f"Para EST-03-CRT, esperado LEC-009, obtenido {id_mas_fria_crt}"
    
    # Verificar la temperatura
    lec009 = next(r for r in validas if r['id_lectura'] == 'LEC-009')
    temp_lec009 = lec009['temperatura_celsius']
    print(f"✅ EST-03-CRT más fría: {id_mas_fria_crt} ({temp_lec009}°C)")
    
    # Caso 2: EST-01-SJO (1 sola lectura)
    id_mas_fria_sjo = encontrar_lectura_mas_fria(validas, 'EST-01-SJO')
    assert id_mas_fria_sjo == 'LEC-001', f"Para EST-01-SJO, esperado LEC-001, obtenido {id_mas_fria_sjo}"
    print(f"✅ EST-01-SJO más fría: {id_mas_fria_sjo}")
    
    # Caso 3: EST-02-LIM (2 lecturas: 30.1 y 31.5)
    id_mas_fria_lim = encontrar_lectura_mas_fria(validas, 'EST-02-LIM')
    assert id_mas_fria_lim == 'LEC-002', f"Para EST-02-LIM, esperado LEC-002, obtenido {id_mas_fria_lim}"
    print(f"✅ EST-02-LIM más fría: {id_mas_fria_lim}")
    
    # Caso 4: Estación inexistente
    id_inexistente = encontrar_lectura_mas_fria(validas, 'EST-99-XXX')
    assert id_inexistente is None, f"Para estación inexistente, esperado None, obtenido {id_inexistente}"
    print(f"✅ Estación inexistente retorna: {id_inexistente}")


def test_imprimir_reporte_climatico():
    """Prueba la impresión del reporte climático (verifica que no lance errores)."""
    print("\n🧪 TEST 6: Impresión de Reporte Climático")
    print("-" * 50)
    
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    promedios = calcular_promedios_por_estacion(validas)
    eventos = identificar_eventos_extremos(validas)
    precipitacion = resumir_precipitacion_por_provincia(validas, info_estaciones_test)
    lectura_fria = encontrar_lectura_mas_fria(validas, 'EST-03-CRT')
    
    # Ejecutar la función (no debe lanzar errores)
    try:
        resultado = imprimir_reporte_climatico(promedios, eventos, precipitacion, lectura_fria)
        assert resultado is None, "La función debe retornar None"
        print("✅ Función ejecutada sin errores")
        print("✅ Retorna None correctamente")
    except Exception as e:
        raise AssertionError(f"Error al imprimir reporte: {e}")


def test_validaciones_especiales():
    """Pruebas de casos especiales y validaciones."""
    print("\n🧪 TEST 7: Validaciones Especiales")
    print("-" * 50)
    
    # Caso 1: Temperatura fuera de rango (muy baja)
    lectura_temp_baja = [{
        'id_lectura': 'TEMP-BAJA',
        'estacion': 'EST-01-SJO',
        'timestamp': '03:00',
        'temperatura_celsius': -15.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_temp_baja = validar_y_limpiar_lecturas(lectura_temp_baja, info_estaciones_test)
    assert len(validas_temp_baja) == 0, "Temperatura < -10.0 debe ser descartada"
    print("✅ Temperatura fuera de rango (< -10.0°C) descartada")
    
    # Caso 2: Temperatura fuera de rango (muy alta)
    lectura_temp_alta = [{
        'id_lectura': 'TEMP-ALTA',
        'estacion': 'EST-01-SJO',
        'timestamp': '14:00',
        'temperatura_celsius': 50.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_temp_alta = validar_y_limpiar_lecturas(lectura_temp_alta, info_estaciones_test)
    assert len(validas_temp_alta) == 0, "Temperatura > 45.0 debe ser descartada"
    print("✅ Temperatura fuera de rango (> 45.0°C) descartada")
    
    # Caso 3: Humedad negativa
    lectura_humedad_neg = [{
        'id_lectura': 'HUM-NEG',
        'estacion': 'EST-01-SJO',
        'timestamp': '10:00',
        'temperatura_celsius': 25.0,
        'humedad_relativa': -5.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_humedad_neg = validar_y_limpiar_lecturas(lectura_humedad_neg, info_estaciones_test)
    assert len(validas_humedad_neg) == 0, "Humedad < 0.0 debe ser descartada"
    print("✅ Humedad negativa descartada")
    
    # Caso 4: Precipitación negativa
    lectura_precip_neg = [{
        'id_lectura': 'PREC-NEG',
        'estacion': 'EST-01-SJO',
        'timestamp': '10:00',
        'temperatura_celsius': 25.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': -2.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_precip_neg = validar_y_limpiar_lecturas(lectura_precip_neg, info_estaciones_test)
    assert len(validas_precip_neg) == 0, "Precipitación negativa debe ser descartada"
    print("✅ Precipitación negativa descartada")
    
    # Caso 5: Lista vacía
    promedios_vacio = calcular_promedios_por_estacion([])
    assert promedios_vacio == {}, "Lista vacía debe generar diccionario vacío"
    print("✅ Lista vacía manejada correctamente")
    
    # Caso 6: Eventos extremos - lista vacía
    eventos_vacio = identificar_eventos_extremos([])
    assert eventos_vacio == set(), "Lista vacía debe generar conjunto vacío"
    print("✅ Set vacío para lista vacía")
    
    # Caso 7: Precipitación - lista vacía
    precipitacion_vacio = resumir_precipitacion_por_provincia([], info_estaciones_test)
    assert precipitacion_vacio == {}, "Lista vacía debe generar diccionario vacío"
    print("✅ Precipitación con lista vacía manejada correctamente")


def test_validaciones_rangos_limite():
    """Pruebas de valores en los límites de los rangos permitidos."""
    print("\n🧪 TEST 8: Validaciones de Rangos Límite")
    print("-" * 50)
    
    # Temperatura en límite inferior (-10.0)
    lectura_temp_min = [{
        'id_lectura': 'TEMP-MIN',
        'estacion': 'EST-01-SJO',
        'timestamp': '03:00',
        'temperatura_celsius': -10.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_temp_min = validar_y_limpiar_lecturas(lectura_temp_min, info_estaciones_test)
    assert len(validas_temp_min) == 1, "Temperatura -10.0°C debe ser aceptada"
    print("✅ Temperatura límite inferior (-10.0°C) aceptada")
    
    # Temperatura en límite superior (45.0)
    lectura_temp_max = [{
        'id_lectura': 'TEMP-MAX',
        'estacion': 'EST-01-SJO',
        'timestamp': '14:00',
        'temperatura_celsius': 45.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_temp_max = validar_y_limpiar_lecturas(lectura_temp_max, info_estaciones_test)
    assert len(validas_temp_max) == 1, "Temperatura 45.0°C debe ser aceptada"
    print("✅ Temperatura límite superior (45.0°C) aceptada")
    
    # Humedad en límite inferior (0.0)
    lectura_humedad_min = [{
        'id_lectura': 'HUM-MIN',
        'estacion': 'EST-01-SJO',
        'timestamp': '10:00',
        'temperatura_celsius': 25.0,
        'humedad_relativa': 0.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_humedad_min = validar_y_limpiar_lecturas(lectura_humedad_min, info_estaciones_test)
    assert len(validas_humedad_min) == 1, "Humedad 0.0% debe ser aceptada"
    print("✅ Humedad límite inferior (0.0%) aceptada")
    
    # Humedad en límite superior (100.0)
    lectura_humedad_max = [{
        'id_lectura': 'HUM-MAX',
        'estacion': 'EST-01-SJO',
        'timestamp': '10:00',
        'temperatura_celsius': 25.0,
        'humedad_relativa': 100.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_humedad_max = validar_y_limpiar_lecturas(lectura_humedad_max, info_estaciones_test)
    assert len(validas_humedad_max) == 1, "Humedad 100.0% debe ser aceptada"
    print("✅ Humedad límite superior (100.0%) aceptada")
    
    # Temperatura extrema en límite (35.0 - no debe ser evento)
    lectura_temp_35 = [{
        'id_lectura': 'TEMP-35',
        'estacion': 'EST-01-SJO',
        'timestamp': '14:00',
        'temperatura_celsius': 35.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 0.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_35 = validar_y_limpiar_lecturas(lectura_temp_35, info_estaciones_test)
    eventos_35 = identificar_eventos_extremos(validas_35)
    assert len(eventos_35) == 0, "Temperatura 35.0°C no debe ser evento extremo (> 35.0)"
    print("✅ Temperatura 35.0°C no es evento extremo (límite no incluido)")
    
    # Precipitación extrema en límite (20.0 - no debe ser evento)
    lectura_precip_20 = [{
        'id_lectura': 'PREC-20',
        'estacion': 'EST-01-SJO',
        'timestamp': '14:00',
        'temperatura_celsius': 25.0,
        'humedad_relativa': 80.0,
        'precipitacion_mm': 20.0,
        'estado_sensor': 'OPERATIVO'
    }]
    validas_20 = validar_y_limpiar_lecturas(lectura_precip_20, info_estaciones_test)
    eventos_20 = identificar_eventos_extremos(validas_20)
    assert len(eventos_20) == 0, "Precipitación 20.0 mm no debe ser evento extremo (> 20.0)"
    print("✅ Precipitación 20.0 mm no es evento extremo (límite no incluido)")


def test_integracion_completa():
    """Prueba de integración del flujo completo."""
    print("\n🧪 TEST 9: Integración Completa del Sistema")
    print("-" * 50)
    
    # Flujo completo
    validas = validar_y_limpiar_lecturas(lecturas_test, info_estaciones_test)
    promedios = calcular_promedios_por_estacion(validas)
    eventos = identificar_eventos_extremos(validas)
    precipitacion = resumir_precipitacion_por_provincia(validas, info_estaciones_test)
    lectura_fria = encontrar_lectura_mas_fria(validas, 'EST-03-CRT')
    
    # Verificar consistencia
    assert len(promedios) == 4, f"Deben ser 4 estaciones con promedios, obtenidas: {len(promedios)}"
    print(f"✅ Total de estaciones con datos: {len(promedios)}")
    
    assert len(validas) == 6, f"Total de lecturas debe ser 6, obtenido: {len(validas)}"
    print(f"✅ Total de lecturas válidas: {len(validas)}")
    
    # Verificar que hay eventos extremos
    assert len(eventos) == 2, f"Debe haber 2 eventos extremos, obtenidos: {len(eventos)}"
    print(f"✅ Eventos extremos identificados: {len(eventos)}")
    
    # Verificar precipitación total
    total_precipitacion = sum(precipitacion.values())
    assert abs(total_precipitacion - 33.3) < 0.01, \
        f"Precipitación total esperada 33.3, obtenida {total_precipitacion}"
    print(f"✅ Precipitación total acumulada: {total_precipitacion} mm")
    
    # Verificar la lectura más fría
    assert lectura_fria is not None, "Debe encontrarse una lectura más fría para EST-03-CRT"
    assert lectura_fria in [r['id_lectura'] for r in validas], "El ID debe estar en las lecturas válidas"
    print(f"✅ Lectura más fría identificada: {lectura_fria}")
    
    # Verificar que todas las provincias tienen datos
    provincias_esperadas = {'San José', 'Limón', 'Cartago', 'Alajuela'}
    provincias_obtenidas = set(precipitacion.keys())
    assert provincias_obtenidas == provincias_esperadas, \
        f"Provincias esperadas: {provincias_esperadas}, obtenidas: {provincias_obtenidas}"
    print(f"✅ Todas las provincias tienen datos de precipitación")


# =============================================================================
# EJECUTAR TODAS LAS PRUEBAS
# =============================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas y muestra el resumen."""
    
    if not FUNCIONES_DISPONIBLES:
        print("\n❌ No se pueden ejecutar las pruebas.")
        print("Por favor, implemente las funciones en practica_de_examen_5_plantilla.py")
        return
    
    print("=" * 60)
    print("SUITE DE PRUEBAS - SISTEMA DE DATOS METEOROLÓGICOS IMN")
    print("=" * 60)
    
    pruebas_exitosas = 0
    pruebas_totales = 9
    
    try:
        test_validar_y_limpiar_lecturas()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_calcular_promedios_por_estacion()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_identificar_eventos_extremos()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_resumir_precipitacion_por_provincia()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_encontrar_lectura_mas_fria()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_imprimir_reporte_climatico()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_validaciones_especiales()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_validaciones_rangos_limite()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_integracion_completa()
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
