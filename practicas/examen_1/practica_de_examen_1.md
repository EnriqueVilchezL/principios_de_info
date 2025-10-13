# Práctico: Diseño de Software Científico Modular

**Instrucciones:** Lea atentamente el siguiente problema. DFebe diseñar y escribir en papel un programa completo en Python que cumpla con todos los requisitos. El énfasis de este ejercicio está en la **modularidad estricta**, separando los cálculos puros de la lógica de interacción con el usuario (entradas y salidas).

**Recomendaciones:** Antes de empezar, siga los pasos del diseño de software y resolución de problemas visto en clase:
1.  **Análisis del Problema:** Comprenda qué se le pide hacer, identifique las fórmulas y conceptos científicos involucrados. Piense en los tipos de datos y validaciones requeridas. Considere los casos de prueba y posibles errores. No olvide pensar en los casos extremos.
2.  **Diseño del Programa:** Utilice pseudo codigo o diagramas de flujo para planificar la estructura del programa. Defina claramente las funciones que necesitará, sus parámetros y valores de retorno. Asegúrese de que cada función tenga una única responsabilidad.
3.  **Implementación:** Escriba el código en Python siguiendo el diseño. Comente el código para explicar la lógica. Asegúrese de que las funciones de cálculo no tengan llamadas a `input()` o `print()`.

4.  **Pruebas:** Realice pruebas exhaustivas con diferentes entradas, incluyendo casos límite y datos inválidos, ejecutando el programa a mentalmente o en papel. Verifique que los resultados sean correctos y que el programa maneje errores adecuadamente. 

---

## Problema: Prototipo de Biblioteca de Cálculo Científico

Usted debe desarrollar un prototipo de software para un equipo de ciencias e ingeniería. El programa debe actuar como una interfaz de consola que utiliza una "biblioteca" de funciones de cálculo para realizar simulaciones.

### Requisitos de Arquitectura del Software:

1.  **Separación de Responsabilidades:** Su código debe estar claramente dividido en dos tipos de funciones:
    * **Funciones de Cálculo (Puras):** Son el núcleo de la biblioteca. Estas funciones **NO deben interactuar con el usuario** (no usan `input()` ni `print()`). Su única tarea es recibir datos a través de **parámetros** y devolver un resultado usando la sentencia `return`.
    * **Funciones Gestoras (de Interfaz):** Corresponden a las opciones del menú. Su responsabilidad es comunicarse con la persona usuaria, solicitar y validar los datos, llamar a la función de cálculo correspondiente pasándole los datos como argumentos, recibir el resultado devuelto y presentarlo de forma clara.

2.  **Programa Principal y Menú:**
    * Debe haber un bucle principal que muestre el siguiente menú hasta que el usuario elija salir:
        ```
        *** Biblioteca de Simulación Científica ***
        1. Modelo Logístico de Crecimiento Poblacional (Biología)
        2. Cálculo de Velocidad Terminal (Física)
        3. Salir
        ```
    * Este bucle principal solo debe llamar a la función gestora apropiada según la opción del usuario.

---

## Detalle de las Funciones a Implementar

### Opción 1: Modelo de Crecimiento Poblacional

* **Concepto Teórico:** El **Modelo Logístico** describe el crecimiento de una población en un entorno con recursos limitados. A diferencia del crecimiento exponencial, este modelo incluye la "capacidad de carga" ($K$), que es el tamaño máximo de población que el entorno puede sostener. A medida que la población se acerca a $K$, su tasa de crecimiento disminuye.

* **Tareas a Implementar:**
    1.  **Función de Cálculo (Pura): `calcular_crecimiento_logistico(p_inicial, tasa_r, capacidad_k)`**
        * **Parámetros:**
            * `p_inicial`: Población inicial.
            * `tasa_r`: Tasa intrínseca de crecimiento (un valor decimal, ej: 0.1 para 10%).
            * `capacidad_k`: Capacidad de carga del entorno.
        * **Lógica:** Calcula el cambio en la población ($\Delta P$) usando la fórmula:
            $$ \Delta P = \text{tasa\_r} \times p\_{inicial} \times \left(1 - \frac{p\_{inicial}}{\text{capacidad\_k}}\right) $$
        * **Retorno:** Debe devolver (`return`) el valor de la nueva población (Población Inicial + $\Delta P$), truncado a un número entero.

    2.  **Función Gestora: `gestionar_simulacion_poblacional()`**
        * **Lógica:** Explica el modelo al usuario. Solicita la población inicial, la tasa de crecimiento (ej: 0.1) y la capacidad de carga. Valida que todos los valores sean positivos y que la capacidad de carga sea mayor que la población inicial.
        * Llama a `calcular_crecimiento_logistico()` con los datos validados.
        * Recibe el valor devuelto y lo presenta. Ejemplo de salida:
            `En un entorno con capacidad para 1000 individuos, una población inicial de 100 con una tasa de crecimiento de 0.1 crecerá a aproximadamente 109 individuos en el siguiente periodo.`

---

### Opción 2: Cálculo de Velocidad Terminal

* **Concepto Teórico:** La **Velocidad Terminal** es la velocidad constante máxima que alcanza un objeto al caer a través de un fluido (como el aire). Se produce cuando la fuerza de resistencia del fluido se iguala a la fuerza de la gravedad. A partir de ese punto, la aceleración neta del objeto es cero.

* **Tareas a Implementar:**
    1.  **Función de Cálculo (Pura): `calcular_velocidad_terminal(masa, area_proyectada, coef_arrastre)`**
        * **Parámetros:**
            * `masa`: Masa del objeto en kg.
            * `area_proyectada`: Área de la sección transversal del objeto en m².
            * `coef_arrastre`: Coeficiente de arrastre (adimensional, ej: 0.5 para una esfera).
        * **Constantes a usar dentro de la función:** Gravedad `g = 9.81 m/s²`, Densidad del aire `rho = 1.225 kg/m³`.
        * **Lógica:** Calcula la velocidad terminal ($v_t$) usando la fórmula:
            $$ v_t = \sqrt{\frac{2 \times \text{masa} \times g}{\text{rho} \times \text{area\_proyectada} \times \text{coef\_arrastre}}} $$
        * **Retorno:** Debe devolver (`return`) el valor de la velocidad terminal calculada.

    2.  **Función Gestora: `gestionar_calculo_velocidad_terminal()`**
        * **Lógica:** Explica el concepto al usuario. Solicita la masa, el área proyectada y el coeficiente de arrastre. Valida que todos los valores sean positivos.
        * Llama a `calcular_velocidad_terminal()` con los datos validados.
        * Recibe el valor devuelto y lo presenta redondeado a dos decimales. Ejemplo de salida:
            `Un objeto de 80.0 kg con un área de 0.5 m² y un coeficiente de 0.7 alcanzará una velocidad terminal de 60.33 m/s.`

---
