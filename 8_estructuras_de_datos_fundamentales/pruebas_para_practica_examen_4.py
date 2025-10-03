"""
Suite de Pruebas para el Sistema de Monitoreo de Fauna del SINAC

Este archivo contiene pruebas automatizadas para verificar la correcta
implementación de todas las funciones del sistema.

Para ejecutar las pruebas:
    python3 test_sistema_monitoreo_fauna.py

Nota: Las funciones deben estar implementadas en el archivo que se importa.
"""

import math


# =============================================================================
# DATOS DE PRUEBA
# =============================================================================

# Coordenadas de referencia para pruebas
coordenadas_test = {
    'Parque Nacional Corcovado': (8.55, -83.60),
    'Parque Nacional Manuel Antonio': (9.40, -84.15),
    'Parque Nacional Tortuguero': (10.53, -83.50)
}

radio_test = 40.0

# Avistamientos de prueba (incluye casos válidos e inválidos)
avistamientos_test = [
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
    # Este reporte está geográficamente fuera del radio
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
    # Este reporte tiene cantidad inválida
    {
        'id_reporte': 'RPT007',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Puma concolor',
        'cantidad': 'no_valido',
        'coordenadas': (8.50, -83.60),
        'guardaparque': 'GP-04',
        'estado_conservacion': 'Preocupación Menor'
    },
    # Este reporte tiene parque no registrado
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
# IMPORTAR FUNCIONES A PROBAR
# =============================================================================

# Intenta importar las funciones implementadas
try:
    from practica_de_examen_4_plantilla import (
        calcular_distancia,
        validar_y_limpiar_datos,
        generar_reporte_por_parque,
        obtener_especies_unicas_en_riesgo,
        analizar_contribuciones_guardaparques,
        encontrar_avistamiento_norte,
        imprimir_informe_final
    )
    FUNCIONES_DISPONIBLES = True
except (ImportError, NotImplementedError):
    FUNCIONES_DISPONIBLES = False
    print("⚠️  Las funciones aún no están implementadas.")
    print("Complete las funciones en sistema_monitoreo_fauna_plantilla.py")


# =============================================================================
# FUNCIONES DE PRUEBA
# =============================================================================

def test_calcular_distancia():
    """Prueba la función de cálculo de distancia geográfica."""
    print("\n🧪 TEST 1: Cálculo de Distancia Geográfica")
    print("-" * 50)
    
    # Caso 1: Distancia entre Corcovado y avistamiento cercano
    coords1 = (8.55, -83.60)  # Centro Corcovado
    coords2 = (8.47, -83.59)  # Avistamiento RPT001
    distancia = calcular_distancia(coords1, coords2)
    
    # La distancia debe ser aproximadamente 8.9 km
    assert isinstance(distancia, float), "La distancia debe ser un número flotante"
    assert 8.0 < distancia < 10.0, f"Distancia esperada ~8.9 km, obtenida: {distancia:.2f} km"
    print(f"✅ Distancia Corcovado-RPT001: {distancia:.2f} km (esperado ~8.9 km)")
    
    # Caso 2: Mismo punto (distancia = 0)
    distancia_cero = calcular_distancia(coords1, coords1)
    assert distancia_cero == 0.0, "La distancia de un punto a sí mismo debe ser 0"
    print(f"✅ Distancia mismo punto: {distancia_cero:.2f} km")
    
    # Caso 3: Distancia grande (RPT003 fuera del radio)
    coords3 = (9.52, -83.68)
    distancia_grande = calcular_distancia(coords1, coords3)
    assert distancia_grande > 40.0, f"RPT003 debe estar fuera del radio de 40 km: {distancia_grande:.2f} km"
    print(f"✅ Distancia Corcovado-RPT003: {distancia_grande:.2f} km (>40 km, fuera de rango)")
    

def test_validar_y_limpiar_datos():
    """Prueba la validación y limpieza de datos."""
    print("\n🧪 TEST 2: Validación y Limpieza de Datos")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    
    # Debe haber exactamente 5 reportes válidos
    assert isinstance(validos, list), "El resultado debe ser una lista"
    assert len(validos) == 5, f"Deben quedar 5 reportes válidos, se obtuvieron: {len(validos)}"
    print(f"✅ Cantidad correcta de reportes válidos: {len(validos)}/8")
    
    # Verificar que los IDs correctos están presentes
    ids_validos = {r['id_reporte'] for r in validos}
    ids_esperados = {'RPT001', 'RPT002', 'RPT004', 'RPT005', 'RPT006'}
    assert ids_validos == ids_esperados, f"IDs esperados: {ids_esperados}, obtenidos: {ids_validos}"
    print(f"✅ IDs de reportes válidos correctos: {sorted(ids_validos)}")
    
    # Verificar que los descartados no están
    ids_descartados = {'RPT003', 'RPT007', 'RPT008'}
    for id_desc in ids_descartados:
        assert id_desc not in ids_validos, f"{id_desc} debería haber sido descartado"
    print(f"✅ Reportes descartados correctamente: {sorted(ids_descartados)}")
    
    # Verificar limpieza de espacios
    for reporte in validos:
        assert reporte['parque'].strip() == reporte['parque'], "Parque debe estar sin espacios"
        assert reporte['especie'].strip() == reporte['especie'], "Especie debe estar sin espacios"
    print("✅ Limpieza de espacios correcta")
    
    # Verificar conversión de cantidad a entero
    for reporte in validos:
        assert isinstance(reporte['cantidad'], int), f"Cantidad debe ser entero: {reporte['id_reporte']}"
    print("✅ Conversión de cantidad a entero correcta")


def test_generar_reporte_por_parque():
    """Prueba la generación del reporte por parque."""
    print("\n🧪 TEST 3: Generación de Reporte por Parque")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    reporte = generar_reporte_por_parque(validos)
    
    # Verificar estructura del reporte
    assert isinstance(reporte, dict), "El reporte debe ser un diccionario"
    assert len(reporte) == 3, f"Debe haber 3 parques, se encontraron: {len(reporte)}"
    print(f"✅ Número correcto de parques: {len(reporte)}")
    
    # Verificar Parque Nacional Corcovado
    assert 'Parque Nacional Corcovado' in reporte, "Debe existir Parque Nacional Corcovado"
    corcovado = reporte['Parque Nacional Corcovado']
    assert 'Panthera onca' in corcovado, "Debe haber Panthera onca en Corcovado"
    assert corcovado['Panthera onca'] == 5, f"Panthera onca: esperado 5, obtenido {corcovado['Panthera onca']}"
    print(f"✅ Corcovado - Panthera onca: {corcovado['Panthera onca']} individuos")
    
    # Verificar Parque Nacional Manuel Antonio
    assert 'Parque Nacional Manuel Antonio' in reporte, "Debe existir Parque Nacional Manuel Antonio"
    manuel_antonio = reporte['Parque Nacional Manuel Antonio']
    assert 'Iguana iguana' in manuel_antonio, "Debe haber Iguana iguana"
    assert manuel_antonio['Iguana iguana'] == 45, f"Iguana iguana: esperado 45, obtenido {manuel_antonio['Iguana iguana']}"
    assert 'Saimiri oerstedii' in manuel_antonio, "Debe haber Saimiri oerstedii"
    assert manuel_antonio['Saimiri oerstedii'] == 30, f"Saimiri oerstedii: esperado 30, obtenido {manuel_antonio['Saimiri oerstedii']}"
    print(f"✅ Manuel Antonio - Iguana iguana: {manuel_antonio['Iguana iguana']} individuos")
    print(f"✅ Manuel Antonio - Saimiri oerstedii: {manuel_antonio['Saimiri oerstedii']} individuos")
    
    # Verificar Parque Nacional Tortuguero
    assert 'Parque Nacional Tortuguero' in reporte, "Debe existir Parque Nacional Tortuguero"
    tortuguero = reporte['Parque Nacional Tortuguero']
    assert 'Chelonia mydas' in tortuguero, "Debe haber Chelonia mydas"
    assert tortuguero['Chelonia mydas'] == 150, f"Chelonia mydas: esperado 150, obtenido {tortuguero['Chelonia mydas']}"
    print(f"✅ Tortuguero - Chelonia mydas: {tortuguero['Chelonia mydas']} individuos")


def test_obtener_especies_unicas_en_riesgo():
    """Prueba la identificación de especies en riesgo."""
    print("\n🧪 TEST 4: Identificación de Especies en Riesgo")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    especies_riesgo = obtener_especies_unicas_en_riesgo(validos)
    
    # Verificar que es un conjunto
    assert isinstance(especies_riesgo, set), "El resultado debe ser un conjunto (set)"
    print("✅ Tipo de dato correcto: set")
    
    # Verificar cantidad de especies en riesgo
    assert len(especies_riesgo) == 3, f"Deben ser 3 especies en riesgo, se encontraron: {len(especies_riesgo)}"
    print(f"✅ Cantidad de especies en riesgo: {len(especies_riesgo)}")
    
    # Verificar especies específicas
    especies_esperadas = {'Panthera onca', 'Chelonia mydas', 'Saimiri oerstedii'}
    assert especies_riesgo == especies_esperadas, f"Especies esperadas: {especies_esperadas}, obtenidas: {especies_riesgo}"
    print(f"✅ Especies en riesgo correctas:")
    for especie in sorted(especies_riesgo):
        print(f"   * {especie}")


def test_analizar_contribuciones_guardaparques():
    """Prueba el análisis de contribuciones de guardaparques."""
    print("\n🧪 TEST 5: Análisis de Contribuciones de Guardaparques")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    contribuciones = analizar_contribuciones_guardaparques(validos)
    
    # Verificar estructura
    assert isinstance(contribuciones, dict), "El resultado debe ser un diccionario"
    assert len(contribuciones) == 3, f"Deben ser 3 guardaparques, se encontraron: {len(contribuciones)}"
    print(f"✅ Número de guardaparques: {len(contribuciones)}")
    
    # Verificar contribuciones específicas
    assert contribuciones.get('GP-04') == 2, f"GP-04: esperado 2, obtenido {contribuciones.get('GP-04')}"
    assert contribuciones.get('GP-07') == 2, f"GP-07: esperado 2, obtenido {contribuciones.get('GP-07')}"
    assert contribuciones.get('GP-11') == 1, f"GP-11: esperado 1, obtenido {contribuciones.get('GP-11')}"
    
    print(f"✅ GP-04: {contribuciones['GP-04']} reportes")
    print(f"✅ GP-07: {contribuciones['GP-07']} reportes")
    print(f"✅ GP-11: {contribuciones['GP-11']} reportes")
    
    # Verificar que GP-15 no está (fue descartado)
    assert 'GP-15' not in contribuciones, "GP-15 no debe estar (reporte descartado)"
    print("✅ GP-15 correctamente excluido (reporte inválido)")


def test_encontrar_avistamiento_norte():
    """Prueba la búsqueda del avistamiento más al norte."""
    print("\n🧪 TEST 6: Avistamiento Más al Norte")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    
    # Caso 1: Panthera onca (hay 2 avistamientos válidos)
    id_norte = encontrar_avistamiento_norte(validos, 'Panthera onca')
    assert id_norte == 'RPT005', f"Para Panthera onca, esperado RPT005, obtenido {id_norte}"
    
    # Verificar la latitud
    rpt005 = next(r for r in validos if r['id_reporte'] == 'RPT005')
    lat_rpt005 = rpt005['coordenadas'][0]
    print(f"✅ Panthera onca más al norte: {id_norte} (lat: {lat_rpt005})")
    
    # Caso 2: Especie con un solo avistamiento
    id_chelonia = encontrar_avistamiento_norte(validos, 'Chelonia mydas')
    assert id_chelonia == 'RPT004', f"Para Chelonia mydas, esperado RPT004, obtenido {id_chelonia}"
    print(f"✅ Chelonia mydas más al norte: {id_chelonia}")
    
    # Caso 3: Especie que no existe
    id_inexistente = encontrar_avistamiento_norte(validos, 'Especie Inexistente')
    assert id_inexistente is None, f"Para especie inexistente, esperado None, obtenido {id_inexistente}"
    print(f"✅ Especie inexistente retorna: {id_inexistente}")


def test_imprimir_informe_final():
    """Prueba la impresión del informe final (verifica que no lance errores)."""
    print("\n🧪 TEST 7: Impresión de Informe Final")
    print("-" * 50)
    
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    reporte_parques = generar_reporte_por_parque(validos)
    especies_riesgo = obtener_especies_unicas_en_riesgo(validos)
    contribuciones = analizar_contribuciones_guardaparques(validos)
    id_norte = encontrar_avistamiento_norte(validos, 'Panthera onca')
    
    # Ejecutar la función (no debe lanzar errores)
    try:
        resultado = imprimir_informe_final(reporte_parques, especies_riesgo, contribuciones, id_norte)
        assert resultado is None, "La función debe retornar None"
        print("✅ Función ejecutada sin errores")
        print("✅ Retorna None correctamente")
    except Exception as e:
        raise AssertionError(f"Error al imprimir informe: {e}")


def test_validaciones_especiales():
    """Pruebas de casos especiales y validaciones."""
    print("\n🧪 TEST 8: Validaciones Especiales")
    print("-" * 50)
    
    # Caso 1: Cantidad negativa
    reporte_negativo = [{
        'id_reporte': 'NEG01',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Test',
        'cantidad': -5,
        'coordenadas': (8.50, -83.60),
        'guardaparque': 'GP-99',
        'estado_conservacion': 'En Peligro'
    }]
    validos_neg = validar_y_limpiar_datos(reporte_negativo, coordenadas_test, radio_test)
    assert len(validos_neg) == 0, "Cantidad negativa debe ser descartada"
    print("✅ Cantidad negativa descartada correctamente")
    
    # Caso 2: Cantidad cero
    reporte_cero = [{
        'id_reporte': 'CER01',
        'parque': 'Parque Nacional Corcovado',
        'especie': 'Test',
        'cantidad': 0,
        'coordenadas': (8.50, -83.60),
        'guardaparque': 'GP-99',
        'estado_conservacion': 'En Peligro'
    }]
    validos_cero = validar_y_limpiar_datos(reporte_cero, coordenadas_test, radio_test)
    assert len(validos_cero) == 0, "Cantidad cero debe ser descartada"
    print("✅ Cantidad cero descartada correctamente")
    
    # Caso 3: Lista vacía
    reporte_vacio = generar_reporte_por_parque([])
    assert reporte_vacio == {}, "Lista vacía debe generar diccionario vacío"
    print("✅ Lista vacía manejada correctamente")
    
    # Caso 4: Especies en riesgo - lista vacía
    especies_vacio = obtener_especies_unicas_en_riesgo([])
    assert especies_vacio == set(), "Lista vacía debe generar conjunto vacío"
    print("✅ Set vacío para lista vacía")


def test_integracion_completa():
    """Prueba de integración del flujo completo."""
    print("\n🧪 TEST 9: Integración Completa del Sistema")
    print("-" * 50)
    
    # Flujo completo
    validos = validar_y_limpiar_datos(avistamientos_test, coordenadas_test, radio_test)
    reporte_parques = generar_reporte_por_parque(validos)
    especies_riesgo = obtener_especies_unicas_en_riesgo(validos)
    contribuciones = analizar_contribuciones_guardaparques(validos)
    id_norte = encontrar_avistamiento_norte(validos, 'Panthera onca')
    
    # Verificar consistencia
    total_especies_reportadas = sum(len(especies) for especies in reporte_parques.values())
    assert total_especies_reportadas == 4, f"Deben ser 4 especies únicas reportadas, obtenidas: {total_especies_reportadas}"
    print(f"✅ Total de especies únicas reportadas: {total_especies_reportadas}")
    
    total_reportes = sum(contribuciones.values())
    assert total_reportes == 5, f"Total de reportes debe ser 5, obtenido: {total_reportes}"
    print(f"✅ Total de reportes válidos: {total_reportes}")
    
    # Verificar que hay especies en riesgo
    assert len(especies_riesgo) > 0, "Debe haber al menos una especie en riesgo"
    print(f"✅ Especies en riesgo identificadas: {len(especies_riesgo)}")
    
    # Verificar el avistamiento más al norte
    assert id_norte is not None, "Debe encontrarse un avistamiento de Panthera onca"
    assert id_norte in [r['id_reporte'] for r in validos], "El ID debe estar en los reportes válidos"
    print(f"✅ Avistamiento más al norte identificado: {id_norte}")


# =============================================================================
# EJECUTAR TODAS LAS PRUEBAS
# =============================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas y muestra el resumen."""
    
    if not FUNCIONES_DISPONIBLES:
        print("\n❌ No se pueden ejecutar las pruebas.")
        print("Por favor, implemente las funciones en sistema_monitoreo_fauna_plantilla.py")
        return
    
    print("=" * 60)
    print("SUITE DE PRUEBAS - SISTEMA DE MONITOREO DE FAUNA SINAC")
    print("=" * 60)
    
    pruebas_exitosas = 0
    pruebas_totales = 9
    
    try:
        test_calcular_distancia()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_validar_y_limpiar_datos()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_generar_reporte_por_parque()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_obtener_especies_unicas_en_riesgo()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_analizar_contribuciones_guardaparques()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_encontrar_avistamiento_norte()
        pruebas_exitosas += 1
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except NotImplementedError:
        print("❌ Función no implementada")
    
    try:
        test_imprimir_informe_final()
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
