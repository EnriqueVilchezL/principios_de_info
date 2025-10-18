# Práctica de examen: Código morse

---

## Contexto del Problema

El Sistema de Código Morse

El código Morse es un sistema de comunicación que utiliza secuencias de señales cortas y largas para representar letras y números. Fue inventado en la década de 1830 por **Samuel Morse** y se convirtió en un método fundamental de comunicación telegráfica.

En código Morse, cada letra del alfabeto y cada dígito se representa mediante una combinación única de **puntos (.)** y **rayas (-)**.

---

### Reglas de Tiempo y Espaciado

* Una señal de punto dura **una unidad de tiempo**.
* Una raya dura **tres unidades**.
* Entre cada símbolo de una misma letra hay un espacio de **una unidad**.
* Entre letras hay un espacio de **tres unidades**.
* Entre palabras hay un espacio de **siete unidades**.

**Ejemplo:** La famosa señal de socorro **SOS** se escribiría en Morse como `... --- ...`.

### Reglas de Validación de Mensajes

Un mensaje en código Morse puede contener errores de transmisión. Para validar mensajes, se utilizan las siguientes reglas:

* Las letras solo pueden contener puntos y rayas.
* Cada letra debe estar separada por espacios.
* Cada palabra debe estar separada por el símbolo **/** (slash).
* Solo se permiten las letras de la **A a la Z** y los dígitos del **0 al 9**.

---

## Requisitos del Programa en Python

Escriba un programa en Python que ayude a sus usuarios a trabajar con código Morse. El programa debe presentar un menú con cuatro opciones, que se activan con la letra mayúscula de cada una.

El siguiente podría ser un ejemplo de interacción del programa:

<pre>
```text
Opción [Codificar|Decodificar|Validar|Fin]: D
Error: No se ha ingresado un mensaje.

Opción [Codificar|Decodificar|Validar|Fin]: V
Error: No se ha ingresado un mensaje.

Opción [Codificar|Decodificar|Validar|Fin]: C
Mensaje: Hola mundo 123
Morse: .... --- .-.. .- / -- ..- -. -.. --- / .---- ..--- ...--

Opción [Codificar|Decodificar|Validar|Fin]: V
Mensaje original: HOLA MUNDO 123
Letras: 9
Dígitos: 3
Palabras: 3
Puntos: 19
Rayas: 22

Opción [Codificar|Decodificar|Validar|Fin]: C
Mensaje: SOS
Morse: ... --- ...

Opción [Codificar|Decodificar|Validar|Fin]: D
Morse: ... --- ...
Texto: SOS

Opción [Codificar|Decodificar|Validar|Fin]: C
Mensaje: CODE2025
Morse: -.-. --- -.. . ..--- ----- ..--- .....

Opción [Codificar|Decodificar|Validar|Fin]: D
Morse: -.-. --- -.. . ..--- ----- ..--- .....
Texto: CODE2025

Opción [Codificar|Decodificar|Validar|Fin]: V
Mensaje original: CODE2025
Letras: 4
Dígitos: 4
Palabras: 1
Puntos: 14
Rayas: 17

Opción [Codificar|Decodificar|Validar|Fin]: C
Mensaje: A B C
Morse: .- / -... / -.-.

Opción [Codificar|Decodificar|Validar|Fin]: D
Morse: .- / -... / -.-.
Texto: A B C

Opción [Codificar|Decodificar|Validar|Fin]: F
Programa finalizado. ¡Hasta pronto!
```
<pre>

El menú muestra las opciones: **Codificar (C)**, **Decodificar (D)**, **Validar (V)**, y **Finalizar (F)**. Si el usuario ingresa otra letra, el menú es desplegado de nuevo hasta que se provea una opción válida.

### 1\. Codificar (C)

La opción **Codificar (C)** permite al usuario ingresar un mensaje en texto normal.

* El mensaje puede contener letras (**A-Z**), dígitos (**0-9**) y **espacios**.
* Las letras pueden estar en mayúsculas o minúsculas, pero el programa las convierte internamente a **mayúsculas** para procesarlas.
* Los espacios en el texto original se convierten en el símbolo **/** (slash) en código Morse.
* El programa muestra el mensaje codificado en Morse, donde cada letra/dígito está **separado por un espacio**.

### Tabla de Codificación Morse

Con la siguiente tabla, se pueden establecer los códigos morse de cada letra y número:

| Letra | Morse | Número | Morse |
| :---: | :---: | :----: | :---: |
| A | `.-` | 0 | `-----` |
| B | `-...` | 1 | `.----` |
| C | `-.-.` | 2 | `..---` |
| D | `-..` | 3 | `...--` |
| E | `.` | 4 | `....-` |
| F | `..-.` | 5 | `.....` |
| G | `--.` | 6 | `-....` |
| H | `....` | 7 | `--...` |
| I | `..` | 8 | `---..` |
| J | `.---` | 9 | `----.` |
| K | `-.-` | | |
| L | `.-..` | | |
| M | `--` | | |
| N | `-.` | | |
| O | `---` | | |
| P | `.--.` | | |
| Q | `--.-` | | |
| R | `.-.` | | |
| S | `...` | | |
| T | `-` | | |
| U | `..-` | | |
| V | `...-` | | |
| W | `.--` | | |
| X | `-..-` | | |
| Y | `-.--` | | |
| Z | `--..` | | |

### 2\. Decodificar (D)

La opción **Decodificar (D)** convierte el mensaje en código Morse previamente ingresado de vuelta a texto normal.

* El programa debe reconocer las secuencias de puntos y rayas separadas por espacios como letras individuales.
* El símbolo **/** debe ser reconocido como separador de palabras.
* El resultado se muestra en **mayúsculas**.

### 3\. Validar (V)

La opción **Validar (V)** genera estadísticas sobre el mensaje original que fue **codificado anteriormente**.

* El programa muestra el mensaje en **mayúsculas** (sin espacios múltiples).
* Se deben contar y mostrar las siguientes estadísticas:
    * Cantidad de **Letras**.
    * Cantidad de **Dígitos**.
    * Cantidad de **Palabras**.
    * Cantidad de **Puntos** utilizados en su representación Morse.
    * Cantidad de **Rayas** utilizadas en su representación Morse.

### 4\. Finalizar (F)

La opción **Finalizar (F)** termina la ejecución del programa.

### Manejo de Errores

Si se intenta **decodificar (D)** o **validar (V)** cuando **no se ha ingresado un mensaje** previamente, el programa debe reportar un mensaje de error.

---

## Evaluación y Requisitos de Implementación

En todos los rubros se evalúan las **buenas prácticas de programación** vistas en el curso.

Debe implementar al menos **5 funciones** y distribuir de forma balanceada las tareas.

| Tarea | Puntuación |
| :--- | :---: |
| 1. Función que inicia la ejecución del programa. | 5%  |
| 2. Presenta el menú. Lee opciones. Repite hasta que se solicite finalizar. | 10%  |
| 3. Lee el mensaje a codificar. Normaliza el texto (mayúsculas, espacios). | 10%  |
| 4. Codifica el mensaje de texto a código Morse utilizando la tabla. | 30%  |
| 5. Decodifica el mensaje de código Morse a texto normal. | 25%  |
| 6. Reporta mensajes de error cuando no se ha ingresado un mensaje. | 10% |
| 7. Genera estadísticas del mensaje: cuenta letras, dígitos, palabras, puntos y rayas. | 10%  |
