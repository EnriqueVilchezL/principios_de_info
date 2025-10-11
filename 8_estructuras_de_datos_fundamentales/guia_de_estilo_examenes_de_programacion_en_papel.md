### **Guía de Formato para Evaluaciones de Programación en Papel**

Para asegurar que su solución sea clara, legible y pueda ser evaluada de manera justa y consistente, es **obligatorio** seguir las siguientes directrices al escribir su código.

#### **1. Reglas Generales de Presentación**

  * **Escritura Clara:** Utilice un bolígrafo de tinta oscura (negro o azul) o lápiz y escriba con letra de imprenta clara. La legibilidad es un requisito para la evaluación.
  * **Planificación del Espacio:** Planifique su solución antes de escribir para asegurar que quepa en el espacio que tenga.
  * **Correcciones Limpias:** Si necesita corregir, tache la sección incorrecta con una **única línea horizontal** y escriba la corrección de forma clara. Evite tachones o el uso de corrector.

#### **2. Estructura Obligatoria del Código**

Toda solución debe seguir la siguiente estructura de tres partes en el orden especificado. Se utilizarán comentarios para delimitar cada sección.

**Parte I: Funciones Auxiliares (Helpers)**
En esta sección se deben definir todas las funciones de apoyo. Estas son funciones pequeñas y reutilizables que realizan una tarea específica (ej: cálculos matemáticos, validaciones de datos, normalización de texto, etc.).

**Parte II: Función Principal**
Aquí se debe definir la función principal que orquesta la solución. Esta función se encargará de:

1.  Inicializar las variables necesarias.
2.  Llamar a las funciones auxiliares para procesar los datos.
3.  Realizar los análisis y agregaciones principales.
4.  Preparar los resultados finales.
5.  Llamar a cualquier función de impresión proporcionada en el examen.

**Parte III: Punto de Entrada (Bloque Principal)**
Esta es la última parte de su script. Contendrá únicamente el bloque `if __name__ == "__main__":` que llama a su función principal para iniciar la ejecución.

**Ejemplo de la Estructura Completa:**

```python
# ==========================================================
# PARTE I: FUNCIONES AUXILIARES
# ==========================================================

def calcular_algo(param1: int, param2: float) -> float:
    # Lógica de la primera función auxiliar
    resultado: float = param1 * param2
    return resultado

def validar_dato(dato: dict) -> bool:
    # Lógica de la segunda función auxiliar
    return True # o False

# (Definir todas las demás funciones auxiliares aquí)


# ==========================================================
# PARTE II: FUNCIÓN PRINCIPAL
# ==========================================================

def ejecutar_solucion() -> None:
    # 1. Usar los datos de entrada proporcionados
    
    # 2. Llamar a las funciones auxiliares
    resultado_calculo: float = calcular_algo(10, 5.5)
    es_valido: bool = validar_dato({'clave': 'valor'})

    # 3. Procesar, analizar y agregar resultados

    # 4. Preparar las estructuras de datos finales
    resultados_finales: dict = {}
    
    # 5. Llamar a la función de impresión del examen
    imprimir_reporte(resultados_finales)


# ==========================================================
# PARTE III: PUNTO DE ENTRADA
# ==========================================================

if __name__ == "__main__":
    ejecutar_solucion()
```

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
  * **Type Hints (Recomendado, no obligatorio):**
      * Se recomienda el uso de *type hints* para mejorar la claridad de su código. Ayudan a documentar el tipo de datos que una función espera como argumento (`param: tipo`) y el tipo de dato que retorna (`-> tipo`).
      * **Ejemplo:** `def calcular_promedio(numeros: list[float]) -> float:`
      * Aunque es una buena práctica, **su uso no es un requisito obligatorio para la evaluación.**
  * **Comentarios:**
      * Añada comentarios breves **únicamente** para explicar lógica compleja. No comente lo obvio.
  * **Uso de la Plantilla del Examen:**
      * Asuma que los datos y funciones proporcionados en el enunciado ya existen. **No los reescriba**.
      * Su función principal debe generar las estructuras de datos con el formato exacto que esperan las funciones de reporte del examen.