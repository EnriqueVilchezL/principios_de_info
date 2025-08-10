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

# Diagramas de flujo 🗺️

---

## ¡Hola, Futuro Programador! 👋

---

**¿Qué es un Diagrama de Flujo?**
Es un **mapa visual** de los pasos y decisiones para resolver un problema. ¡Como una receta!

---

**¿Para qué sirven?** 🤔
Nos ayudan a **planificar** y **entender** cómo funciona un programa antes de escribir código.

---

## Símbolos Esenciales 🔑

---

**Cada forma tiene un significado.**
¡Son nuestro vocabulario visual!

---

**1. Inicio / Fin (Terminal)** ⚪
Marca el **principio** o el **final** del proceso.

![Incio](imgs/inicio.svg)

---

**2. Proceso (Acción)** 🟩
Una **tarea** o **acción** a realizar.

![Incio](imgs/proceso.svg)


---

**3. Entrada / Salida (Datos)** 🟦
Para **pedir información** o **mostrar resultados**.

![Incio](imgs/entrada.svg)

---

**4. Decisión (Condicional)** 🔶
Se hace una **pregunta** con dos respuestas: **Sí** o **No**.

![Decision](imgs/decision.svg)

---

**5. Línea de Flujo (Flecha)** ➡️
Conecta los símbolos y muestra la **dirección** del proceso.

![Flujo](imgs/flujo.svg)


---

## ¡Tu Primer Diagrama! 🚶‍♀️

---

**Ejemplo: ¿Llevo Paraguas? ☔**
Vamos a dibujar el proceso de decidir si necesitamos un paraguas.

---

**Paso 1: El Inicio**
Todo comienza con el símbolo de **INICIO**.

![Flujo](imgs/ejemplo/inicio.svg)


---

**Paso 2: La Primera Acción**
Después de iniciar, ¿qué hacemos? ¡**Mirar el cielo**!

![Flujo](imgs/ejemplo/accion_1.svg)

---

**Paso 3: La Decisión Crucial**
Ahora que sabemos cómo está el cielo, ¿**está lloviendo**?

![Flujo](imgs/ejemplo/decision.svg)

---

**Paso 4: Dos Caminos, Un Final**
Si "Sí", tomamos paraguas. Si "No", salimos sin él. Ambos caminos nos llevan al **FIN**.

![width:200px Diagram](imgs/diagram.png)

---

**¡Así se lee el diagrama!**
*   **INICIO**: Empezamos.
*   **Mirar el cielo**: Una acción simple.
*   **¿Está lloviendo?**: Una pregunta con "Sí" o "No".
*   **Tomar paraguas / Salir sin paraguas**: Acciones diferentes según la respuesta.
*   **FIN**: El proceso termina.

---

## Otro Ejemplo: Par/Impar 🔢

---

**Problema:** Queremos saber si un número es par o impar.

---

**¿Cómo funciona?**
Pedimos un número, decidimos si es par, y mostramos el resultado. ¡Dos caminos, un destino!

---

## ¡Tu Turno! 💪

---

**Ejercicio: Calcular el Área de un Rectángulo**
¡Piensa en los pasos para resolverlo!

---

**Consigna:**
Crea un diagrama de flujo para calcular el área de un rectángulo.

**Recuerda:**
*   Necesitas pedir el **ancho** y el **alto**.
*   La fórmula es: **Área = Ancho \* Alto**.
*   Debes **mostrar el resultado**.

---

## Solución ✅

---

**Diagrama: Área de Rectángulo**

![Flujo](imgs/rectangulo.svg)

---

**¿Cómo te fue?**
¡Felicidades si te acercaste! Lo importante es entender el flujo de los pasos.

---

## ¿Por qué son útiles en Programación? 💡

---

**1. Claridad** 📝
Ayudan a **organizar tus ideas** antes de escribir código.

**2. Detectar Errores** 🐛
Puedes **seguir el flujo** para encontrar problemas lógicos.

**3. Comunicación** 🗣️
Explican la **lógica** de tu programa a cualquiera.

**4. Pensamiento Lógico** 🧠
Te entrenan a **pensar paso a paso**, clave para programar.

---

**¡Sigue practicando!**
Con ellos, ¡la programación será más fácil y divertida!

---

**¡Gracias!**
**¡A programar se ha dicho!** 🚀