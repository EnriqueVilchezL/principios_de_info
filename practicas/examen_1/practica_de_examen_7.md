# Práctica de examen: Optimización del Riego en Cultivos Hidropónicos

## Contexto del Problema

Un sistema de agricultura hidropónica avanzado debe optimizar la distribución de $\mathbf{80}$ **Unidades de Agua** (UA) a lo largo del día para un conjunto de bandejas de cultivo. La meta es distribuir estas 80 unidades en el **menor tiempo posible** (minimizando la duración total del ciclo de riego), seleccionando el tipo de tubería y el caudal, ya que la eficiencia del sistema de riego se degrada con el uso continuo debido a la presión y la acumulación de sedimentos.

**Datos del Riego**:

* **Unidades de Agua Totales a Distribuir:** 80 UA
* **Duración del Mantenimiento de la Tubería (s):** 20 segundos (Tiempo que toma detener el sistema y limpiar/cambiar las tuberías).

**Datos de los Tipos de Tubería (Caños)**:

Existen tres tipos de tubería (caños) que afectan el tiempo que tarda en distribuirse una Unidad de Agua y cómo su eficiencia se degrada con la distribución continua:

| Tipo | Denominación | Tiempo para la Primera Unidad de Agua (s) | Degradación por Unidad Adicional (s) |
| :---: | :---: | :---: | :---: |
| **A** | *Alto Caudal* | 0.80s | 0.12s |
| **M** | *Mediano Caudal* | 1.00s | 0.08s |
| **B** | *Bajo Caudal* | 1.20s | 0.03s |

* La tubería **A** (Alto Caudal) es la más rápida inicialmente, pero se degrada más rápido.
* La tubería **B** (Bajo Caudal) es la más lenta, pero más consistente y duradera.

**Ejemplo de Cálculo del Tiempo de Distribución**:

Supóngase que un ciclo de $\mathbf{5}$ UA es asignado a una tubería tipo **M** (Mediano Caudal):

1.  **UA 1:** $1.00s$ (Tubería Mediano Caudal limpia).
2.  **UA 2:** El tiempo se habrá degradado y tardará $1.00 + 0.08 = 1.08s$.
3.  **UA 3:** El tiempo tardará $1.00 + 0.08 \times 2 = 1.16s$.
4.  **UA 4:** El tiempo tardará $1.00 + 0.08 \times 3 = 1.24s$.
5.  **UA 5:** El tiempo tardará $1.00 + 0.08 \times 4 = 1.32s$.

* **Total de tiempo de distribución de las 5 UA:** $1.00 + 1.08 + 1.16 + 1.24 + 1.32 = \mathbf{5.80s}$.
* Si después de estas 5 UA el sistema requiere **mantenimiento** (cambio/limpieza de tubería), se añade un costo de **20 segundos de mantenimiento**.

Gana la estrategia de riego que distribuya las $\mathbf{80}$ UA en el menor tiempo total (tiempo de distribución + tiempo de mantenimiento).

---

## Descripción del Programa

El programa debe simular la estrategia de riego planteada por un ingeniero agrícola. Al correr, el programa pregunta por la **cantidad de Unidades de Agua** en total y la **duración en segundos** que tarda un mantenimiento. Luego muestra un menú con tres opciones:

1.  **Analizar la estrategia:** Solicita el nombre del ingeniero y la cantidad de **Ciclos de Riego** (lotes) que planean usar. Un ciclo de riego implica usar un tipo de tubería hasta que se requiera el **mantenimiento**.
    * Si se ingresa un valor inválido, se debe repetir la pregunta.
    * Luego, el programa pregunta por el **tipo de tubería (A, M, B)** y la **cantidad de Unidades de Agua** que el ingeniero planea usar con ese caño.
2.  **Ver Estrategia Ganadora:** Muestra el nombre del ingeniero que haya planteado la estrategia que permite distribuir el agua en el menor tiempo.
3.  **Salir del programa:** Finaliza la ejecución.

Una vez leída la estrategia, el programa debe producir en la salida estándar un resultado. Si el ingeniero introduce **datos inadecuados** (tipos de tubería no permitidos, una cantidad de UA que no suma la totalidad), la estrategia se **desclasificará** por ser irrealizable. Si la estrategia es válida, se debe indicar el tiempo total de distribución.

El programa deberá llevar rastro del ingeniero que ha planteado la **mejor estrategia**. Si no se han ingresado estrategias o ninguna de las ingresadas logra finalizar, el programa reporta el texto "**No hay estrategias ganadoras**" cuando se activa la opción 2 del menú.

---

### Ejemplo de Ejecución

```txt
Cantidad unidades de agua: 80
Duración mantenimiento (s): 20

Opción [1=Analizar 2=Ganador 0=Salir]: 1
Nombre del ingeniero: Ing. Aquatica
Cantidad ciclos de riego: 2
Ciclo 1 tipo de tubería: A
Ciclo 1 cantidad de UA: 45
Ciclo 2 tipo de tubería: B
Ciclo 2 cantidad de UA: 35
Ing. Aquatica terminará en 335.50s

Opción [1=Analizar 2=Ganador 0=Salir]: 1
Nombre del ingeniero: Ing. Verde
Cantidad ciclos de riego: 3
Ciclo 1 tipo de tubería: M
Ciclo 1 cantidad de UA: 20
Ciclo 2 tipo de tubería: A
Ciclo 2 cantidad de UA: 30
Ciclo 3 tipo de tubería: A
Ciclo 3 cantidad de UA: 25
La suma de UA no es 80.
Ing. Verde desclasificado

Opción [1=Analizar 2=Ganador 0=Salir]: 2
Ing. Aquatica ganaría la optimización en 335.50s
```
