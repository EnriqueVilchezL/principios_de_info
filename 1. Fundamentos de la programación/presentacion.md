---
marp: true
theme: uncover
backgroundImage: url("../resources/templates/2/Template_page-0018.jpg")
style: |
    header {
        position: absolute;
        top: 10px;
        left: 0;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 40px;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    header img {
        height: 150px;
        width: 180px;
    }

    .triple {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 100%;
    }
    .triple > div {
        flex: 1;
    }
    .left   { text-align: left; }
    .center { text-align: center; }
    .right  { text-align: right; }

paginate: true
---
                    
<!-- _header: ![Logo UCR](../resources/ucr.png) Principios de informática ![Logo ECCI](../resources/ecci.png) -->

# 1. Fundamentos de la programación 🚀

---

## 💡 Tu Viaje Comienza Aquí

---

**¡Hola, futuro programador!**
Prepárate para desvelar los secretos de cómo las computadoras "piensan" y cómo puedes hablar con ellas. 🧠

---

**¿Por qué aprender esto?**
Dominarás el arte de resolver problemas, creando soluciones digitales que impactan el mundo. ✨ ¡Piensa en grande!

---

## 🔢 Conceptos Fundamentales

---

**¿Qué es un Algoritmo?**
Es una **secuencia finita y ordenada de pasos** para resolver un problema o realizar una tarea.

---

**Algoritmo: Una Receta 🧑‍🍳**
Imagina hacer una torta:
1.  Mezclar ingredientes.
2.  Hornear a X grados.
3.  Dejar enfriar.
¡Cada paso es crucial!

---

**¿Qué es Software?**
Son las **instrucciones y datos** que le dicen a una computadora qué hacer.
Es lo "intangible" de tu dispositivo. 👻

---

**Software: Ejemplos Cotidianos**
*   Tu navegador web 🌐
*   La app de tu banco 💰
*   Un videojuego 🎮

---

**¿Qué es Programación?**
Es el **proceso de escribir instrucciones** (código) para que una computadora las ejecute.
¡Es hablar con la máquina en su idioma! 🗣️💻

---

**¿Qué es un Lenguaje de Programación?**
Es un **conjunto de reglas y símbolos** que usamos para escribir esas instrucciones.
¡Como un idioma especial para computadoras! 💬

---

**Python: Nuestro Idioma Favorito 🐍**
*   **Fácil de leer:** Parece inglés.
*   **Versátil:** Para web, ciencia, juegos, ¡casi todo!
*   **Potente:** Usado por Google, Netflix, NASA.

---

![bg w:200 center ](imgs/cpp.png)
![bg w:200 center ](imgs/java.png)
![bg w:450 center ](imgs/python.webp)

---

**Construcción y Ejecución de un Programa**
Es el camino desde tu idea hasta que la computadora la entiende y la realiza.

---

**El Flujo del Programa ➡️**
Tu Código (Python) ✍️
⬇️
Intérprete de Python 🐍 (lo "traduce")
⬇️
Computadora 💻 (lo "ejecuta")
⬇️
Resultado ✅

---

**Ejercicio 1: Tu Primer Saludo 👋**
**Consigna:** Escribe un programa simple que muestre "¡Hola, mundo programador!" en la pantalla.

---

**Ejercicio 1: Solución ✅**
```python
print("¡Hola, mundo programador!")
```
**Explicación:** `print()` es una instrucción para mostrar texto.

---


![bg](../resources/templates/2/Template_page-0006.jpg)

## Bases 🧠


![w:500 center Bases de la programacion](imgs/bases.png)

--- 

#### A. Descomposición ፨

**Separar** los problemas en partes más **pequeñas** y manejables

![bg w:400 right Pizza en trozos](imgs/decomp_pizza.png)

---

![w:750 Ejemplo con robot](imgs/decomp_ex.png)

---

La **descomposición** ayuda a que los problemas grandes sean menos abrumadores

---

#### B. Patrones 🚧

**Recetas** o **fórmulas** que nos ayudan a entender similitudes en los datos o en las situaciones. Esto nos permite resolver problemas de forma más **eficiente**.


---

![bg w:450 center Edificio de lego](imgs/pattern_ex.webp)

<===> 

![bg w:400 center Instrucciones de lego](imgs/pattern_ex_1.jpg)

---

**¿En la práctica?**

Son soluciones **reutilizable**. Son guías 

Existen muchos patrones ya identificados. Ayudan a hacer **buenos** programas y más **rápido**.

---

#### C. Abstracción 🔳

**Esconder** el detalle de algo muy complejo. Se enfoca en **qué** hace algo, y **no cómo** lo hace.

![bg w:400 right Caja negra](imgs/abstract_box.jpg)

---

![bg w:500 center Microondas](imgs/abstract_micro.webp)

??

![bg w:500 center Microondas por dentro](imgs/abstract_inside.jpeg)

---

La **abstracción** permite no abrumarse con todos los detalles de cada instrucción o pasos de un programa.

![w:400 Ejemplo con robot](imgs/decomp_ex.png)

---

#### D. Algoritmos 🧮

Lista **finita** y **ordenada** de instrucciones o pasos **bien definidos**, para **resolver** un problema

---

## ♻️ Ciclo de Desarrollo de Software (SDLC)

---

**¿Cómo se crea software de calidad?**
No es magia, es un proceso organizado, ¡como construir un edificio! 🏗️

---

**Fase 1: Análisis 🔍**
**¿Qué problema estamos resolviendo?**
*   Entender las **necesidades** del usuario.
*   Definir los **objetivos** del programa.
*   ¡La fase más crítica!

---

**Fase 2: Diseño ✏️**
**¿Cómo vamos a resolverlo?**
*   Planificar la **estructura** del programa.
*   Pensar en los **algoritmos** necesarios.
*   ¡El "plano" antes de construir!

---

**Fase 3: Implementación 💻**
**¡Manos a la obra: a programar!**
*   Traducir el diseño a **código**.
*   Escribir las **instrucciones** en Python.
*   ¡Aquí es donde la magia cobra vida!

---

**Fase 4: Prueba ✅**
**¿Funciona como esperábamos?**
*   Buscar **errores** (bugs).
*   Asegurarse de que cumple todos los **requisitos**.
*   ¡Ajustar y pulir hasta la perfección! ✨

---

**SDLC: Resumen Visual**
Análisis ➡️ Diseño ➡️ Implementación ➡️ Prueba
(y a menudo, volver a empezar para mejorar) 🔄

---

## 🗺️ Pensamiento Computacional para Problemas

---

**¿Qué es el Pensamiento Computacional?**
Es una forma de **resolver problemas** usando técnicas que usan los científicos de la computación.
¡No es solo para programadores! Es una habilidad para la vida. 🌟

---

**Paso 1: Comprensión del Problema 🤔**
*   **¿Qué me piden?**
*   **¿Cuál es el objetivo final?**
*   **¿Qué información tengo?**
*   **¿Qué necesito obtener?**
¡Entender antes de actuar!

---

**Paso 2: Descomposición del Problema 🧩**
*   Dividir un problema grande en **partes más pequeñas y manejables**.
*   Resolver cada parte por separado.
*   ¡Como un rompecabezas!

---

**Paso 3: Especificación del Algoritmo 📝**
*   Describir los **pasos detallados** para resolver cada subproblema.
*   Puede ser en lenguaje natural, diagramas de flujo o pseudocódigo.
*   ¡La "receta" lista para codificar!

---

**Paso 4: Codificación ✍️**
*   Traducir el algoritmo a un **lenguaje de programación** (Python).
*   Escribir las instrucciones línea por línea.
*   ¡Aquí aplicas tu conocimiento de Python!

---

**Paso 5: Validación (Prueba y Depuración) ✅**
*   **Ejecutar** el código.
*   **Verificar** si el resultado es correcto.
*   Si hay errores (bugs), **identificarlos y corregirlos**.
*   ¡Asegurarse de que todo funciona perfectamente!

---

**Metodología: Flujo Total**
Problema Grande ➡️ Descomponer ➡️ Algoritmo Detallado ➡️ Código ➡️ Validar ✅

---

**Ejercicio 2: Pensando en Pasos 🚶‍♀️**
**Consigna:** Quieres escribir un programa que pida tu nombre y tu edad, y luego diga "Hola [Tu Nombre], tienes [Tu Edad] años."
Aplica los 5 pasos del pensamiento computacional.

---

**Ejercicio 2: Solución (Ejemplo) 💡**
*   **Comprensión:** Necesito pedir nombre y edad, luego mostrar un saludo personalizado.
*   **Descomposición:**
    *   Pedir nombre.
    *   Pedir edad.
    *   Formar el mensaje.
    *   Mostrar el mensaje.

---

*   **Especificación del Algoritmo:**
    1.  Preguntar "Cuál es tu nombre?". Guardar respuesta.
    2.  Preguntar "Cuántos años tienes?". Guardar respuesta.
    3.  Crear frase combinando "Hola", nombre, "tienes", edad, "años.".
    4.  Mostrar la frase.
*   **Codificación:** (Ver siguiente slide)
*   **Validación:** Ejecutar el código, ingresar datos y verificar que la frase sea correcta.

---

**Ejercicio 2: Código de Solución ✅**
```python
# Codificación
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
mensaje = "Hola " + nombre + ", tienes " + edad + " años."
print(mensaje)
```

---

## 🛠️ Entorno de Programación

---

**¿Dónde escribimos y ejecutamos código?**
Necesitas un **"taller"** para tus programas.
Esto es un **Entorno de Programación**. 🖥️

---

**Componentes Clave:**
*   **Editor de Texto:** Donde escribes tu código (como Word, pero para código).
*   **Intérprete/Compilador:** Traduce tu código a lenguaje de máquina. (Python usa un intérprete).
*   **Consola/Terminal:** Donde ves los resultados de tu programa.

---

**IDEs (Entornos de Desarrollo Integrados)**
Son programas que **combinan** todo lo anterior en uno solo.
¡Tu taller completo en una sola herramienta! 🚀

---

**Ejemplos de IDEs para Python:**
*   **VS Code (Visual Studio Code):** Popular, flexible, muchas extensiones.
*   **PyCharm:** Muy potente para desarrollo profesional.
*   **Jupyter Notebooks:** Ideal para análisis de datos y aprendizaje interactivo.

---

**Ejercicio 4: ¡Prepara tu Entorno! 🚀**
**Consigna:** Si aún no lo has hecho, instala Python y un editor como VS Code. Luego, abre VS Code, crea un nuevo archivo `mi_primer_programa.py` y escribe el "Hola mundo" del Ejercicio 1. Ejecútalo.

---

**Ejercicio 4: Solución (No hay código, solo pasos) ✅**
1.  **Descargar Python:** `python.org/downloads`
2.  **Descargar VS Code:** `code.visualstudio.com`
3.  **Abrir VS Code.**
4.  **Crear archivo:** `File > New File`, guardar como `mi_primer_programa.py`.
5.  **Escribir:** `print("¡Hola, mundo programador!")`
6.  **Ejecutar:** Clic derecho en el archivo y "Run Python File in Terminal" o usar el botón de "Play".

---

## ✍️ Instrucciones y Sus Tipos

---

**¿Qué es una Instrucción?**
Es la **unidad más básica** de un programa.
Una sola orden que le das a la computadora. 🗣️

---

**Tipos de Instrucciones Comunes:**

1.  **Declaraciones**
2.  **Asignaciones**
3.  **Control de Flujo**
4.  **Entrada y Salida (I/O)**

---

**Tipo 1: Declaraciones (Variables) 🏷️**
*   Sirven para **nombrar "contenedores"** donde guardamos información.
*   Piensa en una etiqueta para una caja.
*   `nombre_caja = valor_dentro`

---

**Ejemplo de Declaración**
```python
saludo = "Hola"  # Declara 'saludo' y guarda el texto "Hola"
edad = 30        # Declara 'edad' y guarda el número 30
```
**`saludo` y `edad` son variables.**

---

**Tipo 2: Asignaciones ➡️**
*   **Dar un valor** a una variable.
*   Se usa el signo `=` (no significa "igual", sino "asigna").

---

**Ejemplo de Asignación**
```python
x = 10      # Asigna el valor 10 a la variable x
x = x + 5   # Asigna el valor de (x actual + 5) a x (ahora x es 15)
```
¡Las variables pueden cambiar su valor!

---

**Tipo 3: Control de Flujo 🚦**
*   Cambian el **orden normal** en que se ejecutan las instrucciones (de arriba a abajo).
*   Permiten tomar **decisiones** o **repetir** acciones.

---

**Control de Flujo: Condicionales (Decisiones) 🤔**
*   **`if` (si):** Ejecuta un bloque de código **si** una condición es verdadera.
*   **`else` (si no):** Ejecuta otro bloque **si no** lo es.

---

**Ejemplo: Condicional `if-else`**
```python
temperatura = 25
if temperatura > 20:
    print("¡Qué calor!")
else:
    print("Clima agradable.")
```
**El programa decide qué mensaje mostrar.**

---

**Control de Flujo: Bucles (Repeticiones) 🔁**
*   **`for`:** Repite un bloque de código un **número fijo de veces** o para cada elemento en una secuencia.
*   **`while`:** Repite un bloque de código **mientras** una condición sea verdadera.

---

**Ejemplo: Bucle `for`**
```python
for numero in range(3): # Repite 3 veces (0, 1, 2)
    print("Contando:", numero)
```
**Salida:**
Contando: 0
Contando: 1
Contando: 2

---

**Tipo 4: Entrada y Salida (I/O) ↔️**
*   **Entrada (`input()`):** Recibir datos del usuario (desde el teclado).
*   **Salida (`print()`):** Mostrar información al usuario (en la pantalla).

---

**Ejemplo: Entrada y Salida**
```python
nombre = input("¿Cómo te llamas? ") # Entrada
print("¡Hola, " + nombre + "!")     # Salida
```
**Permite que tu programa interactúe.**

---

**Ejercicio 5: Programa Interactivo 💬**
**Consigna:** Crea un programa que:
1.  Pida al usuario su edad.
2.  Si la edad es mayor o igual a 18, muestre "Eres mayor de edad."
3.  Si no, muestre "Eres menor de edad."
4.  Finalmente, salude al usuario 3 veces usando un bucle.

---

**Ejercicio 5: Solución ✅**
```python
# 1. Pedir la edad
edad_str = input("Por favor, ingresa tu edad: ")
edad = int(edad_str) # Convertir el texto a número entero

# 2 y 3. Usar un condicional
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 4. Saludar 3 veces usando un bucle
nombre = input("¿Cuál es tu nombre para saludarte? ")
for i in range(3):
    print("¡Hola de nuevo, " + nombre + "!")
```

---

## 🌟 ¡Felicidades!

---

**Has completado un gran primer paso.**
Ahora entiendes los **pilares de la programación**.
¡Sigue practicando, la mejor forma de aprender es haciendo! 🚀

---

**"Todo el mundo en este país debería aprender a programar un ordenador... porque te enseña a pensar."**
**— Steve Jobs**

---

**¡A programar se ha dicho!** 🐍✨