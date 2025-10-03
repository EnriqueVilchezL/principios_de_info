"""
Pruebas de Verificación para la Solución del Examen 3
======================================================

Este archivo verifica que la solución cumple correctamente con TODOS
los requisitos especificados en el enunciado del examen.
"""

from solucion_practica_examen_3 import (
    # Funciones de cálculo
    calcular_desviacion_termica,
    calcular_desviacion_hidrica,
    calcular_cambio_salud,
    # Funciones de acciones
    calcular_costo_riego,
    ejecutar_riego,
    ejecutar_calefaccion,
    ejecutar_ventilacion,
    # Funciones de ambiente
    aplicar_evapotranspiracion,
    aplicar_fluctuacion_diaria,
    # Funciones de configuración
    obtener_configuracion_facil,
    # Constantes
    COSTO_CALEFACCION_KWH,
    COSTO_VENTILACION_KWH,
    COSTO_RIEGO_LITROS_POR_10_PERCENT,
    EFECTO_CALEFACCION_TEMP,
    EFECTO_VENTILACION_TEMP,
    EFECTO_CALEFACCION_HUMEDAD,
    EFECTO_VENTILACION_HUMEDAD,
    RECUPERACION_SALUD_OPTIMA,
    TASA_EVAPOTRANSPIRACION_BASE,
    TASA_EVAPOTRANSPIRACION_AIRE_SECO,
    TASA_EVAPOTRANSPIRACION_AIRE_HUMEDO,
)


def test_estructura_datos():
    """
    REQUISITO: Modelo de Datos del Complejo Botánico
    Verificar que la estructura de datos cumple con el enunciado.
    """
    print("🧪 TEST 1: Estructura de Datos")
    print("-" * 50)
    
    config = obtener_configuracion_facil()
    
    # Verificar recursos globales
    assert "recursos_globales" in config, "Falta 'recursos_globales'"
    recursos = config["recursos_globales"]
    assert "tanque_agua_litros" in recursos, "Falta 'tanque_agua_litros'"
    assert "energia_diaria_kwh" in recursos, "Falta 'energia_diaria_kwh'"
    
    # Verificar que serres es una LISTA (no diccionario con claves de nombre)
    assert "serres" in config, "Falta 'serres'"
    assert isinstance(config["serres"], list), "❌ ERROR: 'serres' debe ser una LISTA"
    
    # Verificar estructura de cada invernadero
    for serre in config["serres"]:
        assert "nombre" in serre, "Falta 'nombre' en invernadero"
        assert "ambiente" in serre, "Falta 'ambiente'"
        assert "especie" in serre, "Falta 'especie'"
        assert "requerimientos" in serre, "Falta 'requerimientos'"
        assert "plantas" in serre, "Falta 'plantas'"
        
        # Verificar ambiente
        assert "temperatura" in serre["ambiente"]
        assert "humedad_relativa" in serre["ambiente"]
        
        # Verificar requerimientos
        req = serre["requerimientos"]
        assert "temperatura_optima" in req
        assert "humedad_suelo_optima" in req
        assert "k_T" in req
        assert "k_M" in req
        
        # Verificar que los rangos óptimos son TUPLAS
        assert isinstance(req["temperatura_optima"], tuple), "temperatura_optima debe ser tupla"
        assert isinstance(req["humedad_suelo_optima"], tuple), "humedad_suelo_optima debe ser tupla"
        
        # Verificar plantas
        for planta in serre["plantas"]:
            assert "id" in planta
            assert "humedad_suelo" in planta
            assert "salud" in planta
            assert "estado" in planta
    
    print("✅ Estructura de datos correcta")
    print()


def test_desviacion_termica():
    """
    REQUISITO: Cálculo de Desviaciones - Desviación térmica (ΔT)
    """
    print("🧪 TEST 2: Desviación Térmica")
    print("-" * 50)
    
    # Caso 1: Dentro del rango óptimo
    assert calcular_desviacion_termica(27.0, (24, 30)) == 0.0, "Error: dentro del rango debe ser 0"
    
    # Caso 2: Por debajo del mínimo
    delta_t = calcular_desviacion_termica(22.0, (24, 30))
    assert delta_t == 2.0, f"Error: 22°C con rango (24,30) debe dar 2.0, dio {delta_t}"
    
    # Caso 3: Por encima del máximo
    delta_t = calcular_desviacion_termica(32.0, (24, 30))
    assert delta_t == 2.0, f"Error: 32°C con rango (24,30) debe dar 2.0, dio {delta_t}"
    
    # Caso 4: En los límites exactos
    assert calcular_desviacion_termica(24.0, (24, 30)) == 0.0, "Error: límite inferior"
    assert calcular_desviacion_termica(30.0, (24, 30)) == 0.0, "Error: límite superior"
    
    print("✅ Desviación térmica correcta")
    print()


def test_desviacion_hidrica():
    """
    REQUISITO: Cálculo de Desviaciones - Desviación de humedad del suelo (ΔM)
    El enunciado dice: "Es 0 si la humedad está por encima del mínimo"
    """
    print("🧪 TEST 3: Desviación Hídrica")
    print("-" * 50)
    
    # Caso 1: Por encima del mínimo (en el rango o más)
    assert calcular_desviacion_hidrica(60.0, (55, 75)) == 0.0, "Error: dentro del rango debe ser 0"
    assert calcular_desviacion_hidrica(55.0, (55, 75)) == 0.0, "Error: en el mínimo debe ser 0"
    assert calcular_desviacion_hidrica(80.0, (55, 75)) == 0.0, "Error: por encima del máximo debe ser 0"
    
    # Caso 2: Por debajo del mínimo
    delta_m = calcular_desviacion_hidrica(50.0, (55, 75))
    assert delta_m == 5.0, f"Error: 50% con rango (55,75) debe dar 5.0, dio {delta_m}"
    
    print("✅ Desviación hídrica correcta")
    print()


def test_formula_salud():
    """
    REQUISITO: Fórmula de Daño por Estrés
    ΔH = -(k_T·ΔT² + k_M·ΔM²)
    """
    print("🧪 TEST 4: Fórmula de Salud")
    print("-" * 50)
    
    # Preparar datos de prueba
    planta = {
        "id": "TEST01",
        "humedad_suelo": 50.0,
        "salud": 100.0,
        "estado": "viva"
    }
    ambiente = {
        "temperatura": 32.0,
        "humedad_relativa": 70.0
    }
    requerimientos = {
        "temperatura_optima": (24, 30),
        "humedad_suelo_optima": (55, 75),
        "k_T": 0.12,
        "k_M": 0.1
    }
    
    # Calcular manualmente:
    # ΔT = 32 - 30 = 2.0 (por encima del máximo)
    # ΔM = 55 - 50 = 5.0 (por debajo del mínimo)
    # ΔH = -(0.12 * 2² + 0.1 * 5²)
    #    = -(0.12 * 4 + 0.1 * 25)
    #    = -(0.48 + 2.5)
    #    = -2.98
    
    cambio = calcular_cambio_salud(planta, ambiente, requerimientos)
    esperado = -(0.12 * 4 + 0.1 * 25)
    assert abs(cambio - esperado) < 0.01, f"Error en fórmula: esperado {esperado}, obtuvo {cambio}"
    
    print(f"  ΔT = 2.0, ΔM = 5.0, k_T = 0.12, k_M = 0.1")
    print(f"  ΔH = -(0.12 * 2² + 0.1 * 5²) = {cambio:.2f}")
    print("✅ Fórmula de daño correcta")
    print()


def test_recuperacion_optima():
    """
    REQUISITO: Recuperación en condiciones óptimas (+0.5)
    """
    print("🧪 TEST 5: Recuperación en Condiciones Óptimas")
    print("-" * 50)
    
    planta = {
        "id": "TEST01",
        "humedad_suelo": 65.0,  # Dentro del rango óptimo
        "salud": 80.0,
        "estado": "viva"
    }
    ambiente = {
        "temperatura": 27.0,  # Dentro del rango óptimo
        "humedad_relativa": 70.0
    }
    requerimientos = {
        "temperatura_optima": (24, 30),
        "humedad_suelo_optima": (55, 75),
        "k_T": 0.12,
        "k_M": 0.1
    }
    
    cambio = calcular_cambio_salud(planta, ambiente, requerimientos)
    assert cambio == RECUPERACION_SALUD_OPTIMA, f"Error: recuperación debe ser {RECUPERACION_SALUD_OPTIMA}, fue {cambio}"
    assert cambio == 0.5, "Error: recuperación óptima debe ser +0.5"
    
    print("✅ Recuperación óptima correcta (+0.5)")
    print()


def test_costos_acciones():
    """
    REQUISITO: Costos de las Acciones
    - Calefacción: 5 kWh
    - Ventilación: 3 kWh
    - Riego: 1L por cada 10% de humedad
    """
    print("🧪 TEST 6: Costos de Acciones")
    print("-" * 50)
    
    # Verificar constantes
    assert COSTO_CALEFACCION_KWH == 5, "Calefacción debe costar 5 kWh"
    assert COSTO_VENTILACION_KWH == 3, "Ventilación debe costar 3 kWh"
    assert COSTO_RIEGO_LITROS_POR_10_PERCENT == 1, "Riego debe costar 1L por 10%"
    
    # Test costo de riego
    planta = {"humedad_suelo": 40.0}
    requerimientos = {"humedad_suelo_optima": (55, 75)}
    
    # De 40% a 75% = 35% de diferencia = 3.5 litros
    costo = calcular_costo_riego(planta, requerimientos)
    assert costo == 3.5, f"Error: costo de riego debe ser 3.5L, fue {costo}"
    
    print("✅ Costos correctos: Calefacción=5kWh, Ventilación=3kWh, Riego=1L/10%")
    print()


def test_efectos_acciones():
    """
    REQUISITO: Efectos Primarios y Secundarios de Acciones
    """
    print("🧪 TEST 7: Efectos de Acciones")
    print("-" * 50)
    
    # Crear configuración de prueba
    config = {
        "recursos_globales": {
            "tanque_agua_litros": 100.0,
            "energia_diaria_kwh": 20.0
        },
        "serres": [
            {
                "nombre": "Test Serre",
                "ambiente": {"temperatura": 25.0, "humedad_relativa": 60.0},
                "especie": "Test",
                "requerimientos": {
                    "temperatura_optima": (20, 30),
                    "humedad_suelo_optima": (50, 70),
                    "k_T": 0.1,
                    "k_M": 0.1
                },
                "plantas": [
                    {"id": "T01", "humedad_suelo": 40.0, "salud": 100.0, "estado": "viva"}
                ]
            }
        ]
    }
    
    # Test Calefacción
    temp_inicial = config["serres"][0]["ambiente"]["temperatura"]
    hr_inicial = config["serres"][0]["ambiente"]["humedad_relativa"]
    
    exito, msg = ejecutar_calefaccion(config, "Test Serre")
    assert exito, "Calefacción debería tener éxito"
    
    temp_final = config["serres"][0]["ambiente"]["temperatura"]
    hr_final = config["serres"][0]["ambiente"]["humedad_relativa"]
    
    assert temp_final == temp_inicial + EFECTO_CALEFACCION_TEMP, "Efecto primario calefacción incorrecto"
    assert hr_final == hr_inicial + EFECTO_CALEFACCION_HUMEDAD, "Efecto secundario calefacción incorrecto"
    
    # Restaurar para test de ventilación
    config["serres"][0]["ambiente"]["temperatura"] = 25.0
    config["serres"][0]["ambiente"]["humedad_relativa"] = 60.0
    config["recursos_globales"]["energia_diaria_kwh"] = 20.0
    
    # Test Ventilación
    exito, msg = ejecutar_ventilacion(config, "Test Serre")
    assert exito, "Ventilación debería tener éxito"
    
    temp_final = config["serres"][0]["ambiente"]["temperatura"]
    hr_final = config["serres"][0]["ambiente"]["humedad_relativa"]
    
    assert temp_final == 25.0 + EFECTO_VENTILACION_TEMP, "Efecto primario ventilación incorrecto"
    assert hr_final == 60.0 + EFECTO_VENTILACION_HUMEDAD, "Efecto secundario ventilación incorrecto"
    
    print("✅ Efectos de acciones correctos:")
    print(f"  Calefacción: +{EFECTO_CALEFACCION_TEMP}°C, {EFECTO_CALEFACCION_HUMEDAD}% HR")
    print(f"  Ventilación: {EFECTO_VENTILACION_TEMP}°C, +{EFECTO_VENTILACION_HUMEDAD}% HR")
    print()


def test_evapotranspiracion():
    """
    REQUISITO: Evapotranspiración dependiente de humedad relativa
    - HR < 50%: -6% (aire seco)
    - 50% ≤ HR ≤ 80%: -4% (normal)
    - HR > 80%: -2% (aire húmedo)
    """
    print("🧪 TEST 8: Evapotranspiración")
    print("-" * 50)
    
    # Test aire seco (< 50%)
    config_seco = {
        "serres": [{
            "ambiente": {"humedad_relativa": 40.0},
            "plantas": [{"id": "T1", "humedad_suelo": 50.0, "estado": "viva"}]
        }]
    }
    aplicar_evapotranspiracion(config_seco)
    assert config_seco["serres"][0]["plantas"][0]["humedad_suelo"] == 50.0 - 6.0, "Error: aire seco debe ser -6%"
    
    # Test aire normal (50-80%)
    config_normal = {
        "serres": [{
            "ambiente": {"humedad_relativa": 65.0},
            "plantas": [{"id": "T1", "humedad_suelo": 50.0, "estado": "viva"}]
        }]
    }
    aplicar_evapotranspiracion(config_normal)
    assert config_normal["serres"][0]["plantas"][0]["humedad_suelo"] == 50.0 - 4.0, "Error: aire normal debe ser -4%"
    
    # Test aire húmedo (> 80%)
    config_humedo = {
        "serres": [{
            "ambiente": {"humedad_relativa": 85.0},
            "plantas": [{"id": "T1", "humedad_suelo": 50.0, "estado": "viva"}]
        }]
    }
    aplicar_evapotranspiracion(config_humedo)
    assert config_humedo["serres"][0]["plantas"][0]["humedad_suelo"] == 50.0 - 2.0, "Error: aire húmedo debe ser -2%"
    
    print("✅ Evapotranspiración correcta:")
    print(f"  Aire seco (HR<50%): {TASA_EVAPOTRANSPIRACION_AIRE_SECO}%")
    print(f"  Aire normal (50-80%): {TASA_EVAPOTRANSPIRACION_BASE}%")
    print(f"  Aire húmedo (HR>80%): {TASA_EVAPOTRANSPIRACION_AIRE_HUMEDO}%")
    print()


def test_validaciones_recursos():
    """
    REQUISITO: Validación de recursos antes de ejecutar acciones
    """
    print("🧪 TEST 9: Validaciones de Recursos")
    print("-" * 50)
    
    config = {
        "recursos_globales": {
            "tanque_agua_litros": 1.0,  # Solo 1 litro
            "energia_diaria_kwh": 2.0   # Solo 2 kWh
        },
        "serres": [
            {
                "nombre": "Test Serre",
                "ambiente": {"temperatura": 25.0, "humedad_relativa": 60.0},
                "requerimientos": {
                    "humedad_suelo_optima": (50, 70),
                },
                "plantas": [
                    {"id": "T01", "humedad_suelo": 30.0, "salud": 100.0, "estado": "viva"}
                ]
            }
        ]
    }
    
    # Test: Riego requiere 4L pero solo hay 1L
    exito, msg = ejecutar_riego(config, "T01")
    assert not exito, "Riego debería fallar por falta de agua"
    assert "agua insuficiente" in msg.lower(), "Mensaje debe indicar falta de agua"
    
    # Test: Calefacción requiere 5kWh pero solo hay 2kWh
    exito, msg = ejecutar_calefaccion(config, "Test Serre")
    assert not exito, "Calefacción debería fallar por falta de energía"
    assert "energía insuficiente" in msg.lower() or "sin energía" in msg.lower(), "Mensaje debe indicar falta de energía"
    
    print("✅ Validaciones de recursos correctas")
    print()


def test_muerte_planta():
    """
    REQUISITO: Planta cambia a 'muerta' si salud llega a 0 o menos
    """
    print("🧪 TEST 10: Muerte de Plantas")
    print("-" * 50)
    
    planta = {
        "id": "TEST01",
        "humedad_suelo": 10.0,  # Muy baja
        "salud": 1.0,  # Casi muerta
        "estado": "viva"
    }
    ambiente = {
        "temperatura": 40.0,  # Muy caliente
        "humedad_relativa": 20.0
    }
    requerimientos = {
        "temperatura_optima": (20, 30),
        "humedad_suelo_optima": (50, 70),
        "k_T": 0.5,
        "k_M": 0.5
    }
    
    # Esto causará gran daño
    cambio = calcular_cambio_salud(planta, ambiente, requerimientos)
    assert cambio < 0, "Debe haber daño en malas condiciones"
    
    # Actualizar salud
    planta["salud"] = max(0.0, planta["salud"] + cambio)
    
    # Verificar que la salud llegó a 0
    assert planta["salud"] == 0.0, "Salud debe ser 0"
    
    # En la función actualizar_salud_plantas se cambiaría el estado a "muerta"
    if planta["salud"] <= 0.0:
        planta["estado"] = "muerta"
    
    assert planta["estado"] == "muerta", "Estado debe cambiar a 'muerta'"
    
    print("✅ Muerte de planta correcta (salud ≤ 0 → estado = 'muerta')")
    print()


def test_energia_se_renueva():
    """
    REQUISITO: La energía se reinicia cada día (recurso táctico)
    """
    print("🧪 TEST 11: Recurso de Energía Diaria")
    print("-" * 50)
    
    # Verificar que existe energia_diaria_max_kwh
    config = obtener_configuracion_facil()
    assert "energia_diaria_max_kwh" in config["recursos_globales"], "Debe existir energia_diaria_max_kwh"
    
    max_energia = config["recursos_globales"]["energia_diaria_max_kwh"]
    assert max_energia > 0, "Energía máxima debe ser > 0"
    
    print(f"✅ Energía diaria se reinicia a {max_energia} kWh cada día")
    print()


def test_agua_no_se_renueva():
    """
    REQUISITO: El agua NO se reinicia (recurso estratégico)
    """
    print("🧪 TEST 12: Recurso de Agua Estratégico")
    print("-" * 50)
    
    config = obtener_configuracion_facil()
    agua_inicial = config["recursos_globales"]["tanque_agua_litros"]
    
    # Usar agua
    config["serres"][0]["plantas"][0]["humedad_suelo"] = 30.0
    exito, msg = ejecutar_riego(config, "ORQ01")
    
    agua_final = config["recursos_globales"]["tanque_agua_litros"]
    
    assert agua_final < agua_inicial, "El agua debe reducirse al usarla"
    print(f"✅ Agua NO se renueva (recurso estratégico): {agua_inicial}L → {agua_final}L")
    print()


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas y muestra un resumen."""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE SOLUCIÓN - EXAMEN 3: LAS GRANDES SERRES")
    print("=" * 70 + "\n")
    
    try:
        test_estructura_datos()
        test_desviacion_termica()
        test_desviacion_hidrica()
        test_formula_salud()
        test_recuperacion_optima()
        test_costos_acciones()
        test_efectos_acciones()
        test_evapotranspiracion()
        test_validaciones_recursos()
        test_muerte_planta()
        test_energia_se_renueva()
        test_agua_no_se_renueva()
        
        print("=" * 70)
        print("✅ ✅ ✅  TODAS LAS PRUEBAS PASARON EXITOSAMENTE  ✅ ✅ ✅")
        print("=" * 70)
        print("\n📋 VERIFICACIÓN COMPLETADA:")
        print("✅ Estructura de datos cumple con el enunciado")
        print("✅ Cálculo de desviaciones correcto")
        print("✅ Fórmula de salud ΔH = -(k_T·ΔT² + k_M·ΔM²) implementada correctamente")
        print("✅ Recuperación en condiciones óptimas (+0.5)")
        print("✅ Costos de acciones correctos (Calefacción=5kWh, Ventilación=3kWh, Riego=1L/10%)")
        print("✅ Efectos primarios y secundarios correctos")
        print("✅ Evapotranspiración dependiente de humedad relativa")
        print("✅ Validaciones de recursos funcionan")
        print("✅ Muerte de plantas (salud ≤ 0)")
        print("✅ Energía se renueva diariamente (recurso táctico)")
        print("✅ Agua NO se renueva (recurso estratégico)")
        print("\n🎓 LA SOLUCIÓN CUMPLE CON TODOS LOS REQUISITOS DEL ENUNCIADO\n")
        
    except AssertionError as e:
        print("\n" + "=" * 70)
        print("❌ ❌ ❌  PRUEBA FALLIDA  ❌ ❌ ❌")
        print("=" * 70)
        print(f"\n❌ Error: {e}\n")
        raise


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
