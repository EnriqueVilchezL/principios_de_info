"""
Plantilla de la simulación "Las Grandes Serres" para completar en clase.

Objetivo para el estudiantado:
- Rellenar las funciones marcadas con TODO para que el juego funcione igual que
  la versión demostrada por el profesorado.
- Mantener el mismo flujo, mensajes y experiencia de usuario.

Sugerencia de uso en el aula:
1. Presenta esta plantilla y explica el diseño general.
2. Asigna a cada estudiante (o grupo) un conjunto de funciones.
3. Valida el resultado ejecutando el juego completo.

🔧 Solo se permite importar «random» según la consigna original.
"""

import random


# =============================================================================
# CONSTANTES DEL JUEGO
# =============================================================================

DIAS_SIMULACION = 10
PROBABILIDAD_EVENTO_CLIMATICO = 0.15

# Costos de acciones
COSTO_CALEFACCION_KWH = 5
COSTO_VENTILACION_KWH = 3
COSTO_RIEGO_LITROS_POR_10_PERCENT = 1

# Efectos de acciones
EFECTO_CALEFACCION_TEMP = 2.0
EFECTO_VENTILACION_TEMP = -2.0
EFECTO_CALEFACCION_HUMEDAD = -5.0
EFECTO_VENTILACION_HUMEDAD = 5.0

# Parámetros ambientales
RECUPERACION_SALUD_OPTIMA = 0.5
TASA_EVAPOTRANSPIRACION_BASE = -4.0
TASA_EVAPOTRANSPIRACION_AIRE_SECO = -6.0
TASA_EVAPOTRANSPIRACION_AIRE_HUMEDO = -2.0
FLUCTUACION_TEMPERATURA_MAX = 1.0
EVENTO_CLIMATICO_CAMBIO_TEMP = 4.0


# =============================================================================
# FUNCIONES DE INICIALIZACIÓN Y CONFIGURACIÓN (YA IMPLEMENTADAS)
# =============================================================================

# Estas tres funciones ya incluyen los datos de partida.
# No necesitan modificaciones para preservar el aspecto del juego.


def obtener_configuracion_facil() -> dict:
    """Configuración de dificultad fácil con 1 invernadero y 2 plantas."""
    return {
        "recursos_globales": {
            "tanque_agua_litros": 320.0,
            "energia_diaria_max_kwh": 24.0,
            "energia_diaria_kwh": 24.0,
        },
        "serres": [
            {
                "nombre": "Serre Tropicale",
                "ambiente": {"temperatura": 27.0, "humedad_relativa": 75.0},
                "especie": "Orquídea Phalaenopsis",
                "requerimientos": {
                    "temperatura_optima": (24, 30),
                    "humedad_suelo_optima": (55, 75),
                    "k_T": 0.12,
                    "k_M": 0.1,
                },
                "plantas": [
                    {
                        "id": "ORQ01",
                        "humedad_suelo": 60.0,
                        "salud": 100.0,
                        "estado": "viva",
                    },
                    {
                        "id": "ORQ02",
                        "humedad_suelo": 58.0,
                        "salud": 98.0,
                        "estado": "viva",
                    },
                ],
            }
        ],
    }


def obtener_configuracion_media() -> dict:
    """Configuración de dificultad media con 1 invernadero y 3 plantas."""
    return {
        "recursos_globales": {
            "tanque_agua_litros": 280.0,
            "energia_diaria_max_kwh": 20.0,
            "energia_diaria_kwh": 20.0,
        },
        "serres": [
            {
                "nombre": "Serre Méditerranéenne",
                "ambiente": {"temperatura": 24.0, "humedad_relativa": 55.0},
                "especie": "Lavanda y Aromáticas",
                "requerimientos": {
                    "temperatura_optima": (20, 27),
                    "humedad_suelo_optima": (35, 55),
                    "k_T": 0.18,
                    "k_M": 0.22,
                },
                "plantas": [
                    {
                        "id": "MED01",
                        "humedad_suelo": 42.0,
                        "salud": 92.0,
                        "estado": "viva",
                    },
                    {
                        "id": "MED02",
                        "humedad_suelo": 38.0,
                        "salud": 88.0,
                        "estado": "viva",
                    },
                    {
                        "id": "MED03",
                        "humedad_suelo": 40.0,
                        "salud": 90.0,
                        "estado": "viva",
                    },
                ],
            }
        ],
    }


def obtener_configuracion_dificil() -> dict:
    """Configuración de dificultad difícil con 2 invernaderos y 4 plantas."""
    return {
        "recursos_globales": {
            "tanque_agua_litros": 240.0,
            "energia_diaria_max_kwh": 18.0,
            "energia_diaria_kwh": 18.0,
        },
        "serres": [
            {
                "nombre": "Serre Xerófila",
                "ambiente": {"temperatura": 36.0, "humedad_relativa": 28.0},
                "especie": "Cactus y Suculentas",
                "requerimientos": {
                    "temperatura_optima": (28, 38),
                    "humedad_suelo_optima": (8, 18),
                    "k_T": 0.25,
                    "k_M": 0.35,
                },
                "plantas": [
                    {
                        "id": "XER01",
                        "humedad_suelo": 12.0,
                        "salud": 85.0,
                        "estado": "viva",
                    },
                    {
                        "id": "XER02",
                        "humedad_suelo": 10.0,
                        "salud": 82.0,
                        "estado": "viva",
                    },
                ],
            },
            {
                "nombre": "Serre Nebulosa",
                "ambiente": {"temperatura": 21.0, "humedad_relativa": 88.0},
                "especie": "Nepenthes y Plantas Carnívoras",
                "requerimientos": {
                    "temperatura_optima": (18, 26),
                    "humedad_suelo_optima": (65, 85),
                    "k_T": 0.3,
                    "k_M": 0.28,
                },
                "plantas": [
                    {
                        "id": "NEB01",
                        "humedad_suelo": 70.0,
                        "salud": 78.0,
                        "estado": "viva",
                    },
                    {
                        "id": "NEB02",
                        "humedad_suelo": 68.0,
                        "salud": 80.0,
                        "estado": "viva",
                    },
                ],
            },
        ],
    }


# =============================================================================
# FUNCIONES QUE EL ESTUDIANTADO DEBE IMPLEMENTAR
# =============================================================================

# Las funciones siguientes están vacías a propósito. Cada docstring incluye la
# guía de implementación. Reemplaza «raise NotImplementedError» con el código
# correspondiente.


def calcular_desviacion_termica(
    temperatura_actual: float, rango_optimo: tuple[float, float]
) -> float:
    """TODO: devolver la desviación térmica respecto al rango óptimo.

    Pasos sugeridos:
    1. Desempaqueta el rango en temp_min y temp_max.
    2. Devuelve 0.0 si la temperatura está dentro del rango [min, max].
    3. Si está por debajo, devuelve la diferencia positiva (temp_min - actual).
    4. Si está por encima, devuelve (actual - temp_max).
    """
    raise NotImplementedError("Implementa calcular_desviacion_termica")


def calcular_desviacion_hidrica(
    humedad_suelo_actual: float, rango_optimo: tuple[float, float]
) -> float:
    """TODO: devolver cuánto falta para alcanzar la humedad mínima óptima.

    Pistas:
    - Solo nos preocupa si la humedad está por debajo del mínimo.
    - Si la planta ya está por encima, devuelve 0.0.
    - En caso contrario, devuelve la diferencia positiva.
    """
    raise NotImplementedError("Implementa calcular_desviacion_hidrica")


def calcular_cambio_salud(planta: dict, ambiente: dict, requerimientos: dict) -> float:
    """TODO: calcular el cambio diario en la salud de una planta.

    Considera:
    - Las plantas muertas no cambian su salud.
    - Usa las funciones de desviación para delta_t y delta_m.
    - Si ambas desviaciones son 0, devuelve RECUPERACION_SALUD_OPTIMA.
    - En otro caso, calcula el daño con la fórmula negativa:
      daño = -(k_T * delta_t ** 2 + k_M * delta_m ** 2)
    """
    raise NotImplementedError("Implementa calcular_cambio_salud")


def actualizar_salud_plantas(configuracion: dict) -> None:
    """TODO: actualizar la salud y estado ('viva'/'muerta') de todas las plantas.

    Recorre cada invernadero y planta:
    - Calcula el cambio usando calcular_cambio_salud.
    - Ajusta la salud entre 0 y 100.
    - Si llega a 0, marca la planta como 'muerta' y guarda un mensaje para
      imprimir al final («La planta X en Y ha muerto»).
    - Muestra los mensajes de muerte fuera del bucle principal.
    """
    raise NotImplementedError("Implementa actualizar_salud_plantas")


def generar_evento_climatico() -> str | None:
    """TODO: devolver un evento aleatorio o None.

    - Usa random.random() y PROBABILIDAD_EVENTO_CLIMATICO.
    - Si ocurre, elige entre "ola_frio" y "dia_soleado" con random.choice.
    - Si no ocurre, devuelve None.
    """
    raise NotImplementedError("Implementa generar_evento_climatico")


def aplicar_evento_climatico(configuracion: dict, evento: str) -> None:
    """TODO: aplicar los cambios de temperatura dependiendo del evento.

    - Si evento == "ola_frio", resta EVENTO_CLIMATICO_CAMBIO_TEMP a la
      temperatura de cada serre y muestra el mensaje correspondiente.
    - Si evento == "dia_soleado", súmalo y muestra el mensaje de calor.
    - No olvides los emojis para mantener la interfaz 🙂.
    """
    raise NotImplementedError("Implementa aplicar_evento_climatico")


def aplicar_fluctuacion_diaria(configuracion: dict) -> None:
    """TODO: sumar una fluctuación aleatoria (-1.0 a +1.0) a la temperatura de cada serre."""
    raise NotImplementedError("Implementa aplicar_fluctuacion_diaria")


def aplicar_evapotranspiracion(configuracion: dict) -> None:
    """TODO: reducir la humedad del suelo según la humedad relativa del aire.

    Receta:
    - Obtén la humedad relativa del serre.
    - Determina la tasa adecuada comparando con 50% y 80%.
    - Resta (o suma porque las tasas son negativas) la tasa del campo
      "humedad_suelo" de cada planta viva, limitando el valor mínimo en 0.
    """
    raise NotImplementedError("Implementa aplicar_evapotranspiracion")


def buscar_planta_por_id(configuracion: dict, planta_id: str) -> tuple[dict | None, dict | None]:
    """TODO: devolver el invernadero y la planta que coinciden con el ID.

    - Recorre cada serre y cada planta.
    - Si la encuentras, retorna (serre, planta).
    - Si terminas sin hallarla, retorna (None, None).
    """
    raise NotImplementedError("Implementa buscar_planta_por_id")


def buscar_serre_por_nombre(configuracion: dict, nombre_serre: str) -> dict | None:
    """TODO: buscar un invernadero ignorando diferencias de mayúsculas/minúsculas."""
    raise NotImplementedError("Implementa buscar_serre_por_nombre")


def calcular_costo_riego(planta: dict, requerimientos: dict) -> float:
    """TODO: determinar cuánta agua cuesta llevar la planta al máximo óptimo.

    - Usa el valor máximo del rango óptimo de humedad del suelo.
    - Si la planta ya está en o por encima, el costo es 0.0.
    - Cada 10 puntos percentuales requieren COSTO_RIEGO_LITROS_POR_10_PERCENT litros.
    """
    raise NotImplementedError("Implementa calcular_costo_riego")


def ejecutar_riego(configuracion: dict, planta_id: str) -> tuple[bool, str]:
    """TODO: lógica completa del riego, devolviendo (éxito, mensaje).

    Pistas:
    - Usa buscar_planta_por_id.
    - Verifica si la planta existe, si está viva y si hay suficiente agua.
    - Descuenta el agua necesaria y ajusta la humedad al máximo óptimo.
    - Devuelve mensajes con los emojis originales.
    """
    raise NotImplementedError("Implementa ejecutar_riego")


def ejecutar_calefaccion(configuracion: dict, nombre_serre: str) -> tuple[bool, str]:
    """TODO: gastar energía para subir la temperatura y reducir humedad relativa.

    - Localiza el serre.
    - Comprueba si hay energía suficiente.
    - Ajusta la temperatura (+2°C) y la humedad (-5%), respetando el mínimo 0.
    """
    raise NotImplementedError("Implementa ejecutar_calefaccion")


def ejecutar_ventilacion(configuracion: dict, nombre_serre: str) -> tuple[bool, str]:
    """TODO: gastar energía para bajar la temperatura y subir la humedad relativa.

    - Ajusta temperatura (-2°C) y humedad (+5%) sin sobrepasar 100%.
    """
    raise NotImplementedError("Implementa ejecutar_ventilacion")


def procesar_comando(configuracion: dict, comando: str) -> tuple[bool, str]:
    """TODO: interpretar el texto que ingresa la persona jugadora.

    - Divide el comando en palabras (acción + argumentos).
    - Soporta: regar, calefaccion, ventilacion, pasar, ayuda, condiciones.
    - Para ayuda y condiciones devuelve (True, texto) sin cambiar contadores.
    - Para errores, devuelve (False, "❌ mensaje de error").
    """
    raise NotImplementedError("Implementa procesar_comando")


def mostrar_condiciones_optimas(configuracion: dict) -> str:
    """TODO: construir el texto con los rangos óptimos y situación actual.

    - Usa exactamente el mismo formato que la versión completa para mantener la UI.
    - Recorre cada serre y lista sus plantas vivas.
    """
    raise NotImplementedError("Implementa mostrar_condiciones_optimas")


def mostrar_estado_recursos(configuracion: dict) -> None:
    """TODO: imprimir el estado de agua y energía (actual/máximo)."""
    raise NotImplementedError("Implementa mostrar_estado_recursos")


def mostrar_estado_serre(serre: dict) -> None:
    """TODO: mostrar la información detallada de un invernadero.

    Sigue el formato exacto del juego original, incluyendo emojis y mensajes
    sobre temperatura, plantas en riesgo, etc.
    """
    raise NotImplementedError("Implementa mostrar_estado_serre")


def mostrar_informe_diario(configuracion: dict, dia: int) -> None:
    """TODO: imprimir el reporte completo del día, llamando a las funciones de apoyo."""
    raise NotImplementedError("Implementa mostrar_informe_diario")


def contar_plantas_vivas(configuracion: dict) -> tuple[int, int]:
    """TODO: contar cuántas plantas siguen vivas y el total inicial."""
    raise NotImplementedError("Implementa contar_plantas_vivas")


def mostrar_informe_final(configuracion: dict) -> None:
    """TODO: reutilizar contar_plantas_vivas y mostrar el resumen final."""
    raise NotImplementedError("Implementa mostrar_informe_final")


def ciclo_decision_jugador(configuracion: dict) -> None:
    """TODO: gestionar el bucle de entrada de comandos durante un día.

    Asegúrate de:
    - Mostrar los mensajes iniciales del turno.
    - Pedir comandos numerados.
    - Llamar a procesar_comando y mostrar la respuesta.
    - Detener el ciclo cuando se escriba "pasar" o se produzca KeyboardInterrupt.
    - Ignorar (pero avisar) cuando el comando esté vacío.
    """
    raise NotImplementedError("Implementa ciclo_decision_jugador")


def simular_dia(configuracion: dict, dia: int) -> None:
    """TODO: orquestar todas las etapas de un día de simulación.

    Secuencia esperada:
    1. Reiniciar la energía diaria al máximo.
    2. Generar y aplicar un evento climático si corresponde.
    3. Mostrar el informe del día.
    4. Actualizar la salud de las plantas.
    5. Ejecutar el ciclo de decisiones del jugador.
    6. Aplicar fluctuaciones naturales y evapotranspiración.
    """
    raise NotImplementedError("Implementa simular_dia")


def mostrar_introduccion_juego() -> None:
    """UI ya preparada: explica cómo jugar."""
    print("\n" + "🌿" * 20)
    print("BIENVENIDA A LAS GRANDES SERRES DU JARDIN DES PLANTES")
    print("🌿" * 20)
    print("\n🎯 OBJETIVO:")
    print("Mantén vivas el máximo número de plantas durante 10 días")
    print("\n🛠️ CÓMO JUGAR:")
    print("1. Cada día recibirás un reporte del estado de tus invernaderos")
    print("2. Analiza la temperatura, humedad y salud de las plantas")
    print("3. Ejecuta acciones para mejorar las condiciones")
    print("4. Gestiona tus recursos limitados de agua y energía")
    print("\n✨ CONSEJOS IMPORTANTES:")
    print("• Usa 'condiciones' para ver los requisitos óptimos de cada planta")
    print("• Usa 'ayuda' para recordar los comandos disponibles")
    print("• ¡La prevención es mejor que la curación!")
    print("\n" + "-" * 60)


def seleccionar_configuracion() -> dict | None:
    """UI ya preparada: menú para elegir dificultad."""
    print("🌿 BIENVENIDA A LAS GRANDES SERRES DU JARDIN DES PLANTES 🌿")
    print("=" * 60)
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil - 1 invernadero, 2 plantas, recursos generosos")
    print("2. Medio - 1 invernadero, 3 plantas, recursos balanceados")
    print("3. Difícil - 2 invernaderos, recursos ajustados")
    print("4. Salir")

    while True:
        try:
            opcion = input("\nIngrese su opción (1-4): ").strip()
            if opcion == "1":
                print("🟢 Dificultad FÁCIL seleccionada")
                return obtener_configuracion_facil()
            if opcion == "2":
                print("🟡 Dificultad MEDIA seleccionada")
                return obtener_configuracion_media()
            if opcion == "3":
                print("🔴 Dificultad DIFÍCIL seleccionada")
                return obtener_configuracion_dificil()
            if opcion == "4":
                print("👋 ¡Hasta pronto!")
                return None
            print("❌ Opción inválida. Ingrese 1, 2, 3 o 4.")
        except (ValueError, KeyboardInterrupt):
            print("❌ Entrada inválida. Intente nuevamente.")


def mostrar_ayuda() -> str:
    """UI ya preparada: ayuda de comandos."""
    return """
📚 COMANDOS DISPONIBLES:

🚿 RIEGO:
• regar <ID_PLANTA>          - Riega una planta específica hasta su nivel óptimo
  Formato: regar SAG01       - Las IDs aparecen en el reporte diario
  Costo: Variable según la cantidad de agua necesaria (1L por cada 10%)

🔥 CALEFACCIÓN:
• calefaccion <INVERNADERO>  - Aumenta temperatura (+2°C, -5% humedad)
  Formato: calefaccion Serre Des Cactus
  Costo: 5 kWh de energía diaria

💨 VENTILACIÓN:
• ventilacion <INVERNADERO>  - Reduce temperatura (-2°C, +5% humedad)
  Formato: ventilacion Serre Tropicale
  Costo: 3 kWh de energía diaria

⏭️ CONTROL:
• pasar                      - Termina tu turno y avanza al siguiente día
• ayuda                      - Muestra esta ayuda
• condiciones                - Muestra condiciones óptimas de todas las plantas

💡 CONSEJOS:
- Escribe los nombres de invernaderos EXACTAMENTE como aparecen en el reporte
- Las IDs de plantas son sensibles a mayúsculas/minúsculas
- Puedes usar múltiples comandos antes de escribir 'pasar'
- Revisa las condiciones óptimas con 'condiciones' para planificar mejor
"""


def jugar() -> None:
    """TODO: coordenar el flujo completo del juego empleando las funciones anteriores."""
    raise NotImplementedError("Implementa jugar")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    print("⚠️ Esta es solo una plantilla. Completa las funciones antes de jugar.")
    # Cuando todas las funciones estén implementadas, descomenta la línea:
    # jugar()
