# Práctica de exámen: Análisis de Datos de Estaciones Meteorológicas del IMN

-----

## Contexto del Problema

El **Instituto Meteorológico Nacional (IMN)** de Costa Rica opera una red de estaciones automáticas que recopilan datos climáticos cruciales de todo el país. Estos datos son fundamentales para el pronóstico del tiempo, la investigación climática y la toma de decisiones en sectores como la agricultura y la gestión de emergencias.

Como parte de la modernización de sus sistemas, el IMN necesita un prototipo en Python para procesar los datos crudos que envían estas estaciones. El sistema debe ser capaz de validar la información, calcular estadísticas vitales y generar reportes consolidados para el personal de meteorología.

-----

## Objetivo General del Ejercicio

Desarrollar un programa en Python que procese una lista de registros de datos meteorológicos. El programa deberá validar y limpiar los datos, y luego, generar una serie de reportes analíticos formateados que se imprimirán directamente en la consola.

-----

## 1\. Modelo de Datos

Usted recibirá los datos de cada una de las estaciones. Esta es una lista cuyos elementos representan una única lectura de una estación en un momento específico. Sin embargo, los datos pueden contener errores o valores fuera de rango.

### Datos de Referencia de Estaciones

Adicionalmente, se le proporcionará un diccionario con la información de cada estación meteorológica.

- **`info_estaciones`**: Un diccionario que mapea el código de la estación a una tupla con su `(provincia, altitud_msnm)`.

### Formato del Diccionario de Lectura (Datos Brutos)

- **`id_lectura`**: Un identificador único del registro (cadena de caracteres).
- **`estacion`**: Código de la estación meteorológica (cadena de caracteres).
- **`timestamp`**: Hora de la lectura en formato 24h (cadena de caracteres, e.g., `'14:30'`).
- **`temperatura_celsius`**: Temperatura registrada (puede ser un número o una cadena).
- **`humedad_relativa`**: Porcentaje de humedad (flotante entre 0.0 y 100.0).
- **`precipitacion_mm`**: Lluvia acumulada en la última hora en milímetros (número positivo).
- **`estado_sensor`**: Estado reportado por el sensor (cadena de caracteres, e.g., `'OPERATIVO'`, `'ERROR'`).

-----

## 2\. Requisitos Funcionales y Modularización

Para garantizar un diseño ordenado y modular, su programa deberá estar descompuesto en las siguientes funciones, las cuales usted debe implementar.

### Función 1: `validar_y_limpiar_lecturas(lecturas_brutas, estaciones_validas)`

**Parámetros:**

- `lecturas_brutas`: La lista de diccionarios con los datos sin procesar.
- `estaciones_validas`: El diccionario `info_estaciones` para referencia.

**Lógica:**

- Debe iterar sobre cada diccionario de la lista de entrada.

- Para cada lectura, realice las siguientes validaciones **en orden**:

    1. **Validación de Estación y Sensor**:

          - Verifique que el código de la `estacion` exista como clave en el diccionario `estaciones_validas`.
          - Verifique que el `estado_sensor` sea exactamente `'OPERATIVO'`.
          - Si alguna de estas condiciones no se cumple, la lectura debe ser descartada.

    2. **Validación de Tipos y Rangos**:

          - Convierta `temperatura_celsius` a flotante. Si la conversión falla (e.g., no es un número), descarte la lectura. (Use `try-except`).
          - Valide que la `temperatura_celsius` esté en un rango realista, por ejemplo, entre -10.0 y 45.0 grados.
          - Valide que `humedad_relativa` sea un flotante entre 0.0 y 100.0.
          - Valide que `precipitacion_mm` sea un número no negativo.
          - Si alguna validación de rango falla, la lectura debe ser descartada.

    3. **Limpieza de Datos**: Para las lecturas que pasan todas las validaciones, asegúrese de que el código de la estación no tenga espacios en blanco al inicio o al final (método `.strip()`).

**Retorno:**

- Una nueva lista que contenga únicamente los diccionarios de lecturas que pasaron todas las validaciones, con sus datos numéricos correctamente convertidos.

-----

### Función 2: `calcular_promedios_por_estacion(lecturas_validas)`

**Parámetros:**

- `lecturas_validas`: La lista de lecturas limpias y validadas.

**Lógica:**

- Debe procesar la lista para calcular la temperatura promedio y la humedad promedio para cada estación.

**Retorno:**

- Un diccionario. Las claves serán los códigos de las estaciones. El valor para cada estación será otro diccionario con las claves `'temperatura_promedio'` y `'humedad_promedio'`.

**Ejemplo de la estructura retornada:**

```python
{
    'EST-01-SJO': {'temperatura_promedio': 25.5, 'humedad_promedio': 75.0},
    'EST-02-LIM': {'temperatura_promedio': 30.1, 'humedad_promedio': 88.5}
}
```

-----

### Función 3: `identificar_eventos_extremos(lecturas_validas)`

**Parámetros:**

- `lecturas_validas`: La lista de lecturas limpias.

**Lógica:**

- Debe identificar todas las lecturas que representen un "evento extremo". Un evento se considera extremo si cumple **alguna** de las siguientes condiciones:
  - `temperatura_celsius` es mayor a 35.0 grados.
  - `precipitacion_mm` es mayor a 20.0 mm.
- La función debe recopilar los `id_lectura` de estos eventos.

**Retorno:**

- Un conjunto (`set`) que contenga los `id_lectura` únicos de todas las lecturas que se consideran eventos extremos. El uso de un conjunto es un requisito explícito.

-----

### Función 4: `resumir_precipitacion_por_provincia(lecturas_validas, estaciones)`

**Parámetros:**

- `lecturas_validas`: La lista de lecturas limpias.
- `estaciones`: El diccionario `info_estaciones` que mapea códigos de estación a `(provincia, altitud)`.

**Lógica:**

- Debe calcular la precipitación total acumulada para cada provincia de Costa Rica.
- Para ello, necesitará usar el diccionario `estaciones` para saber a qué provincia pertenece cada lectura.

**Retorno:**

- Un diccionario donde las claves son los nombres de las provincias y los valores son la suma total de la precipitación (`precipitacion_mm`) registrada en esa provincia.

-----

### Función 5: `encontrar_lectura_mas_fria(lecturas_validas, codigo_estacion)`

**Parámetros:**

- `lecturas_validas`: La lista de lecturas limpias.
- `codigo_estacion`: Una cadena con el código de una estación de interés.

**Lógica:**

- Debe buscar entre todas las lecturas de la `codigo_estacion` especificada cuál de ellas tuvo la temperatura más baja.

**Retorno:**

- El `id_lectura` de la lectura que cumple esta condición. Si no hay lecturas para la estación solicitada, debe retornar `None`.

-----

### Función 6: `imprimir_reporte_climatico(promedios, eventos, precipitacion_provincial, reporte_clave)`

**Parámetros:**

- `promedios`: El diccionario generado por `calcular_promedios_por_estacion`.
- `eventos`: El conjunto generado por `identificar_eventos_extremos`.
- `precipitacion_provincial`: El diccionario generado por `resumir_precipitacion_por_provincia`.
- `reporte_clave`: El ID de la lectura más fría para la estación de interés.

**Lógica:**

- Debe imprimir en la consola un informe claramente formateado con todos los resultados de los análisis.

**Retorno:**

- Esta función no retorna ningún valor (`None`). Su única responsabilidad es la salida de datos a la consola.

-----

## 3\. Flujo Principal del Programa

En la sección principal de su script (en una función con el nombre `main`), usted debe:

1. Inicializar los datos brutos y la información de las estaciones.
2. Llamar a `validar_y_limpiar_lecturas` para obtener la lista de datos procesados.
3. Llamar a las funciones de análisis (`calcular_promedios_por_estacion`, `identificar_eventos_extremos`, `resumir_precipitacion_por_provincia`).
4. Definir una estación de interés (e.g., `'EST-03-CRT'`) y llamar a `encontrar_lectura_mas_fria`.
5. Finalmente, llamar a `imprimir_reporte_climatico` con todos los resultados anteriores para mostrar el informe completo.

-----

## 4\. Datos de Entrada de Ejemplo

Use estos datos para probar su programa:

```python
# --- Datos de Referencia ---
info_estaciones_ejemplo = {
    'EST-01-SJO': ('San José', 1172),
    'EST-02-LIM': ('Limón', 3),
    'EST-03-CRT': ('Cartago', 1435),
    'EST-04-ALA': ('Alajuela', 952)
}

# --- Datos de Campo (Crudos) ---
lecturas_brutas_ejemplo = [
    {'id_lectura': 'LEC-001', 'estacion': ' EST-01-SJO ', 'timestamp': '08:00', 'temperatura_celsius': 22.5, 'humedad_relativa': 80.5, 'precipitacion_mm': 0.0, 'estado_sensor': 'OPERATIVO'},
    {'id_lectura': 'LEC-002', 'estacion': 'EST-02-LIM', 'timestamp': '08:15', 'temperatura_celsius': 30.1, 'humedad_relativa': 88.0, 'precipitacion_mm': 5.5, 'estado_sensor': 'OPERATIVO'},
    # Temperatura no es un número, debe ser descartada
    {'id_lectura': 'LEC-003', 'estacion': 'EST-03-CRT', 'timestamp': '08:05', 'temperatura_celsius': 'diecinueve', 'humedad_relativa': 85.2, 'precipitacion_mm': 0.0, 'estado_sensor': 'OPERATIVO'},
    # Humedad fuera de rango (mayor a 100), debe ser descartada
    {'id_lectura': 'LEC-004', 'estacion': 'EST-01-SJO', 'timestamp': '14:30', 'temperatura_celsius': 26.8, 'humedad_relativa': 102.0, 'precipitacion_mm': 15.0, 'estado_sensor': 'OPERATIVO'},
    {'id_lectura': 'LEC-005', 'estacion': 'EST-03-CRT', 'timestamp': '14:45', 'temperatura_celsius': 18.9, 'humedad_relativa': 90.0, 'precipitacion_mm': 2.5, 'estado_sensor': 'OPERATIVO'},
    # Estación no registrada, debe ser descartada
    {'id_lectura': 'LEC-006', 'estacion': 'EST-05-HER', 'timestamp': '15:00', 'temperatura_celsius': 24.0, 'humedad_relativa': 78.0, 'precipitacion_mm': 1.0, 'estado_sensor': 'OPERATIVO'},
    {'id_lectura': 'LEC-007', 'estacion': 'EST-02-LIM', 'timestamp': '15:10', 'temperatura_celsius': 31.5, 'humedad_relativa': 87.5, 'precipitacion_mm': 25.3, 'estado_sensor': 'OPERATIVO'},
    # Sensor con error, debe ser descartada
    {'id_lectura': 'LEC-008', 'estacion': 'EST-04-ALA', 'timestamp': '15:20', 'temperatura_celsius': 28.0, 'humedad_relativa': 70.1, 'precipitacion_mm': 0.0, 'estado_sensor': 'ERROR'},
    {'id_lectura': 'LEC-009', 'estacion': 'EST-03-CRT', 'timestamp': '04:00', 'temperatura_celsius': 16.5, 'humedad_relativa': 92.3, 'precipitacion_mm': 0.0, 'estado_sensor': 'OPERATIVO'},
    # Temperatura extrema (evento)
    {'id_lectura': 'LEC-010', 'estacion': 'EST-04-ALA', 'timestamp': '12:00', 'temperatura_celsius': 36.2, 'humedad_relativa': 65.0, 'precipitacion_mm': 0.0, 'estado_sensor': 'OPERATIVO'},
]
```

-----

## 5\. Salida Esperada en Consola

Considerando que las lecturas **LEC-003, LEC-004, LEC-006 y LEC-008** serán descartadas por las reglas de validación, la salida esperada es:

```
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

> EST-03-CRT:
  - Temperatura Promedio: 17.7 °C
  - Humedad Promedio: 91.2 %

> EST-04-ALA:
  - Temperatura Promedio: 36.2 °C
  - Humedad Promedio: 65.0 %

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
```
