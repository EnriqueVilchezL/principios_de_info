"""
Simulación Interactiva de Gestión de Ecosistemas - Las Grandes Serres
=====================================================================

🎮 DESCRIPCIÓN DEL JUEGO:
Juego de simulación donde el jugador gestiona invernaderos botánicos
durante 10 días, manteniendo plantas vivas con recursos limitados.

📚 CONCEPTOS CLAVE DE PROGRAMACIÓN UTILIZADOS:
- Diccionarios anidados: para representar la estructura completa del juego
- Listas: para almacenar múltiples invernaderos y plantas
- Tuplas: para representar rangos óptimos (min, max)
- Bucles (for/while): para iterar sobre días, invernaderos y plantas
- Condicionales (if/elif/else): para validaciones y lógica de juego
- Funciones: modularización del código en funciones reutilizables
- Entrada/salida: interacción con el usuario mediante input() y print()

🗂️ ESTRUCTURA DE DATOS PRINCIPAL:
El juego usa un diccionario principal llamado 'configuracion' con esta estructura:
{
    "recursos_globales": {
        "tanque_agua_litros": float,      # Agua total disponible (no se renueva)
        "energia_diaria_max_kwh": float,  # Energía máxima por día
        "energia_diaria_kwh": float       # Energía disponible hoy (se renueva cada día)
    },
    "serres": [  # Lista de invernaderos
        {
            "nombre": str,
            "ambiente": {"temperatura": float, "humedad_relativa": float},
            "especie": str,
            "requerimientos": {
                "temperatura_optima": (min, max),      # Tupla
                "humedad_suelo_optima": (min, max),    # Tupla
                "k_T": float,  # Constante de estrés térmico
                "k_M": float   # Constante de estrés hídrico
            },
            "plantas": [  # Lista de plantas en este invernadero
                {
                    "id": str,
                    "humedad_suelo": float,
                    "salud": float,
                    "estado": str  # "viva" o "muerta"
                }
            ]
        }
    ]
}

📐 FÓRMULA MATEMÁTICA PRINCIPAL:
Cambio de salud diario: ΔH = -(k_T·ΔT² + k_M·ΔM²)
Donde:
- ΔT = desviación térmica (diferencia con temperatura óptima)
- ΔM = desviación hídrica (diferencia con humedad mínima óptima)
- k_T, k_M = constantes de sensibilidad de cada especie

⚙️ RESTRICCIONES:
Solo se permite importar random según las restricciones del ejercicio.

👨‍🎓 NOTA PARA ESTUDIANTES:
Este código está diseñado con comentarios educativos para facilitar la comprensión
de cómo funcionan las estructuras de datos fundamentales en Python. Se recomienda leer los
comentarios con atención y observar cómo los datos fluyen a través del programa.
"""

import random
from typing import Optional, Tuple


# =============================================================================
# CONSTANTES DEL JUEGO
# =============================================================================
# Las constantes son valores que NO cambian durante toda la ejecución del programa.
# Se escriben en MAYÚSCULAS por convención para identificarlas fácilmente.
# Usar constantes facilita ajustar el balance del juego sin buscar valores en todo el código.

# Duración y probabilidades
DIAS_SIMULACION = 10  # Total de días que dura la simulación
PROBABILIDAD_EVENTO_CLIMATICO = 0.15  # 15% de probabilidad de evento climático cada día

# Costos de acciones (recursos que consume cada acción)
COSTO_CALEFACCION_KWH = 5  # kWh de energía que cuesta activar calefacción
COSTO_VENTILACION_KWH = 3  # kWh de energía que cuesta activar ventilación
COSTO_RIEGO_LITROS_POR_10_PERCENT = 1  # Litros de agua por cada 10% de humedad a reponer

# Efectos de acciones sobre el ambiente
EFECTO_CALEFACCION_TEMP = 2.0  # °C que aumenta la temperatura con calefacción
EFECTO_VENTILACION_TEMP = -2.0  # °C que disminuye la temperatura con ventilación
EFECTO_CALEFACCION_HUMEDAD = -5.0  # % que reduce la humedad relativa la calefacción
EFECTO_VENTILACION_HUMEDAD = 5.0  # % que aumenta la humedad relativa la ventilación

# Parámetros ambientales y procesos naturales
RECUPERACION_SALUD_OPTIMA = 0.5  # Puntos de salud que recupera una planta en condiciones óptimas
TASA_EVAPOTRANSPIRACION_BASE = -4.0  # % de humedad que pierden las plantas normalmente
TASA_EVAPOTRANSPIRACION_AIRE_SECO = -6.0  # % de humedad que pierden con aire seco (<50% HR)
TASA_EVAPOTRANSPIRACION_AIRE_HUMEDO = -2.0  # % de humedad que pierden con aire húmedo (>80% HR)
FLUCTUACION_TEMPERATURA_MAX = 1.0  # °C de variación aleatoria diaria de temperatura
EVENTO_CLIMATICO_CAMBIO_TEMP = 4.0  # °C que cambia la temperatura por evento climático


# =============================================================================
# FUNCIONES DE INICIALIZACIÓN Y CONFIGURACIÓN
# =============================================================================


def obtener_configuracion_facil() -> dict:
    """
    Configuración de dificultad fácil con 1 invernadero y 2 plantas.

    Retorna:
        dict: Diccionario principal con la configuración completa del juego.
              Estructura:
              {
                  "recursos_globales": dict con llaves "tanque_agua_litros" (float),
                                       "energia_diaria_max_kwh" (float),
                                       "energia_diaria_kwh" (float),
                  "serres": lista de dicts, cada uno representa un invernadero
              }

              Ejemplo de invernadero:
              {
                  "nombre": str (ej: "Serre Tropicale"),
                  "ambiente": dict con "temperatura" (float) y "humedad_relativa" (float),
                  "especie": str (ej: "Orquídea Phalaenopsis"),
                  "requerimientos": dict con tuplas de rangos óptimos,
                  "plantas": lista de dicts con info de cada planta
              }
    """
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
    """
    Configuración de dificultad media con 1 invernadero y 3 plantas.

    Retorna:
        dict: Misma estructura que obtener_configuracion_facil() pero con
              menos recursos y plantas más exigentes.
    """
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
    """
    Configuración de dificultad difícil con 2 invernaderos y 4 plantas.

    Retorna:
        dict: Misma estructura que obtener_configuracion_facil() pero con
              2 invernaderos en la lista "serres" y recursos muy limitados.
    """
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


def mostrar_introduccion_juego():
    """
    Muestra las instrucciones iniciales del juego.

    Esta función no recibe parámetros ni retorna nada.
    Solo imprime en pantalla el texto de bienvenida.
    """
    # Crear una línea decorativa repitiendo el emoji 20 veces
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


def seleccionar_configuracion() -> Optional[dict]:
    """
    Permite a la persona jugadora seleccionar la dificultad del juego.

    Retorna:
        dict | None: Si selecciona opción 1-3, retorna dict de configuración.
                     Si selecciona opción 4 (Salir), retorna None.
                     La estructura del dict es la misma que obtener_configuracion_facil().
    """
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
            elif opcion == "2":
                print("🟡 Dificultad MEDIA seleccionada")
                return obtener_configuracion_media()
            elif opcion == "3":
                print("🔴 Dificultad DIFÍCIL seleccionada")
                return obtener_configuracion_dificil()
            elif opcion == "4":
                print("👋 ¡Hasta pronto!")
                return None
            else:
                print("❌ Opción inválida. Ingrese 1, 2, 3 o 4.")
        except (ValueError, KeyboardInterrupt):
            print("❌ Entrada inválida. Intente nuevamente.")


# =============================================================================
# FUNCIONES DE CÁLCULO DE SALUD Y ESTRÉS
# =============================================================================


def calcular_desviacion_termica(
    temperatura_actual: float, rango_optimo: Tuple[float, float]
) -> float:
    """
    Calcula la desviación térmica según las condiciones óptimas.

    Parámetros:
        temperatura_actual: float, temperatura en grados Celsius (ej: 27.5)
        rango_optimo: tupla de 2 floats (min, max), ej: (24.0, 30.0)

    Retorna:
        float: Desviación térmica ΔT
               - 0.0 si la temperatura está dentro del rango óptimo
               - Valor positivo indicando cuántos grados falta o sobra

    Ejemplo:
        calcular_desviacion_termica(22.0, (24.0, 30.0)) -> 2.0 (falta 2°C)
        calcular_desviacion_termica(27.0, (24.0, 30.0)) -> 0.0 (está OK)
    """
    # Desempaquetar la tupla en dos variables
    temp_min, temp_max = rango_optimo

    # Caso 1: La temperatura está en el rango óptimo -> no hay desviación
    if temp_min <= temperatura_actual <= temp_max:
        return 0.0
    # Caso 2: Hace demasiado frío -> calcular cuánto falta para llegar al mínimo
    elif temperatura_actual < temp_min:
        return temp_min - temperatura_actual
    # Caso 3: Hace demasiado calor -> calcular cuánto sobra del máximo
    else:  # temperatura_actual > temp_max
        return temperatura_actual - temp_max


def calcular_desviacion_hidrica(
    humedad_suelo_actual: float, rango_optimo: Tuple[float, float]
) -> float:
    """
    Calcula la desviación hídrica según las condiciones óptimas.

    Parámetros:
        humedad_suelo_actual: float, porcentaje de humedad (0-100), ej: 45.5
        rango_optimo: tupla de 2 floats (min, max), ej: (55.0, 75.0)

    Retorna:
        float: Desviación hídrica ΔM
               - 0.0 si la humedad está por encima del mínimo
               - Valor positivo indicando cuánta humedad falta

    Nota: Solo nos importa el mínimo, por eso usamos _ para ignorar el máximo.
    """
    # Desempaquetar solo el mínimo, ignorar el máximo con _
    humedad_min, _ = rango_optimo

    # Si tiene suficiente agua (≥ mínimo) -> no hay desviación
    if humedad_suelo_actual >= humedad_min:
        return 0.0
    # Si le falta agua (< mínimo) -> calcular cuánta falta
    else:
        return humedad_min - humedad_suelo_actual


def calcular_cambio_salud(planta: dict, ambiente: dict, requerimientos: dict) -> float:
    """
    Calcula el cambio diario en la salud de una planta.
    Implementa la fórmula: ΔH = -(k_T·ΔT² + k_M·ΔM²)

    Parámetros:
        planta: dict con llaves "id" (str), "humedad_suelo" (float),
                "salud" (float), "estado" (str: "viva" o "muerta")
                Ejemplo: {"id": "ORQ01", "humedad_suelo": 60.0, "salud": 85.0, "estado": "viva"}

        ambiente: dict con llaves "temperatura" (float) y "humedad_relativa" (float)
                  Ejemplo: {"temperatura": 27.0, "humedad_relativa": 75.0}

        requerimientos: dict con llaves "temperatura_optima" (tupla),
                        "humedad_suelo_optima" (tupla), "k_T" (float), "k_M" (float)
                        Ejemplo: {"temperatura_optima": (24, 30), "k_T": 0.12, ...}

    Retorna:
        float: Cambio en salud (puede ser positivo o negativo)
               - Positivo: la planta se recupera (+0.5 si está en condiciones óptimas)
               - Negativo: la planta pierde salud por estrés
    """
    # Si la planta ya murió, no hay cambios
    if planta["estado"] == "muerta":
        return 0.0

    # Calcular desviaciones usando las funciones auxiliares
    delta_t = calcular_desviacion_termica(
        ambiente["temperatura"], requerimientos["temperatura_optima"]
    )
    delta_m = calcular_desviacion_hidrica(
        planta["humedad_suelo"], requerimientos["humedad_suelo_optima"]
    )

    # Caso especial: Si está en condiciones óptimas, se recupera
    if delta_t == 0.0 and delta_m == 0.0:
        return RECUPERACION_SALUD_OPTIMA  # +0.5 puntos de salud

    # Caso general: Calcular daño por estrés usando la fórmula del enunciado
    # ΔH = -(k_T·ΔT² + k_M·ΔM²)
    k_t = requerimientos["k_T"]  # Constante de sensibilidad térmica
    k_m = requerimientos["k_M"]  # Constante de sensibilidad hídrica
    danio = -(k_t * (delta_t**2) + k_m * (delta_m**2))

    return danio  # Será un número negativo (pérdida de salud)


def actualizar_salud_plantas(configuracion: dict) -> None:
    """
    Actualiza la salud de todas las plantas en todos los invernaderos.

    Parámetros:
        configuracion: dict, el diccionario principal del juego con estructura:
                       {"recursos_globales": {...}, "serres": [...]}

    Esta función no retorna nada (None), pero modifica directamente
    los valores de "salud" y "estado" de las plantas dentro de configuracion.
    """
    # Lista para acumular las plantas que mueran durante la actualización
    plantas_muertas = []

    # Recorrer cada invernadero en la lista de invernaderos
    for serre in configuracion["serres"]:
        # Extraer los datos necesarios del invernadero actual
        ambiente = serre["ambiente"]
        requerimientos = serre["requerimientos"]

        # Recorrer cada planta dentro de este invernadero
        for planta in serre["plantas"]:
            # Solo procesar plantas vivas
            if planta["estado"] == "viva":
                # Calcular cuánto cambia la salud hoy
                cambio_salud = calcular_cambio_salud(planta, ambiente, requerimientos)

                # Actualizar la salud: sumar el cambio (puede ser + o -)
                # Usar max/min para mantener salud entre 0 y 100
                planta["salud"] = max(0.0, min(100.0, planta["salud"] + cambio_salud))

                # Verificar si la planta murió (salud llegó a 0 o menos)
                if planta["salud"] <= 0.0:
                    planta["estado"] = "muerta"  # Cambiar estado
                    # Guardar info para notificar después
                    plantas_muertas.append((serre["nombre"], planta["id"]))

    # Notificar al jugador sobre plantas que murieron hoy
    for nombre_serre, planta_id in plantas_muertas:
        print(f"💀 La planta {planta_id} en {nombre_serre} ha muerto.")


# =============================================================================
# FUNCIONES DE EVENTOS CLIMÁTICOS Y CAMBIOS AMBIENTALES
# =============================================================================


def generar_evento_climatico() -> str:
    """
    Genera un evento climático aleatorio.

    Retorna:
        str | None: "ola_frio" o "dia_soleado" si ocurre un evento (15% probabilidad)
                    None si no ocurre ningún evento (85% probabilidad)
    """
    # Generar un número aleatorio entre 0 y 1
    if random.random() < PROBABILIDAD_EVENTO_CLIMATICO:  # 15% de probabilidad
        # Si ocurre evento, elegir uno al azar de la lista
        eventos = ["ola_frio", "dia_soleado"]
        return random.choice(eventos)
    # Si no ocurre evento, retornar None
    return None


def aplicar_evento_climatico(configuracion: dict, evento: str) -> None:
    """
    Aplica un evento climático a todos los invernaderos.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        evento: str, puede ser "ola_frio" o "dia_soleado"

    Esta función modifica la temperatura de todos los invernaderos.
    """
    if evento == "ola_frio":
        # Informar al jugador sobre el evento
        print(f"🥶 EVENTO CLIMÁTICO: Ola de frío (-{EVENTO_CLIMATICO_CAMBIO_TEMP}°C)")
        # Aplicar reducción de temperatura a todos los invernaderos
        for serre in configuracion["serres"]:
            serre["ambiente"]["temperatura"] -= EVENTO_CLIMATICO_CAMBIO_TEMP
    elif evento == "dia_soleado":
        # Informar al jugador sobre el evento
        print(f"☀️ EVENTO CLIMÁTICO: Día soleado intenso (+{EVENTO_CLIMATICO_CAMBIO_TEMP}°C)")
        # Aplicar aumento de temperatura a todos los invernaderos
        for serre in configuracion["serres"]:
            serre["ambiente"]["temperatura"] += EVENTO_CLIMATICO_CAMBIO_TEMP


def aplicar_fluctuacion_diaria(configuracion: dict) -> None:
    """
    Aplica fluctuaciones aleatorias de temperatura.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Simula la variación natural de temperatura añadiendo un valor
    aleatorio entre -1°C y +1°C a cada invernadero.
    """
    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        # Generar un número aleatorio entre -1.0 y +1.0
        fluctuacion = random.uniform(-FLUCTUACION_TEMPERATURA_MAX, FLUCTUACION_TEMPERATURA_MAX)
        # Añadir la fluctuación a la temperatura actual
        serre["ambiente"]["temperatura"] += fluctuacion


def aplicar_evapotranspiracion(configuracion: dict) -> None:
    """
    Aplica la evapotranspiración a todas las plantas.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    La evapotranspiración es la pérdida de agua por evaporación del suelo.
    La tasa de pérdida depende de la humedad del aire:
    - Aire seco (< 50%): pérdida rápida (-6% humedad suelo)
    - Aire normal (50-80%): pérdida media (-4% humedad suelo)
    - Aire húmedo (> 80%): pérdida lenta (-2% humedad suelo)
    """
    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        # Obtener la humedad relativa del aire de este invernadero
        humedad_relativa = serre["ambiente"]["humedad_relativa"]

        # Determinar tasa de evapotranspiración según humedad del aire
        if humedad_relativa < 50:
            # Aire seco: las plantas pierden agua más rápido
            tasa = TASA_EVAPOTRANSPIRACION_AIRE_SECO  # -6.0
        elif humedad_relativa > 80:
            # Aire húmedo: las plantas pierden agua más lento
            tasa = TASA_EVAPOTRANSPIRACION_AIRE_HUMEDO  # -2.0
        else:
            # Aire normal: tasa estándar
            tasa = TASA_EVAPOTRANSPIRACION_BASE  # -4.0

        # Aplicar la tasa a todas las plantas vivas del invernadero
        for planta in serre["plantas"]:
            if planta["estado"] == "viva":
                # Reducir humedad del suelo (tasa es negativa)
                # Usar max(0.0, ...) para evitar valores negativos
                planta["humedad_suelo"] = max(0.0, planta["humedad_suelo"] + tasa)


# =============================================================================
# FUNCIONES DE ACCIONES DE La PERSONA JUGADORA
# =============================================================================


def buscar_planta_por_id(configuracion: dict, planta_id: str) -> Tuple:
    """
    Busca una planta por su ID en todos los invernaderos.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        planta_id: str, identificador de la planta (ej: "ORQ01")

    Retorna:
        tuple: (serre, planta) si encuentra la planta
               - serre: dict del invernadero que contiene la planta
               - planta: dict con los datos de la planta
               (None, None) si no encuentra la planta
    """
    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        # Recorrer cada planta en este invernadero
        for planta in serre["plantas"]:
            # Si encontramos la planta buscada, retornar ambos
            if planta["id"] == planta_id:
                return serre, planta
    # Si no se encontró, retornar None, None
    return None, None


def buscar_serre_por_nombre(configuracion: dict, nombre_serre: str) -> dict:
    """
    Busca un invernadero por su nombre.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        nombre_serre: str, nombre del invernadero (ej: "Serre Tropicale")

    Retorna:
        dict: Diccionario del invernadero si lo encuentra
        None: Si no encuentra el invernadero

    Nota: La comparación ignora mayúsculas/minúsculas usando .lower()
    """
    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        # Comparar nombres en minúsculas para evitar problemas de mayúsculas
        if serre["nombre"].lower() == nombre_serre.lower():
            return serre
    # Si no se encontró, retornar None
    return None


def calcular_costo_riego(planta: dict, requerimientos: dict) -> float:
    """
    Calcula el costo de agua para regar una planta hasta el óptimo.

    Parámetros:
        planta: dict con datos de la planta (debe tener "humedad_suelo")
        requerimientos: dict con "humedad_suelo_optima" (tupla min, max)

    Retorna:
        float: Litros de agua necesarios
               - 0.0 si la planta ya tiene suficiente agua
               - Cantidad calculada según: 1 litro por cada 10% de diferencia

    Ejemplo:
        Planta con 40% humedad, óptimo (55, 75)
        Diferencia: 75 - 40 = 35%
        Costo: (35 / 10) * 1 = 3.5 litros
    """
    # Extraer el valor máximo óptimo (ignoramos el mínimo con _)
    _, humedad_max_optima = requerimientos["humedad_suelo_optima"]
    humedad_actual = planta["humedad_suelo"]

    # Si ya tiene suficiente agua, no cuesta nada
    if humedad_actual >= humedad_max_optima:
        return 0.0

    # Calcular cuánta humedad falta para llegar al máximo
    diferencia_porcentaje = humedad_max_optima - humedad_actual
    # Calcular costo: 1 litro por cada 10% de diferencia
    costo_agua = (diferencia_porcentaje / 10.0) * COSTO_RIEGO_LITROS_POR_10_PERCENT
    return costo_agua


def ejecutar_riego(configuracion: dict, planta_id: str) -> Tuple[bool, str]:
    """
    Ejecuta la acción de riego en una planta específica.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        planta_id: str, ID de la planta a regar (ej: "ORQ01")

    Retorna:
        tuple[bool, str]: (exito, mensaje)
        - exito: True si se regó exitosamente, False si hubo error
        - mensaje: Descripción de lo que ocurrió

    Efectos si tiene éxito:
        - Reduce el agua del tanque global
        - Aumenta humedad_suelo de la planta al máximo óptimo
    """
    # Buscar la planta en todos los invernaderos
    serre, planta = buscar_planta_por_id(configuracion, planta_id)

    # Validación 1: Verificar si la planta existe
    if not serre or not planta:
        return False, f"❌ Planta {planta_id} no encontrada."

    # Validación 2: Verificar si la planta está viva
    if planta["estado"] == "muerta":
        return False, f"❌ La planta {planta_id} está muerta."

    # Calcular cuánta agua se necesita
    costo_agua = calcular_costo_riego(planta, serre["requerimientos"])

    # Validación 3: Verificar si ya tiene suficiente agua
    if costo_agua == 0:
        return False, f"❌ La planta {planta_id} ya tiene suficiente agua."

    # Validación 4: Verificar si hay suficiente agua en el tanque
    if configuracion["recursos_globales"]["tanque_agua_litros"] < costo_agua:
        return (
            False,
            f"❌ Agua insuficiente para regar {planta_id} (necesita {costo_agua:.1f}L).",
        )

    # Ejecutar el riego
    # 1. Restar agua del tanque global
    configuracion["recursos_globales"]["tanque_agua_litros"] -= costo_agua
    # 2. Llenar la humedad del suelo al máximo óptimo
    _, humedad_max_optima = serre["requerimientos"]["humedad_suelo_optima"]
    planta["humedad_suelo"] = humedad_max_optima

    return True, f"✅ Planta {planta_id} regada (costo: {costo_agua:.1f}L)."


def ejecutar_calefaccion(configuracion: dict, nombre_serre: str) -> Tuple[bool, str]:
    """
    Ejecuta la acción de calefacción en un invernadero.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        nombre_serre: str, nombre del invernadero (ej: "Serre Tropicale")

    Retorna:
        tuple[bool, str]: (exito, mensaje)

    Efectos si tiene éxito:
        - Efecto primario: Aumenta temperatura +2°C
        - Efecto secundario: Reduce humedad relativa -5%
        - Consume 5 kWh de energía diaria
    """
    # Buscar el invernadero por nombre
    serre = buscar_serre_por_nombre(configuracion, nombre_serre)

    # Validación 1: Verificar si el invernadero existe
    if not serre:
        return False, f"❌ Invernadero '{nombre_serre}' no encontrado."

    # Validación 2: Verificar si hay suficiente energía
    if configuracion["recursos_globales"]["energia_diaria_kwh"] < COSTO_CALEFACCION_KWH:
        return (
            False,
            f"❌ Energía insuficiente para calefacción (necesita {COSTO_CALEFACCION_KWH}kWh).",
        )

    # Ejecutar calefacción
    # 1. Restar energía
    configuracion["recursos_globales"]["energia_diaria_kwh"] -= COSTO_CALEFACCION_KWH
    # 2. Efecto primario: aumentar temperatura
    serre["ambiente"]["temperatura"] += EFECTO_CALEFACCION_TEMP
    # 3. Efecto secundario: reducir humedad relativa (mínimo 0%)
    serre["ambiente"]["humedad_relativa"] = max(
        0.0, serre["ambiente"]["humedad_relativa"] + EFECTO_CALEFACCION_HUMEDAD
    )

    return (
        True,
        f"✅ Calefacción activada en {serre['nombre']} (costo: {COSTO_CALEFACCION_KWH}kWh).",
    )


def ejecutar_ventilacion(configuracion: dict, nombre_serre: str) -> Tuple[bool, str]:
    """
    Ejecuta la acción de ventilación en un invernadero.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        nombre_serre: str, nombre del invernadero (ej: "Serre Tropicale")

    Retorna:
        tuple[bool, str]: (exito, mensaje)

    Efectos si tiene éxito:
        - Efecto primario: Reduce temperatura -2°C
        - Efecto secundario: Aumenta humedad relativa +5%
        - Consume 3 kWh de energía diaria
    """
    # Buscar el invernadero por nombre
    serre = buscar_serre_por_nombre(configuracion, nombre_serre)

    # Validación 1: Verificar si el invernadero existe
    if not serre:
        return False, f"❌ Invernadero '{nombre_serre}' no encontrado."

    # Validación 2: Verificar si hay suficiente energía
    if configuracion["recursos_globales"]["energia_diaria_kwh"] < COSTO_VENTILACION_KWH:
        return (
            False,
            f"❌ Energía insuficiente para ventilación (necesita {COSTO_VENTILACION_KWH}kWh).",
        )

    # Ejecutar ventilación
    # 1. Restar energía
    configuracion["recursos_globales"]["energia_diaria_kwh"] -= COSTO_VENTILACION_KWH
    # 2. Efecto primario: reducir temperatura
    serre["ambiente"]["temperatura"] += EFECTO_VENTILACION_TEMP  # -2.0
    # 3. Efecto secundario: aumentar humedad relativa (máximo 100%)
    serre["ambiente"]["humedad_relativa"] = min(
        100.0, serre["ambiente"]["humedad_relativa"] + EFECTO_VENTILACION_HUMEDAD
    )

    return (
        True,
        f"✅ Ventilación activada en {serre['nombre']} (costo: {COSTO_VENTILACION_KWH}kWh).",
    )


def procesar_comando(configuracion: dict, comando: str) -> Tuple[bool, str]:
    """
    Procesa un comando del jugador y ejecuta la acción correspondiente.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        comando: str, texto ingresado por el usuario (ej: "regar ORQ01")

    Retorna:
        tuple[bool, str]: (exito, mensaje)

    Comandos soportados:
        - "regar <ID>" -> ejecuta riego
        - "calefaccion <nombre>" -> ejecuta calefacción
        - "ventilacion <nombre>" -> ejecuta ventilación
        - "pasar" -> termina el turno
        - "ayuda" -> muestra ayuda
        - "condiciones" -> muestra condiciones óptimas
    """
    # Limpiar espacios y separar el comando en palabras
    partes = comando.strip().lower().split()

    # Validar que no esté vacío
    if not partes:
        return False, "❌ Comando vacío."

    # La primera palabra es la acción
    accion = partes[0]

    # Procesar según la acción
    if accion == "regar" and len(partes) == 2:
        # Extraer ID de planta y convertir a mayúsculas
        # el id tiene que estar en mayúsculas para coincidir
        # con como son los ids de las plantas en la configuración
        planta_id = partes[1].upper()
        return ejecutar_riego(configuracion, planta_id)

    elif accion == "calefaccion" and len(partes) >= 2:
        # Unir todas las palabras después de "calefaccion" y capitalizar
        # aquí usamos title() para poner mayúscula inicial en cada palabra
        # usamos " ".join(partes[1:]) para unir todas las palabras
        # el partes[1:] toma desde la segunda palabra hasta el final
        nombre_serre = " ".join(partes[1:]).title()
        return ejecutar_calefaccion(configuracion, nombre_serre)

    elif accion == "ventilacion" and len(partes) >= 2:
        # Unir todas las palabras después de "ventilacion" y capitalizar
        nombre_serre = " ".join(partes[1:]).title()
        return ejecutar_ventilacion(configuracion, nombre_serre)

    elif accion == "pasar":
        return True, "✅ Turno terminado."

    elif accion == "ayuda":
        return True, mostrar_ayuda()

    elif accion == "condiciones":
        return True, mostrar_condiciones_optimas(configuracion)

    else:
        return (
            False,
            "❌ Comando no reconocido. Use 'ayuda' para ver comandos disponibles.",
        )


# =============================================================================
# FUNCIONES DE INTERFAZ Y REPORTES
# =============================================================================


def mostrar_ayuda() -> str:
    """
    Muestra la ayuda de comandos disponibles.

    Retorna:
        str: Texto con todos los comandos y cómo usarlos
    """
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


def mostrar_condiciones_optimas(configuracion: dict) -> str:
    """
    Muestra las condiciones óptimas para todas las plantas.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Retorna:
        str: Texto formateado con las condiciones óptimas de cada invernadero
    """
    info = "\n🌱 CONDICIONES ÓPTIMAS POR INVERNADERO:\n"
    info += "=" * 50 + "\n"

    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        info += f"\n🏠 {serre['nombre']}\n"
        info += f"   Especie: {serre['especie']}\n"

        # Extraer rangos óptimos
        temp_min, temp_max = serre["requerimientos"]["temperatura_optima"]
        humid_min, humid_max = serre["requerimientos"]["humedad_suelo_optima"]

        info += f"   🌡️ Temperatura óptima: {temp_min}°C - {temp_max}°C\n"
        info += f"   💧 Humedad suelo óptima: {humid_min}% - {humid_max}%\n"

        # Mostrar temperatura actual y si está en rango
        temp_actual = serre["ambiente"]["temperatura"]
        if temp_min <= temp_actual <= temp_max:
            info += f"   ✅ Temperatura actual: {temp_actual:.1f}°C (ÓPTIMA)\n"
        else:
            info += f"   ⚠️ Temperatura actual: {temp_actual:.1f}°C (FUERA DE RANGO)\n"

        # Mostrar plantas y sus niveles
        plantas_vivas = [p for p in serre["plantas"] if p["estado"] == "viva"]
        info += f"   🌿 Plantas: {', '.join(p['id'] for p in plantas_vivas)}\n"

    return info


def mostrar_estado_recursos(configuracion: dict) -> None:
    """
    Muestra el estado actual de los recursos.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Imprime en pantalla los recursos disponibles (agua y energía).
    """
    recursos = configuracion["recursos_globales"]
    print(f"💧 Agua: {recursos['tanque_agua_litros']:.1f}L")
    energia_max = recursos.get("energia_diaria_max_kwh", recursos["energia_diaria_kwh"])
    print(f"⚡ Energía diaria: {recursos['energia_diaria_kwh']:.1f}/{energia_max:.1f}kWh")


def mostrar_estado_serre(serre: dict) -> None:
    """
    Muestra el estado detallado de un invernadero.

    Parámetros:
        serre: dict con estructura de invernadero
               {"nombre": str, "ambiente": dict, "especie": str,
                "requerimientos": dict, "plantas": list}

    Imprime información del ambiente y estado de cada planta.
    """
    print(f"\n🏠 {serre['nombre']} - {serre['especie']}")

    # Información ambiental actual
    temp_actual = serre["ambiente"]["temperatura"]
    humedad_rel = serre["ambiente"]["humedad_relativa"]
    print(f"   🌡️ Temperatura: {temp_actual:.1f}°C")
    print(f"   💨 Humedad relativa: {humedad_rel:.1f}%")

    # Condiciones óptimas para referencia
    temp_min, temp_max = serre["requerimientos"]["temperatura_optima"]
    humid_min, humid_max = serre["requerimientos"]["humedad_suelo_optima"]

    # Indicar si temperatura está en rango óptimo
    if temp_min <= temp_actual <= temp_max:
        print(f"   ✅ Temperatura óptima: {temp_min}-{temp_max}°C (CUMPLIDA)")
    else:
        # Determinar si necesita calefacción o ventilación
        if temp_actual < temp_min:
            print(f"   🥶 Temperatura óptima: {temp_min}-{temp_max}°C (NECESITA CALEFACCIÓN)")
        else:
            print(f"   🔥 Temperatura óptima: {temp_min}-{temp_max}°C (NECESITA VENTILACIÓN)")

    # Filtrar plantas vivas y encontrar casos críticos
    plantas_vivas = [p for p in serre["plantas"] if p["estado"] == "viva"]
    plantas_criticas = [p for p in plantas_vivas if p["salud"] < 50.0]
    plantas_secas = [p for p in plantas_vivas if p["humedad_suelo"] < humid_min]

    print(f"   🌱 Plantas vivas: {len(plantas_vivas)}/{len(serre['plantas'])}")

    # Alertas especiales
    if plantas_criticas:
        print(f"   🆘 SALUD CRÍTICA: {', '.join(p['id'] for p in plantas_criticas)}")

    if plantas_secas:
        print(f"   🚿 NECESITAN RIEGO: {', '.join(p['id'] for p in plantas_secas)}")

    print(f"   💧 Rango humedad suelo óptimo: {humid_min}-{humid_max}%")

    # Mostrar cada planta viva individualmente
    for planta in plantas_vivas:
        # Determinar emoji de estado de salud
        estado_salud = "🆘" if planta["salud"] < 50 else "⚠️" if planta["salud"] < 80 else "✅"
        # Determinar emoji de estado de agua
        estado_agua = "🚿" if planta["humedad_suelo"] < humid_min else "✅"
        print(
            f"      {estado_salud}{estado_agua} {planta['id']}: Salud {planta['salud']:.1f}%, "
            f"Humedad suelo {planta['humedad_suelo']:.1f}%"
        )


def mostrar_informe_diario(configuracion: dict, dia: int) -> None:
    """
    Muestra el informe completo del estado diario.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        dia: int, número del día actual (1-10)

    Imprime un reporte completo con recursos, estado de invernaderos y plantas.
    """
    print("\n" + "=" * 60)
    print(f"📅 DÍA {dia}/{DIAS_SIMULACION} - REPORTE DE ESTADO")
    print("=" * 60)

    # Mostrar recursos disponibles
    mostrar_estado_recursos(configuracion)

    # Mostrar estado de cada invernadero
    for serre in configuracion["serres"]:
        mostrar_estado_serre(serre)

    # Pie de página con información útil
    print("\n" + "=" * 60)
    print("💡 LEYENDA: ✅=Óptimo | ⚠️=Precaución | 🆘=Crítico | 🚿=Necesita riego")
    print("📋 Comandos útiles: 'ayuda' - 'condiciones' - 'pasar'")
    print("-" * 60)


def contar_plantas_vivas(configuracion: dict) -> Tuple[int, int]:
    """
    Cuenta el total de plantas vivas en toda la simulación.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Retorna:
        tuple[int, int]: (plantas_vivas, total_plantas)
        - plantas_vivas: cantidad de plantas con estado "viva"
        - total_plantas: cantidad total de plantas en todos los invernaderos
    """
    total_vivas = 0
    total_plantas = 0

    # Recorrer cada invernadero
    for serre in configuracion["serres"]:
        # Recorrer cada planta
        for planta in serre["plantas"]:
            total_plantas += 1
            if planta["estado"] == "viva":
                total_vivas += 1

    return total_vivas, total_plantas


def mostrar_informe_final(configuracion: dict) -> None:
    """
    Muestra el informe final de la simulación.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Calcula y muestra:
    - Cantidad de plantas supervivientes
    - Porcentaje de supervivencia
    - Agua restante
    - Calificación del desempeño
    """
    # Contar resultados
    vivas, total = contar_plantas_vivas(configuracion)
    porcentaje = (vivas / total) * 100 if total > 0 else 0

    print("\n" + "🌿" * 20)
    print("INFORME FINAL DE LAS GRANDES SERRES")
    print("🌿" * 20)
    print(f"📊 Plantas supervivientes: {vivas}/{total} ({porcentaje:.1f}%)")
    print(f"💧 Agua restante: {configuracion['recursos_globales']['tanque_agua_litros']:.1f}L")

    # Clasificar rendimiento según porcentaje de supervivencia
    if porcentaje >= 90:
        print("🏆 ¡EXCELENTE! Eres un maestro botánico.")
    elif porcentaje >= 75:
        print("🥈 ¡MUY BIEN! Buen trabajo como director.")
    elif porcentaje >= 50:
        print("🥉 ACEPTABLE. Podrías mejorar la gestión.")
    else:
        print("💔 DESASTROSO. Las plantas necesitaban mejor cuidado.")

    print("🌿" * 20 + "\n")


# =============================================================================
# FUNCIÓN PRINCIPAL DE JUEGO
# =============================================================================


def ciclo_decision_jugador(configuracion: dict) -> None:
    """
    Maneja el ciclo de decisiones del jugador durante un día.

    Parámetros:
        configuracion: dict, diccionario principal del juego

    Esta función ejecuta un bucle interactivo donde:
    1. Solicita comandos al jugador uno por uno
    2. Procesa y ejecuta cada comando
    3. Termina cuando el jugador escribe "pasar"

    El bucle es infinito (while True) y solo se rompe con "pasar" o interrupción.
    """
    print("\n🎮 ES TU TURNO - GESTIONA TUS INVERNADEROS")
    print("Escribe tus comandos uno por uno. Escribe 'pasar' cuando termines.")
    print("💡 TIP: Usa 'ayuda' para ver comandos o 'condiciones' para ver requisitos óptimos")

    comando_numero = 1  # Contador para enumerar los comandos

    # Bucle infinito que solo termina con 'pasar' o interrupción
    while True:
        try:
            # Pedir comando al usuario
            comando = input(f"👤 Comando #{comando_numero} > ").strip()

            # Validar que no esté vacío
            if not comando:
                print("⚠️ Comando vacío. Escribe 'ayuda' si necesitas información.")
                continue  # Volver al inicio del bucle sin incrementar contador

            # Procesar el comando
            exito, mensaje = procesar_comando(configuracion, comando)
            print(mensaje)  # Mostrar resultado

            # Si el comando fue "pasar", salir del bucle
            if comando.lower() == "pasar":
                print("⏭️ Terminando turno y avanzando al siguiente día...")
                break  # Salir del while

            # Incrementar contador solo si fue un comando de acción exitoso
            # (no cuenta ayuda ni condiciones)
            if exito and comando.lower() not in ["ayuda", "condiciones"]:
                comando_numero += 1

        except KeyboardInterrupt:
            # Si el usuario presiona Ctrl+C, terminar el día
            print("\n🔄 Juego interrumpido. Finalizando día...")
            break
        except Exception as e:
            print(f"❌ Error procesando comando: {e}")
            print("💡 Intenta escribir 'ayuda' para ver los comandos disponibles.")


def simular_dia(configuracion: dict, dia: int) -> None:
    """
    Simula un día completo del juego.

    Parámetros:
        configuracion: dict, diccionario principal del juego
        dia: int, número del día actual (1-10)

    ORDEN DE EJECUCIÓN (según especificaciones del enunciado):
    1. Inicio del día: reiniciar energía diaria
    2. Evento climático: posible ola de frío o día soleado
    3. Mostrar informe: recursos y estado de plantas
    4. Actualizar salud: aplicar fórmula de daño/recuperación
    5. Ciclo de jugador: recibir y ejecutar acciones
    6. Cambios pasivos: fluctuación de temperatura y evapotranspiración
    """
    # PASO 1: Inicio del día - Reiniciar energía diaria al máximo
    recursos = configuracion["recursos_globales"]
    energia_max = recursos.get("energia_diaria_max_kwh", recursos["energia_diaria_kwh"])
    recursos["energia_diaria_max_kwh"] = energia_max
    recursos["energia_diaria_kwh"] = energia_max

    # PASO 2: Evento climático al inicio (15% probabilidad)
    evento = generar_evento_climatico()
    if evento:
        aplicar_evento_climatico(configuracion, evento)

    # PASO 3: Mostrar informe del día
    mostrar_informe_diario(configuracion, dia)

    # PASO 4: Actualizar salud de plantas (antes de que el jugador actúe)
    actualizar_salud_plantas(configuracion)

    # PASO 5: Ciclo de decisión del jugador (interactivo)
    ciclo_decision_jugador(configuracion)

    # PASO 6: Cambios naturales pasivos (después de las acciones del jugador)
    aplicar_fluctuacion_diaria(configuracion)
    aplicar_evapotranspiracion(configuracion)


def jugar() -> None:
    """
    Función principal que ejecuta todo el juego.

    Esta es la función que coordina toda la simulación:
    1. Muestra la introducción
    2. Permite seleccionar dificultad
    3. Ejecuta el bucle principal de 10 días
    4. Muestra el informe final

    No recibe parámetros ni retorna nada.
    """
    # Mostrar introducción y bienvenida
    mostrar_introduccion_juego()

    # Seleccionar configuración (fácil, media o difícil)
    configuracion = seleccionar_configuracion()
    # Si el jugador elige "Salir" (opción 4), retornar None y terminar
    if not configuracion:
        return

    print(f"\n🚀 ¡Iniciando simulación de {DIAS_SIMULACION} días!")
    print("🎯 Objetivo: Mantener vivas el máximo número de plantas.")

    # Ejecutar simulación día por día (bucle principal del juego)
    for dia in range(1, DIAS_SIMULACION + 1):
        simular_dia(configuracion, dia)

        # Verificar condición de derrota: todas las plantas murieron
        vivas, _ = contar_plantas_vivas(configuracion)
        if vivas == 0:
            print("\n💀 Todas las plantas han muerto. Juego terminado.")
            break  # Salir del bucle antes de completar los 10 días

    # Mostrar informe final con estadísticas y calificación
    mostrar_informe_final(configuracion)


# =============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================================
# Este bloque se ejecuta SOLO cuando se ejecuta este archivo directamente.
# Si se importara este archivo desde otro programa, este bloque NO se ejecutaría.
# Es una buena práctica en Python para definir el punto de inicio del programa.

if __name__ == "__main__":
    jugar()  # Llamar a la función principal que inicia el juego
