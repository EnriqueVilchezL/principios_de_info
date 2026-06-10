# Practica de Examen 7

<head>
  <meta charset="UTF-8">
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
      }
    };
  </script>

  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>

## Contexto del Problema

La **Comisión Nacional de Emergencias (CNE)** de Costa Rica está implementando un prototipo para su **Sistema de Alerta Temprana de Incendios (SATI)**, enfocado en la protección de sus Parques Nacionales. Este sistema integra datos de focos de calor de diversas fuentes satelitales, como el **GOES-16 de la NASA/NOAA** y el **Sentinel-2 de la ESA**. 🛰️

Los datos satelitales llegan con información sobre el parque nacional donde se detectó cada foco de calor. Su tarea es consolidar estas detecciones, agruparlas por parque, calcular la intensidad promedio por parque, y determinar el nivel de riesgo basado en esta intensidad.

-----

## Objetivo General

Desarrollar un programa en **Python** que procese detecciones satelitales de focos de calor. El programa deberá:

1. Consolidar todas las detecciones de múltiples satélites
2. Agrupar las detecciones por parque nacional
3. Calcular la potencia promedio de cada parque
4. Determinar el nivel de riesgo según la intensidad promedio
5. Generar un reporte formateado en la consola

-----

## Modelo de Datos

### Datos de Entrada: Focos de Calor por Satélite

Recibirá los datos en un **diccionario**. Las claves son los nombres de los satélites y los valores son **listas de diccionarios**, donde cada diccionario es una detección individual.

* `focos_de_calor_brutos`: El diccionario principal de entrada.

### Formato del Diccionario de Detección (Individual)

* `id_deteccion`: Identificador único de la lectura.
* `region_geografica`: Nombre del Parque Nacional donde se detectó el foco.
* `potencia_mw`: Potencia Radiativa del Fuego (FRP) en Megawatts.
* `timestamp`: Fecha y hora de la detección.

### Lista de Parques Nacionales Monitoreados

Se le proporciona una lista con los nombres de los parques nacionales bajo vigilancia:

* `parques_monitoreados`: Lista con nombres de parques

-----

## Requisitos del Procesamiento y Análisis

### Consolidación y Agrupación de Datos

1. **Consolidación:** Extraiga todas las detecciones individuales de la estructura de diccionario anidada (que tiene múltiples satélites como claves).
2. **Agrupación por Parque:** Organice las detecciones agrupándolas por `region_geografica`. Deberá crear una estructura que permita acceder fácilmente a todas las detecciones de cada parque.

### Análisis de Peligrosidad por Parque

Con las detecciones agrupadas por parque:

1. **Potencia Promedio:** Para cada parque que tenga al menos una detección, calcule la **potencia promedio** (promedio de `potencia_mw` de todas sus detecciones).
2. **Determinación del Nivel de Riesgo:** Clasifique cada parque según su potencia promedio:
      * **ALTO**: potencia promedio $\geq 200$ MW
      * **MEDIO**: potencia promedio entre 100 y 199 MW (inclusive)
      * **BAJO**: potencia promedio $< 100$ MW
3. **Parque de Máxima Prioridad:** Identificar el parque con la **potencia promedio más alta**. 🔥

-----

## Datos de Entrada de Ejemplo con Código Base

```python
# --- Lista de parques nacionales monitoreados ---
parques_monitoreados = [
    'Parque Nacional Santa Rosa',
    'Parque Nacional Corcovado',
    'Parque Nacional Volcan Poas',
    'Parque Nacional Tortuguero',
]

# --- Datos de Detecciones Satelitales ---
focos_de_calor_brutos = {
    'GOES-16': [
        {'id_deteccion': 'G1-001', 'region_geografica': 'Parque Nacional Santa Rosa', 'potencia_mw': 200.0, 'timestamp': '2025-10-11T14:30:00Z'},
        {'id_deteccion': 'G1-002', 'region_geografica': 'Parque Nacional Corcovado', 'potencia_mw': 180.0, 'timestamp': '2025-10-11T14:32:00Z'},
        {'id_deteccion': 'G1-003', 'region_geografica': 'Parque Nacional Volcan Poas', 'potencia_mw': 50.0, 'timestamp': '2025-10-11T14:35:00Z'},
        {'id_deteccion': 'G1-004', 'region_geografica': 'Parque Nacional Tortuguero', 'potencia_mw': 100.0, 'timestamp': '2025-10-11T14:42:00Z'},
    ],
    'Sentinel-2': [
        {'id_deteccion': 'S2-001', 'region_geografica': 'Parque Nacional Tortuguero', 'potencia_mw': 120.0, 'timestamp': '2025-10-11T15:01:00Z'},
        {'id_deteccion': 'S2-002', 'region_geografica': 'Parque Nacional Tortuguero', 'potencia_mw': 150.0, 'timestamp': '2025-10-11T15:04:00Z'},
        {'id_deteccion': 'S2-003', 'region_geografica': 'Parque Nacional Corcovado', 'potencia_mw': 300.0, 'timestamp': '2025-10-11T15:10:00Z'},
    ]
}

# Puede usar esta funcion para imprimir el reporte final si lo desea
def imprimir_reporte(
    resumen_parques: dict,
    parque_maxima_prioridad: str
) -> None:
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
    print("Fecha del Reporte: 2025-10-11")
    
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

def main() -> None:
    """Ejecutar el flujo completo del sistema SATI."""
    # La idea es que aqui utilice los datos almacenados en las variables
    # **focos_de_calor_brutos** y **parques_monitoreados**
    # para realizar todo el procesamiento y analisis requerido.
    pass

# ===================================================================
# PUNTO DE ENTRADA
# ===================================================================

main()
```

-----

## Salida Esperada en Consola

```text
===================================================================
*** SATI: REPORTE DE ANÁLISIS DE FOCOS DE CALOR ***
===================================================================
Fecha del Reporte: 2025-10-11

--- PARQUE DE MÁXIMA PRIORIDAD ---

> Parque Nacional Corcovado
  - Potencia Promedio: 240.00 MW
  - Nivel de Riesgo: ALTO
  - Detecciones Asignadas: 2

--- RESUMEN POR PARQUE NACIONAL ---

> Parque Nacional Corcovado:
  - Detecciones: 2
  - Potencia Promedio: 240.00 MW
  - Nivel de Riesgo: ALTO

> Parque Nacional Santa Rosa:
  - Detecciones: 1
  - Potencia Promedio: 200.00 MW
  - Nivel de Riesgo: ALTO

> Parque Nacional Tortuguero:
  - Detecciones: 3
  - Potencia Promedio: 123.33 MW
  - Nivel de Riesgo: MEDIO

> Parque Nacional Volcán Poás:
  - Detecciones: 1
  - Potencia Promedio: 50.00 MW
  - Nivel de Riesgo: BAJO

===================================================================
*** Fin del Reporte ***
===================================================================
```
