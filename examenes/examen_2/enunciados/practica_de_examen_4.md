# **Práctica de examen 4: Gestión de Flota, Análisis y Visualización de Combustible**

## Contexto

Usted es el ingeniero encargado de la flota de una planta de distribución de combustibles. Su tarea es diseñar un sistema de software para rastrear los traslados diarios de combustible entre la planta central (Beneficio) y los depósitos de clientes. El objetivo es calcular con precisión el pago a los transportistas, considerando la distancia recorrida y el tipo de combustible.

Para optimizar costos, la planta provee de una red de depósitos receptores a sus clientes. Para cada entrega, un medidor registra el volumen de combustible transportado en barriles (Bbl) y la distancia.

### Unidades de Medida

* El combustible se mide en barriles (Bbl) y galones (Gal).
* 1 barril (Bbl) equivale a 42 galones (Gal).
* Las mediciones de combustible se hacen en notación BB/GG, donde BB indica barriles y GG indica galones.
* Suponga que GG nunca será >= 42.
* La conversión a la unidad base (barriles) es: Total Bbl=BB+GG/42.

### Archivo de Datos Base

Al iniciar el programa, debe solicitar el archivo de transporte realizado ese día (ej. transportes.csv). El archivo tiene un registro por línea, con campos separados por punto y coma (;), o sea un `.csv`.

La **cantidad de columnas llenas varía** según el valor del primer campo, que identifica el **Tipo de Registro**.

| Tipo de Registro | Cantidad de columnas usadas | Columna 2 | Columna 3 | Columna 4 | Columna 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **deposito** | 4 | ID | Nombre | Distancia (km) | N/A |
| **transpor** | 4 | ID | Nombre | Capacidad (Bbl/Gal) | N/A |
| **flete** | 5 | ID Transportista | Carga (Bbl/Gal) | ID Depósito 1 | ID Depósito 2 (0 si solo es uno) |

Un ejemplo de cómo se vería el archivo completo es (los comentarios entre paréntesis y las unidades de medida en los datos son solo indicativos para el ejemplo, pero no están en los datos reales):

| Tipo_de_registro | ID_o_Transportista | Nombre_o_Carga | Distancia_o_Capacidad_o_Deposito_1 | Deposito_3 |
| :--- | :--- | :--- | :--- | :--- |
| **deposito** | `1` (ID) | `Taboga` (Nombre) | `50.5` km | N/A |
| **deposito** | `3` (ID) | `El Roble` (Nombre) | `75.2` km | N/A |
| **transpor** | `4` (ID) | `Acosta` (Nombre) | `400/0` Bbl/Gal | N/A |
| **transpor** | `5` (ID) | `Perez` (Nombre) | `300/30` Bbl/Gal | N/A |
| **flete** | `4` (Transportista ID) | `40/20` Bbl/Gal (Carga) | `1` (Depósito ID) | `2` (Depósito ID) |
| **flete** | `17` (Transportista ID) | `20/0` Bbl/Gal (Carga) | `3` (Depósito ID) | `0` (Ninguno) |

Note cómo los registros que no ocupan la columna 5, simplemente tienen un valor nulo. **No** hay que limpiar los datos.

### Estructura del Programa y Funcionalidad

El programa ahora tiene un menú con tres categorías: **Transacción (Registro)**, **Estadísticas (NumPy/Pandas)** y **Gráficos (Matplotlib)**.

| Opción | Comando | Categoría | Descripción |
| :--- | :--- | :--- | :--- |
| **D**epósito | `D/T/F/A/P/E/G/S`: **D** | Registro | Registra un nuevo depósito receptor. |
| **T**ransportista | `D/T/F/A/P/E/G/S`: **T** | Registro | Registra un nuevo transportista. |
| **F**lete | `D/T/F/A/P/E/G/S`: **F** | Registro | Registra un nuevo viaje de entrega. |
| **A**tención | `D/T/F/A/P/E/G/S`: **A** | Reporte | Reporte de depósitos **no visitados**. |
| **P**ago | `D/T/F/A/P/E/G/S`: **P** | Reporte | Reporte de pagos pendientes a transportistas. |
| **E**stadísticas | `D/T/F/A/P/E/G/S`: **E** | **NumPy/Pandas** | Muestra métricas de fletes (promedios, desviaciones). |
| **G**ráfico | `D/T/F/A/P/E/G/S`: **G** | **Matplotlib** | Visualiza la relación entre carga y costo. |
| **S**alir | `D/T/F/A/P/E/G/S`: **S** | Fin | Finaliza el programa. |

-----

## I. Tareas de Ingeniería Básica (Registro y Reporte)

### 1\. **F**lete (Registro de Viaje)

  * **Entrada:** ID Transportista, Combustible Transportado ($BB/GG$), Depósito 1 ID, Depósito 2 ID (o 0).
  * **Cálculo:** El programa debe tener una función que convierta $BB/GG$ a **Galones totales**.
    $$\text{Galones Totales} = (BB \times 42) + GG$$
  * **Registro:** Se añade el flete al archivo.

### 2\. **P**ago (Reporte de Pagos)

  * **Tarea:** Calcular la suma total de pagos debidos a cada transportista por sus fletes realizados.
  * **Cálculo (Para cada flete):**
      * **Galones Totales** (de $BB/GG$).
      * **Capacidad Base ($C_{base}$):** Capacidad del camión del transportista, convertida a **Barriles base**.
      * **Distancia Promedio ($D_{promedio}$):** Promedio de las distancias de los depósitos visitados (si se visitan dos depósitos con distancias $D_1$ y $D_2$, $D_{promedio} = (D_1 + D_2)/2$).
      * **Factor de Ajuste ($F_{ajuste}$):** $1 + \frac{D_{promedio}}{C_{base}}$
      * **Pago del Flete:** $\text{Pago} = \text{Galones Totales} \times 1500 \times F_{ajuste}$
  * **Salida:** Lista de transportistas y su pago total acumulado.

-----

## II. Tareas de Ingeniería Avanzada (NumPy, Pandas, Matplotlib)

### 3\. **E**stadísticas (Análisis con NumPy y Pandas)

  * **Propósito:** Analizar la eficiencia y distribución de los fletes.
  * **Proceso:** El programa debe cargar los datos de los fletes y las capacidades en un **DataFrame de Pandas** para realizar los siguientes cálculos con **NumPy/Pandas**:
    1.  **Carga Promedio por Viaje:** Calcular la **media** y **desviación estándar** de los Galones Totales transportados en todos los fletes.
    2.  **Eficiencia de Ruta:** Calcule la **media** y la **varianza** del Factor de Ajuste ($F_{ajuste}$). Un $F_{ajuste}$ alto indica una ruta costosa (lejana o con camión pequeño).
    3.  **Top 3:** Identifique los 3 transportistas con la **mayor Capacidad** de camión (en galones).

### 4\. **G**ráfico (Visualización con Matplotlib)

  * **Propósito:** Visualizar la relación entre el volumen transportado y el costo.
  * **Proceso:** El programa debe generar un gráfico de **Matplotlib**:
      * **Eje X:** Combustible Transportado (en **Galones**).
      * **Eje Y:** Costo por Galón Ajustado (que es el término: $1500 \times F_{ajuste}$).
      * **Gráfico:** Un **gráfico de dispersión** (*scatter plot*) donde cada punto represente un flete.
      * **Líneas de Referencia:** Trace una línea horizontal en el **Costo Base de $1,500$ colones** para visualizar rápidamente qué fletes están por encima o por debajo del costo base.
      * **Salida:** Mostrar el gráfico con etiquetas y título claros.

-----

## III. Opciones de Registro y Reporte (Normales)

### 5\. **D**epósito (Registrar Depósito)

  * **Entrada:** ID, Nombre, Distancia (km).
  * **Registro:** Añade `deposito;ID;Nombre;Distancia` al archivo.

### 6\. **T**ransportista (Registrar Transportista)

  * **Entrada:** ID, Nombre, Capacidad ($BB/GG$).
  * **Registro:** Añade `transportista;ID;Nombre;Capacidad` al archivo.

### 7\. **A**tención (Reporte de Depósitos Pendientes)

  * **Proceso:** Compara la lista de todos los depósitos registrados con los Depósitos ID listados en todos los registros de `flete;`.
  * **Salida:** Imprime la lista de depósitos no visitados, ordenados por ID. Si la lista está vacía, imprime un mensaje de que todos fueron visitados.

-----

### Ejemplo de Interacción y Uso de Opciones Avanzadas

```txt
Nombre del archivo: carros.csv
El archivo indicado no existe.
Nombre del archivo: transportes.csv

Menú [D/T/F/A/P/E/G/S]: D
Identificador (ID): 3
Nombre: El Roble
Distancia (km): 75.2
(Registro 'deposito;3;El Roble;75.2' añadido)

Menú [D/T/F/A/P/E/G/S]: T
Identificador (ID): 5
Nombre: Perez
Capacidad camión (Bbl/Gal): 300/30
(Registro 'transportista;5;Perez;300/30' añadido)

Menú [D/T/F/A/P/E/G/S]: F
Identificador transportista: 4 (Acosta, Capacidad: 400 Bbl)
Combustible transportado (Bbl/Gal): 40/20 (-> 40.476 Bbl / 1699 Gal)
Depósito 1 (ID): 1 (Distancia: 50.5 km)
Depósito 2 (ID): 2 (Distancia: 35.0 km)
(Registro 'flete;4;40/20;1;2' añadido)

Menú [D/T/F/A/P/E/G/S]: F
Identificador transportista: 17 (Palmares, Capacidad: 200 Bbl)
Combustible transportado (Bbl/Gal): 20/0 (-> 20 Bbl / 840 Gal)
Depósito 1 (ID): 3 (Distancia: 75.2 km)
Depósito 2 (ID): 0
(Registro 'flete;17;20/0;3;0' añadido)

Menú [D/T/F/A/P/E/G/S]: E
--- ESTADÍSTICAS DE FLOTA ---

1. Carga Promedio por Viaje:
   - Media: 1269.5 Galones
   - Desviación Estándar: 593.3 Galones

2. Eficiencia de Ruta (Factor de Ajuste):
   - Media: 1.155 (Rutas 15.5% más caras que el base)
   - Varianza: 0.0055

3. Top 3 Transportistas por Capacidad (en Galones):
   - 4 Acosta: 16800.0 Galones
   - 5 Perez: 12630.0 Galones
   - 17 Palmares: 8400.0 Galones

Menú [D/T/F/A/P/E/G/S]: G

(Se abre una ventana con el gráfico. En este gráfico se ve que el Flete 17 (ruta más larga, camión más pequeño) tiene un Costo por Galón Ajustado significativamente más alto que el Flete 4 (ruta más corta, camión más grande), superando la línea de $1500$ colones).

Menú [D/T/F/A/P/E/G/S]: P
--- REPORTE DE PAGOS PENDIENTES ---
4 Acosta: 2,949,500.50 Colones
17 Palmares: 1,601,280.00 Colones

Menú [D/T/F/A/P/E/G/S]: A
--- DEPÓSITOS PENDIENTES DE ATENCIÓN ---
(Ninguno - Todos los depósitos fueron visitados en los fletes registrados)

Menú [D/T/F/A/P/E/G/S]: S
```
