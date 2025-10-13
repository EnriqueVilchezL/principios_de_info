from typing import List, Dict
import datetime
# --- Lista de parques nacionales monitoreados ---
parques_monitoreados = [
    "Parque Nacional Santa Rosa",
    "Parque Nacional Corcovado",
    "Parque Nacional Volcan Poas",
    "Parque Nacional Tortuguero",
]

# --- Datos de Detecciones Satelitales ---
focos_de_calor_brutos = {
    "GOES-16": [
        {
            "id_deteccion": "G1-001",
            "region_geografica": "Parque Nacional Santa Rosa",
            "potencia_mw": 200.0,
            "timestamp": "2025-10-11T14:30:00Z",
        },
        {
            "id_deteccion": "G1-002",
            "region_geografica": "Parque Nacional Corcovado",
            "potencia_mw": 180.0,
            "timestamp": "2025-10-11T14:32:00Z",
        },
        {
            "id_deteccion": "G1-003",
            "region_geografica": "Parque Nacional Volcan Poas",
            "potencia_mw": 50.0,
            "timestamp": "2025-10-11T14:35:00Z",
        },
        {
            "id_deteccion": "G1-004",
            "region_geografica": "Parque Nacional Tortuguero",
            "potencia_mw": 100.0,
            "timestamp": "2025-10-11T14:42:00Z",
        },
    ],
    "Sentinel-2": [
        {
            "id_deteccion": "S2-001",
            "region_geografica": "Parque Nacional Tortuguero",
            "potencia_mw": 120.0,
            "timestamp": "2025-10-11T15:01:00Z",
        },
        {
            "id_deteccion": "S2-002",
            "region_geografica": "Parque Nacional Tortuguero",
            "potencia_mw": 150.0,
            "timestamp": "2025-10-11T15:04:00Z",
        },
        {
            "id_deteccion": "S2-003",
            "region_geografica": "Parque Nacional Corcovado",
            "potencia_mw": 300.0,
            "timestamp": "2025-10-11T15:10:00Z",
        },
    ],
}


def agrupar_detecciones_por_parque(
    focos_brutos: Dict[str, List[Dict]],
    parques_monitoreados: List[str],
) -> Dict[str, List[Dict]]:
    # preparamos un diccionario con listas vacias para cada parque
    # aka: por cada parque, en los parques_monitoreados, creamos una llave con su nombre y una lista vacia como valor
    # posteriormente llenaremos estas listas con las detecciones correspondientes a cada parque
    detecciones_por_parque = {parque: [] for parque in parques_monitoreados}
    # no usamos la llave satelite para nada, entonces solo iteramos por las detecciones
    for detecciones in focos_brutos.values():
        for deteccion in detecciones:
            # agregamos la deteccion a la lista del parque correspondiente si el parque esta en la lista de monitoreo
            # caso contrario, la ignoramos, porque no nos interesa, al no estar en la lista de parques monitoreados
            if deteccion["region_geografica"] in detecciones_por_parque:
                detecciones_por_parque[deteccion["region_geografica"]].append(deteccion)
    return detecciones_por_parque


def calcular_promedio_de_potencia(detecciones: List[Dict]) -> float:
    # si no hay detecciones, el promedio es 0.0
    if len(detecciones) == 0 or not detecciones:
        return 0.0
    # hacemos una lista con todas las potencias y calculamos el promedio
    # aka: por cada deteccion en la lista de detecciones, sacamos su potencia y la ponemos en una nueva lista
    potencias = [d["potencia_mw"] for d in detecciones]
    # calculamos y retornamos el promedio
    return sum(potencias) / len(detecciones)


def determinar_nivel_de_riesgo(potencia_promedio: float) -> str:
    if potencia_promedio > 200.0:
        return "ALTO"
    elif 100.0 <= potencia_promedio:
        return "MEDIO"
    else:
        return "BAJO"


def calcular_resumen_por_parque(
    detecciones_por_parque: Dict[str, List[Dict]],
) -> Dict[str, Dict]:
    # preparamos el diccionario de resumen
    # aka: por cada llave en detecciones_por_parque, creamos un diccionario vacio como valor
    resumen = {parque: {} for parque in detecciones_por_parque.keys()}

    for parque, detecciones in detecciones_por_parque.items():
        potencia_promedio = calcular_promedio_de_potencia(detecciones)
        nivel_riesgo = determinar_nivel_de_riesgo(potencia_promedio)

        resumen[parque] = {
            "num_detecciones": len(detecciones),
            "potencia_promedio": potencia_promedio,
            "nivel_riesgo": nivel_riesgo,
        }

    return resumen

def obtener_parque_de_maxima_prioridad(resumen_parques: Dict[str, Dict]) -> str:
    parque_maxima_prioridad = None
    maxima_potencia_promedio = float('-inf')

    for parque, info in resumen_parques.items():
        if info['potencia_promedio'] > maxima_potencia_promedio:
            maxima_potencia_promedio = info['potencia_promedio']
            parque_maxima_prioridad = parque

    return parque_maxima_prioridad

# Puede usar esta funcion para imprimir el reporte final si lo desea
def imprimir_reporte(resumen_parques: dict, parque_maxima_prioridad: str) -> None:
    """Imprimir el reporte formateado en consola.

    Args:
        resumen_parques (dict): Informacion de cada parque con detecciones.
            Las claves son nombres de parques.
            Los valores son diccionarios con:
            - 'num_detecciones' (int): Cantidad de detecciones asignadas
            - 'potencia_promedio' (float): Potencia promedio en MW
            - 'nivel_riesgo' (str): 'ALTO', 'MEDIO' o 'BAJO'

            Ejemplo:
            {
                'Parque Nacional Corcovado': {
                    'num_detecciones': 2,
                    'potencia_promedio': 240.0,
                    'nivel_riesgo': 'ALTO'
                },
                ...
            }

        parque_maxima_prioridad (str): Nombre del parque con mayor potencia promedio.

    Returns:
        None
    """
    print("=" * 67)
    print("*** SATI: REPORTE DE ANALISIS DE FOCOS DE CALOR ***")
    print("=" * 67)
    print(f"Fecha del Reporte: {datetime.datetime.now().strftime('%Y-%m-%d')}")

    # Parque de maxima prioridad
    print("\n--- PARQUE DE MAXIMA PRIORIDAD ---")

    if parque_maxima_prioridad and parque_maxima_prioridad in resumen_parques:
        info = resumen_parques[parque_maxima_prioridad]
        print(f"\n> {parque_maxima_prioridad}")
        print(f"  - Potencia Promedio: {info['potencia_promedio']:.2f} MW")
        print(f"  - Nivel de Riesgo: {info['nivel_riesgo']}")
        print(f"  - Detecciones Asignadas: {info['num_detecciones']}")
    else:
        print("  - No hay detecciones")

    # Resumen por parque
    print("\n--- RESUMEN POR PARQUE NACIONAL ---")

    for nombre_parque in sorted(resumen_parques.keys()):
        info = resumen_parques[nombre_parque]
        print(f"\n> {nombre_parque}:")
        print(f"  - Detecciones: {info['num_detecciones']}")
        print(f"  - Potencia Promedio: {info['potencia_promedio']:.2f} MW")
        print(f"  - Nivel de Riesgo: {info['nivel_riesgo']}")

    print("\n" + "=" * 67)
    print("*** Fin del Reporte ***")
    print("=" * 67)


# ===================================================================
# FUNCION PRINCIPAL
# ===================================================================


def ejecutar_solucion() -> None:
    """Ejecutar el flujo completo del sistema SATI."""
    detecciones_agrupadas_por_parque = agrupar_detecciones_por_parque(
        focos_de_calor_brutos, parques_monitoreados
    )

    resumen_detecciones = calcular_resumen_por_parque(detecciones_agrupadas_por_parque)

    parque_maxima_prioridad = obtener_parque_de_maxima_prioridad(resumen_detecciones)

    imprimir_reporte(resumen_detecciones, parque_maxima_prioridad)


# ===================================================================
# PUNTO DE ENTRADA
# ===================================================================

if __name__ == "__main__":
    ejecutar_solucion()
