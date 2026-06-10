# Práctica de Examen 9

<head>
  <meta charset="UTF-8">
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
      }
    };
  </script>

  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>

## Contexto del Problema: Gestión de Recursos Limitados

El sistema de Evaluación de Alerta Temprana (EAT) debe interactuar con un **inventario limitado de recursos** hospitalarios. Un paciente solo puede pasar a la fase de atención (**Procesamiento**) si el recurso especializado que requiere su nivel de gravedad está disponible.

---

### Estructura de Datos del Paciente (Actualizada)

Cada paciente debe contener: **ID, Nombre, Edad, Síntomas, Signos Vitales, Puntuación EAT**. Además:

* **Recurso Requerido:** Nombre del recurso que el paciente necesita para ser atendido (e.g., 'UCI', 'Quirófano').
* **Estado:** `EN ESPERA`, `EN PROCESAMIENTO`, o `DISCARGADO`.

### Inventario de Recursos Críticos (Estado Global)

El sistema debe gestionar los siguientes recursos limitados (usando una variable global en el módulo de negocio):

| Recurso | Disponibilidad Inicial | Requerido por Nivel de Triage |
| --- | --- | --- |
| **CAMA UCI** | 3 | **Nivel 5 (Rojo)** |
| **EQUIPO DE CHOQUE** | 5 | **Nivel 4 (Naranja)** |
| **SALA DE OBSERVACIÓN** | 10 | **Nivel 3 (Amarillo)** |

Los niveles 1 (Azul) y 2 (Verde) se atienden con recursos generales y no consumen estos recursos críticos.

---

## Algoritmo de Triage Automático (Fórmulas de Puntuación EAT)

El programa debe calcular una **Puntuación Total EAT** sumando los puntos de cada signo vital.

### 1. Puntuación por Signo Vital

| Parámetro | Rango de Valor | Puntuación |
| :---: | :---: | :---: |
| **TAS** ($\text{mmHg}$) | $\le 90$ | 3 puntos |
| | $91 - 100$ | 2 puntos |
| | $\ge 160$ | 2 puntos |
| | $101 - 159$ | 0 puntos |
| **FR** ($\text{rpm}$) | $\ge 25$ | 3 puntos |
| | $\le 8$ | 2 puntos |
| | $9 - 24$ | 0 puntos |
| **FC** ($\text{lpm}$) | $\ge 130$ | 3 puntos |
| | $100 - 129$ | 2 puntos |
| | $50 - 99$ | 0 puntos |
| **Temp** ($^{\circ}\text{C}$) | $\ge 38.5$ o $\le 35.0$ | 1 punto |
| **Dolor** (1-10) | $\ge 8$ | 1 punto |

$$
\text{Puntuación Total EAT} = \sum (\text{Puntos\_TAS} + \text{Puntos\_FR} + \text{Puntos\_FC} + \text{Puntos\_Temp} + \text{Puntos\_Dolor})
$$

### 2. Mapeo de Puntuación a Prioridad (Triage)

| Puntuación Total | Nivel | Color |
| :---: | :---: | :---: |
| $\ge 5$ | 5 | **Rojo** (Máxima) |
| $3 - 4$ | 4 | **Naranja** (Grave) |
| $2$ | 3 | **Amarillo** (Urgente) |
| $1$ | 2 | **Verde** (Menos Urgente) |
| $0$ | 1 | **Azul** (No Urgente) |

---

## Requisitos del Programa (Nivel de Análisis)

El menú es: **[Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]**

### 1\. Ingresar (I)

* Calcula EAT, asigna Prioridad/Recurso Requerido.
* El paciente siempre comienza en estado **`EN ESPERA`**.

### 2\. Procesar (P) **(Análisis Crítico)**

Simula el **intento de admisión** del paciente más urgente (`EN ESPERA`, Nivel más alto, luego ID más bajo).

* **Nivel 1 o 2 (Sin Recurso Crítico):** Se atiende y se **retira de la lista** inmediatamente.
* **Nivel 3, 4, o 5 (Con Recurso Crítico):**
    * **Si hay disponibilidad:** **Asigna el recurso** (decrementa el inventario), cambia el estado a **`EN PROCESAMIENTO`**, y el paciente **permanece en la lista**.
    * **Si no hay disponibilidad:** Muestra mensaje de bloqueo, el paciente **permanece** en estado `EN ESPERA`.

### 3\. Liberar Recurso (L) **(Análisis Crítico)**

Simula la finalización del tratamiento.

* Solicita el **ID** de un paciente que debe estar en estado **`EN PROCESAMIENTO`**.
* **Liberación:** Identifica el Recurso Requerido, **incrementa** la disponibilidad de ese recurso en el inventario global.
* Retira al paciente de la lista (`DISCARGADO`).

### 4\. Ver Lista (V)

Muestra la lista de pacientes **ordenada** por Prioridad (Nivel/ID), incluyendo el **`Estado`**.

### 5\. Analizar (A)

Genera un reporte estadístico:

* **Número total de pacientes** (EN ESPERA + EN PROCESAMIENTO).
* **Ocupación de Recursos:** Muestra el número total, **disponible**, y el **porcentaje de utilización** de cada Recurso Crítico.
* **Promedio General** de cada Signo Vital para todos los pacientes en la sala.

---

## Ejemplo de salida

```txt
--- Sistema de Triage Hospitalario v4.0 (Gestión de Recursos Críticos) ---
Bienvenido. Preparese para gestionar la disponibilidad de UCI y Choque.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: I

--- INGRESO DE NUEVO PACIENTE ---
Nombre completo: Julia Vargas
Edad: 45
Síntomas Clave: Choque séptico
--- INGRESO DE SIGNOS VITALES ---
TAS (mmHg): 85
FR (rpm): 26
FC (lpm): 135
Temp (°C, ej: 36.5): 39.1
Nivel de Dolor (1-10): 9

[ÉXITO] Paciente ID 1 ingresado. Prioridad ROJO. Recurso requerido: CAMA UCI.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: I

--- INGRESO DE NUEVO PACIENTE ---
Nombre completo: Roberto Pérez
Edad: 62
Síntomas Clave: Descompensación cardiorrespiratoria
--- INGRESO DE SIGNOS VITALES ---
TAS (mmHg): 95
FR (rpm): 30
FC (lpm): 140
Temp (°C, ej: 36.5): 36.5
Nivel de Dolor (1-10): 5

[ÉXITO] Paciente ID 2 ingresado. Prioridad ROJO. Recurso requerido: CAMA UCI.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: I

--- INGRESO DE NUEVO PACIENTE ---
Nombre completo: Carla Soto
Edad: 22
Síntomas Clave: Fractura simple
--- INGRESO DE SIGNOS VITALES ---
TAS (mmHg): 120
FR (rpm): 15
FC (lpm): 80
Temp (°C, ej: 36.5): 37.0
Nivel de Dolor (1-10): 1

[ÉXITO] Paciente ID 3 ingresado. Prioridad AZUL. Recurso requerido: NINGUNO.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: I

--- INGRESO DE NUEVO PACIENTE ---
Nombre completo: Ernesto Mena
Edad: 71
Síntomas Clave: Dolor abdominal moderado
--- INGRESO DE SIGNOS VITALES ---
TAS (mmHg): 155
FR (rpm): 20
FC (lpm): 95
Temp (°C, ej: 36.5): 38.0
Nivel de Dolor (1-10): 6

[ÉXITO] Paciente ID 4 ingresado. Prioridad AMARILLO. Recurso requerido: SALA DE OBSERVACIÓN.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P

--- INTENTO DE ADMISIÓN (ID: 1, Prioridad: ROJO) ---
[ADMITIDO] Julia Vargas admitida en CAMA UCI.
Recursos restantes de CAMA UCI: 2

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P

--- INTENTO DE ADMISIÓN (ID: 2, Prioridad: ROJO) ---
[ADMITIDO] Roberto Pérez admitido en CAMA UCI.
Recursos restantes de CAMA UCI: 1

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P
--- INTENTO DE ADMISIÓN (ID: 4, Prioridad: AMARILLO) ---
[ADMITIDO] Ernesto Mena admitido en SALA DE OBSERVACIÓN.
Recursos restantes de SALA DE OBSERVACIÓN: 9

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: I

--- INGRESO DE NUEVO PACIENTE ---
Nombre completo: Susana López
Edad: 50
Síntomas Clave: Accidente grave
--- INGRESO DE SIGNOS VITALES ---
TAS (mmHg): 75
FR (rpm): 35
FC (lpm): 150
Temp (°C, ej: 36.5): 37.0
Nivel de Dolor (1-10): 10

[ÉXITO] Paciente ID 5 ingresado. Prioridad ROJO. Recurso requerido: CAMA UCI.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P

--- INTENTO DE ADMISIÓN (ID: 3, Prioridad: AZUL) ---
[ATENDIDO] Carla Soto (ID: 3) - Nivel general. No consume recurso crítico.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P

--- INTENTO DE ADMISIÓN (ID: 5, Prioridad: ROJO) ---
[BLOQUEADO] No hay CAMA UCI disponible. Paciente Susana López sigue EN ESPERA.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: V

--- LISTA DE ESPERA (Prioridad EAT y Antigüedad) ---
Total de Pacientes: 4

--- Posición 1 ---
ID: 1 | Nombre: Julia Vargas | Estado: EN PROCESAMIENTO
  > Triage: ROJO (N5) - EAT: 7 pts
  > Recurso: CAMA UCI
  > SV: TAS:85 | FR:26 | FC:135 | Temp:39.1 | Dolor:9
--- Posición 2 ---
ID: 2 | Nombre: Roberto Pérez | Estado: EN PROCESAMIENTO
  > Triage: ROJO (N5) - EAT: 7 pts
  > Recurso: CAMA UCI
  > SV: TAS:95 | FR:30 | FC:140 | Temp:36.5 | Dolor:5
--- Posición 3 ---
ID: 5 | Nombre: Susana López | Estado: EN ESPERA
  > Triage: ROJO (N5) - EAT: 9 pts
  > Recurso: CAMA UCI
  > SV: TAS:75 | FR:35 | FC:150 | Temp:37.0 | Dolor:10
--- Posición 4 ---
ID: 4 | Nombre: Ernesto Mena | Estado: EN PROCESAMIENTO
  > Triage: AMARILLO (N3) - EAT: 2 pts
  > Recurso: SALA DE OBSERVACIÓN
  > SV: TAS:155 | FR:20 | FC:95 | Temp:38.0 | Dolor:6

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: L

--- LIBERACIÓN DE RECURSO ---
Pacientes actualmente en proceso:
  ID: 1 | Nombre: Julia Vargas | Usando: CAMA UCI
  ID: 2 | Nombre: Roberto Pérez | Usando: CAMA UCI
  ID: 4 | Nombre: Ernesto Mena | Usando: SALA DE OBSERVACIÓN
ID del paciente dado de alta: 1

[LIBERADO] Recurso CAMA UCI liberado.
Recursos disponibles ahora: 2
[DISCARGADO] Paciente Julia Vargas dado de alta y removido de la lista.

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: P

--- INTENTO DE ADMISIÓN (ID: 5, Prioridad: ROJO) ---
[ADMITIDO] Susana López admitida en CAMA UCI.
Recursos restantes de CAMA UCI: 1

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: A

--- REPORTE ESTADÍSTICO DE GESTIÓN DE RECURSOS ---
Número total de pacientes en sala (Espera + Proceso): 3

-- Ocupación y Utilización de Recursos --
  > CAMA UCI: Capacidad Total=3 | Ocupado=2 | Disponible=1
    [Utilización: 66.7%]
  > EQUIPO DE CHOQUE: Capacidad Total=5 | Ocupado=0 | Disponible=5
    [Utilización: 0.0%]
  > SALA DE OBSERVACIÓN: Capacidad Total=10 | Ocupado=1 | Disponible=9
    [Utilización: 10.0%]

-- Promedios de Signos Vitales --
  > Promedio TAS: 105.0
  > Promedio FR: 28.3
  > Promedio FC: 118.3
  > Promedio Temp: 37.85 °C
  > Promedio Dolor: 7.0

Prioridad más alta en sala: ROJO (Nivel 5)

Opción [Ingresar|Procesar|Liberar Recurso|Ver Lista|Analizar|Fin]: F

Programa finalizado. Saliendo del sistema.
```

---

## Evaluación y Requisitos de Implementación (CRÍTICO)

| Tarea | Requisitos Específicos |
| :--- | :--- |
| **Modularidad** | El programa debe estar dividido en **dos**: un módulo de hospital que contenga toda la lógica, funciones y datos (ponga la lista de pacientes como una variable global), y una función principal que llame a esas funciones y las coordine. |
| **Gestión de Estado** | El módulo de negocio **DEBE** utilizar variables globales (`PACIENTES`, `NEXT_ID` y el inventario `RECURSOS_DISPONIBLES`) para gestionar el estado. |
| **Lógica de Recurso** | Implementación correcta de la lógica de **asignación y liberación de recursos** en las opciones **P** y **L**. |

---
