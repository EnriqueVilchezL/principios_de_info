# Práctica de Examen: Sistema de Monitoreo de Fauna para el SINAC

**Tiempo Estimado:** 2 horas  

---

## Contexto del Problema

El **Sistema Nacional de Áreas de Conservación (SINAC)**, bajo la dirección del MINAE, es responsable de la protección de la vasta biodiversidad de Costa Rica. Una tarea fundamental para la conservación es el análisis de datos de avistamientos de fauna, recolectados por guardaparques en los diferentes Parques Nacionales del país.

Usted ha sido contratado como persona especialista en programación para desarrollar un prototipo en Python que procese los reportes de avistamientos de campo. El sistema debe ser capaz de consolidar datos, generar estadísticas clave y resaltar información crítica para persona biólogas y encargadas de la toma de decisiones.

---

## Objetivo General del Ejercicio

Desarrollar un programa en Python que procese una lista de registros de avistamientos de fauna. El programa debe limpiar y validar los datos, y posteriormente, generar una serie de reportes analíticos formateados que se imprimirán en la consola.

---

## 1. Modelo de Datos

Usted recibirá los datos de campo en forma de una **lista de diccionarios**. Cada diccionario representa un único avistamiento, pero los datos pueden venir con inconsistencias.

### Datos de Referencia Geográfica:

Adicionalmente, se le proporcionará un diccionario con las coordenadas del punto central de cada Parque Nacional y un radio máximo de validez.

- **`coordenadas_parques`**: Un diccionario que mapea nombres de parques a una tupla con su latitud y longitud central.
- **`radio_valido_km`**: Un valor numérico (flotante) que representa la distancia máxima en kilómetros desde el centro del parque para que un avistamiento sea considerado válido.

### Formato del Diccionario de Avistamiento (Datos Brutos):

- **`id_reporte`**: Un identificador único (cadena de caracteres).
- **`parque`**: Nombre del Parque Nacional (cadena de caracteres).
- **`especie`**: Nombre científico de la especie (cadena de caracteres).
- **`cantidad`**: Número de individuos avistados (puede ser un número o una cadena).
- **`coordenadas`**: Ubicación del avistamiento (una tupla de dos flotantes: `(latitud, longitud)`).
- **`guardaparque`**: Código del guardaparques que realizó el reporte (cadena de caracteres).
- **`estado_conservacion`**: Categoría de riesgo de la especie (cadena de caracteres, e.g., `'En Peligro'`, `'Vulnerable'`, `'Preocupación Menor'`).

---

## 2. Requisitos Funcionales y Modularización

Para asegurar un diseño limpio y reutilizable, su programa deberá estar descompuesto en las siguientes funciones. Usted debe implementar cada una de ellas.

### Función Auxiliar: `calcular_distancia(coords1, coords2)`

**Propósito:**  
Antes de implementar la validación, debe crear una función auxiliar que calcule la distancia entre dos puntos geográficos.

**Parámetros:**
- `coords1`: Tupla `(latitud, longitud)` del primer punto.
- `coords2`: Tupla `(latitud, longitud)` del segundo punto.

**Lógica:**  
Usará la aproximación **Equirectangular**, una fórmula simplificada adecuada para este problema.

1. Convierta las latitudes y longitudes de grados a radianes.
2. Calcule `x = (lon2_rad - lon1_rad) * cos((lat1_rad + lat2_rad) / 2)`.
3. Calcule `y = (lat2_rad - lat1_rad)`.
4. La distancia en kilómetros es `d = sqrt(x² + y²) * R`, donde `R` (radio de la Tierra) es **6371 km**.

**Nota:** Necesitará importar el módulo `math` para `sqrt`, `cos` y `radians`.

**Retorno:**
- La distancia calculada en kilómetros (flotante).

---

### Función 1: `validar_y_limpiar_datos(avistamientos_brutos, coords_parques, radio_maximo)`

**Parámetros:**
- `avistamientos_brutos`: Una lista de diccionarios con los datos sin procesar.
- `coords_parques`: El diccionario con las coordenadas centrales de los parques.
- `radio_maximo`: El radio de validez en kilómetros.

**Lógica:**
- Debe iterar sobre cada diccionario de la lista de entrada.
- Para cada avistamiento, realice las siguientes validaciones **en orden**:
  
  1. **Validación de Cantidad**: Valide que el campo `cantidad` sea un número entero positivo. Si no lo es, descarte el avistamiento. (Use `try-except`).
  
  2. **Validación Geográfica**: 
     - Verifique que el parque del avistamiento exista como clave en `coords_parques`. Si no existe, descarte el avistamiento.
     - Luego, usando su función `calcular_distancia`, calcule la distancia entre las coordenadas del avistamiento y el centro del parque correspondiente.
     - Si la distancia es mayor al `radio_maximo`, el avistamiento debe ser descartado.
  
  3. **Limpieza de Datos**: Si un avistamiento pasa todas las validaciones, asegúrese de que los nombres de los parques y las especies no tengan espacios en blanco al inicio o al final (use el método `.strip()`).

**Retorno:**
- Una nueva lista que contenga únicamente los diccionarios de avistamientos que pasaron todas las validaciones y con sus datos ya limpios.

---

### Función 2: `generar_reporte_por_parque(avistamientos_validos)`

**Parámetros:**
- `avistamientos_validos`: La lista de avistamientos limpios retornada por la función anterior.

**Lógica:**
- Debe procesar la lista para determinar cuántos individuos de cada especie se han reportado en cada Parque Nacional.

**Retorno:**
- Un diccionario. Las claves de este diccionario serán los nombres de los Parques Nacionales. El valor para cada parque será otro diccionario, donde las claves son los nombres de las especies y los valores son la suma total de individuos avistados de esa especie en ese parque.

**Ejemplo de la estructura retornada:**
```python
{
    'Parque Nacional Corcovado': {'Panthera onca': 5, 'Tapirus bairdii': 12},
    'Parque Nacional Manuel Antonio': {'Iguana iguana': 45, 'Saimiri oerstedii': 30}
}
```

---

### Función 3: `obtener_especies_unicas_en_riesgo(avistamientos_validos)`

**Parámetros:**
- `avistamientos_validos`: La lista de avistamientos limpios.

**Lógica:**
- Debe identificar todas las especies cuyos `estado_conservacion` sean `'En Peligro'` o `'Vulnerable'`.
- La colección de especies debe ser única, es decir, sin nombres repetidos.

**Retorno:**
- Un conjunto (`set`) que contenga los nombres de todas las especies únicas que se consideran en riesgo. El uso de un conjunto es un requisito explícito para esta función.

---

### Función 4: `analizar_contribuciones_guardaparques(avistamientos_validos)`

**Parámetros:**
- `avistamientos_validos`: La lista de avistamientos limpios.

**Lógica:**
- Debe contar cuántos reportes válidos ha realizado cada guardaparque.

**Retorno:**
- Un diccionario donde las claves son los códigos de los guardaparques y los valores son el número total de avistamientos que han reportado.

---

### Función 5: `encontrar_avistamiento_norte(avistamientos_validos, especie_objetivo)`

**Parámetros:**
- `avistamientos_validos`: La lista de avistamientos limpios.
- `especie_objetivo`: Una cadena con el nombre de una especie de interés especial (e.g., `'Panthera onca'`).

**Lógica:**
- Debe buscar entre todos los avistamientos de la `especie_objetivo` cuál de ellos se encuentra más al norte (es decir, el que tiene el valor de latitud más alto).
- La latitud es el primer elemento de la tupla `coordenadas`.

**Retorno:**
- El `id_reporte` del avistamiento que cumple con esta condición. Si no hay avistamientos de la especie objetivo, debe retornar `None`.

---

### Función 6: `imprimir_informe_final(reporte_parques, especies_riesgo, contribuciones_guardaparques, reporte_clave)`

**Parámetros:**
- `reporte_parques`: El diccionario generado por `generar_reporte_por_parque`.
- `especies_riesgo`: El conjunto generado por `obtener_especies_unicas_en_riesgo`.
- `contribuciones_guardaparques`: El diccionario generado por `analizar_contribuciones_guardaparques`.
- `reporte_clave`: El ID del reporte del avistamiento más al norte de la especie clave.

**Lógica:**
- Debe imprimir en la consola un informe claramente formateado.
- El informe debe contener todas las secciones: reporte por parque, alerta de especies en riesgo, contribuciones por guardaparque y el punto de interés geográfico.

**Retorno:**
- Esta función no retorna ningún valor (`None`). Su única responsabilidad es la salida de datos a la consola.

---

## 3. Flujo Principal del Programa

En la sección principal de su script (fuera de cualquier función), usted debe:

1. Inicializar los datos brutos, las coordenadas de los parques y el radio máximo.
2. Llamar a `validar_y_limpiar_datos` para obtener la lista de datos procesados.
3. Llamar a `generar_reporte_por_parque` con los datos limpios.
4. Llamar a `obtener_especies_unicas_en_riesgo` con los datos limpios.
5. Llamar a `analizar_contribuciones_guardaparques` con los datos limpios.
6. Definir una especie de interés (e.g., `'Panthera onca'`) y llamar a `encontrar_avistamiento_norte`.
7. Finalmente, llamar a `imprimir_informe_final` con todos los resultados anteriores para mostrar el informe completo.

---

## 4. Datos de Entrada de Ejemplo

Use estos datos para probar su programa:

```python
# --- Datos de Referencia ---
coordenadas_parques_ejemplo = {
    'Parque Nacional Corcovado': (8.55, -83.60),
    'Parque Nacional Manuel Antonio': (9.40, -84.15),
    'Parque Nacional Tortuguero': (10.53, -83.50)
}
radio_valido_km_ejemplo = 40.0  # 40 km de radio máximo

# --- Datos de Campo ---
avistamientos_brutos_ejemplo = [
    {'id_reporte': 'RPT001', 'parque': 'Parque Nacional Corcovado', 'especie': 'Panthera onca', 'cantidad': 2, 'coordenadas': (8.47, -83.59), 'guardaparque': 'GP-04', 'estado_conservacion': 'En Peligro'},
    {'id_reporte': 'RPT002', 'parque': 'Parque Nacional Manuel Antonio ', 'especie': 'Iguana iguana', 'cantidad': '45', 'coordenadas': (9.39, -84.14), 'guardaparque': 'GP-07', 'estado_conservacion': 'Preocupación Menor'},
    # Este reporte está geográficamente fuera del radio de Corcovado, debería ser descartado.
    {'id_reporte': 'RPT003', 'parque': ' Parque Nacional Corcovado ', 'especie': 'Tapirus bairdii', 'cantidad': 12, 'coordenadas': (9.52, -83.68), 'guardaparque': 'GP-04', 'estado_conservacion': 'En Peligro'},
    {'id_reporte': 'RPT004', 'parque': 'Parque Nacional Tortuguero', 'especie': 'Chelonia mydas', 'cantidad': 150, 'coordenadas': (10.53, -83.50), 'guardaparque': 'GP-11', 'estado_conservacion': 'Vulnerable'},
    {'id_reporte': 'RPT005', 'parque': 'Parque Nacional Corcovado', 'especie': 'Panthera onca', 'cantidad': '3', 'coordenadas': (8.49, -83.61), 'guardaparque': 'GP-04', 'estado_conservacion': 'En Peligro'},
    {'id_reporte': 'RPT006', 'parque': 'Parque Nacional Manuel Antonio', 'especie': 'Saimiri oerstedii', 'cantidad': 30, 'coordenadas': (9.40, -84.15), 'guardaparque': 'GP-07', 'estado_conservacion': 'Vulnerable'},
    # Este reporte tiene una cantidad inválida, debería ser descartado.
    {'id_reporte': 'RPT007', 'parque': 'Parque Nacional Corcovado', 'especie': 'Puma concolor', 'cantidad': 'no_valido', 'coordenadas': (8.50, -83.60), 'guardaparque': 'GP-04', 'estado_conservacion': 'Preocupación Menor'},
    # Este reporte corresponde a un parque no registrado en los datos de referencia, debería ser descartado.
    {'id_reporte': 'RPT008', 'parque': 'Parque Nacional Chirripó', 'especie': 'Sylvilagus dicei', 'cantidad': 10, 'coordenadas': (9.48, -83.48), 'guardaparque': 'GP-15', 'estado_conservacion': 'En Peligro'},
]
```

---

## 5. Salida Esperada en Consola

Considerando que los reportes **RPT003**, **RPT007** y **RPT008** serán descartados por las nuevas reglas de validación, la salida esperada ahora es:

```
============================================================
*** INFORME DE MONITOREO DE FAUNA - SINAC ***
============================================================

--- Reporte de Avistamientos por Parque Nacional ---

> Parque Nacional Corcovado:
  - Panthera onca: 5 individuos

> Parque Nacional Manuel Antonio:
  - Iguana iguana: 45 individuos
  - Saimiri oerstedii: 30 individuos

> Parque Nacional Tortuguero:
  - Chelonia mydas: 150 individuos

--- Alerta de Especies en Riesgo ---

Las siguientes especies requieren atención especial:
* Panthera onca
* Chelonia mydas
* Saimiri oerstedii

--- Contribuciones por Guardaparque ---

> Reportes válidos por guardaparque:
  - GP-04: 2 reportes
  - GP-07: 2 reportes
  - GP-11: 1 reporte

--- Punto de Interés Geográfico ---

> Avistamiento más al norte de 'Panthera onca':
  - ID del Reporte: RPT005

============================================================
*** Fin del Informe ***
============================================================
```
