### **Guía de Formato para Evaluaciones de Programación en Papel**

Para asegurar que su solución sea clara, legible y pueda ser evaluada de manera justa y consistente, es **obligatorio** seguir las siguientes directrices al escribir su código.

#### **1. Reglas Generales de Presentación**

  * **Escritura Clara:** Utilice un bolígrafo de tinta oscura (negro o azul) o lápiz y escriba con letra de imprenta clara. La legibilidad es un requisito para la evaluación.
  * **Planificación del Espacio:** Planifique su solución antes de escribir para asegurar que quepa en el espacio que tenga.
  * **Correcciones Limpias:** Si necesita corregir, tache la sección incorrecta con una **única línea horizontal** y escriba la corrección de forma clara. Evite tachones o el uso de corrector.

#### **2. Estructura Obligatoria del Código**

Toda solución debe seguir la siguiente estructura de tres partes en el orden especificado. Se utilizarán comentarios para delimitar cada sección.

**Parte I: Función Principal**
Aquí se debe definir la función principal (con nombre **main**) que orquesta la solución. Esta función se encargará de:

1.  Inicializar las variables necesarias.
2.  Llamar a las funciones auxiliares para procesar los datos.
3.  Realizar los análisis y agregaciones principales.
4.  Preparar los resultados finales.

**Parte II: Funciones Auxiliares (Helpers)**
En esta sección se deben definir todas las funciones de apoyo. Estas son funciones pequeñas y reutilizables que realizan una tarea específica (ej: cálculos matemáticos, validaciones de datos, normalización de texto, etc.).

#### **3. Formato y Estilo del Código**

  * **Indentación Consistente:**
      * La indentación es **obligatoria** y define los bloques de código.
      * Use una sangría visualmente clara y consistente para cada nivel (aprox. 4 espacios).
  * **Espaciado Vertical:**
      * Deje **una línea en blanco** entre la definición de cada función.
  * **Nombres de Variables y Funciones:**
      * Utilice nombres **descriptivos** y claros (e.g., `promedio_final` en lugar de `pf`).
      * Los nombres de las funciones deben ser verbos que hacen explícito qué hace la función (e.g., `def calcular_promedio()` en lugar de `def promedio()`).
      * Siga la convención `snake_case` (minúsculas y guiones bajos).
  * **Type Hints:**
      * Se recomienda el uso de *type hints* para mejorar la claridad de su código. Ayudan a documentar el tipo de datos que una función espera como argumento (`param: tipo`) y el tipo de dato que retorna (`-> tipo`).
      * **Ejemplo:** `def calcular_promedio(numeros: list[float]) -> float:`
  * **Comentarios:**
      * Añada comentarios breves **únicamente** para explicar lógica compleja. No comente lo obvio.