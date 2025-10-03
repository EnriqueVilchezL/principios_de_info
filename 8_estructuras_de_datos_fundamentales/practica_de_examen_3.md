# **Práctica de examen 3: El Juego de las *Grandes Serres***

## Introducción al Desafío

Se le ha encomendado el desarrollo de un **juego de simulación interactivo**. En este juego la persona jugadora asumirá el rol Dirección Principal de las históricas *Grandes Serres du Jardin des Plantes* en París. Su objetivo es tomar las decisiones diarias de gestión para mantener con vida la valiosa colección botánica del museo durante un período de 10 días, operando con recursos limitados. El juego tendrá 3 configuraciones de juego: facil, medio y difícil.

Deberá implementar una juego que simule por pasos discretos (días) el estado del sistema, y la persona jugadora introduce comandos para gestionarlo. El éxito se medirá por la cantidad de especímenes que logre mantener con vida al final del mes.

## Requerimientos

### Modelo de Datos del Complejo Botánico

En el juego se debe representar el complejo de invernaderos mediante un *diccionario* principal con dos claves: `"recursos_globales"` y `"serres"`.

  * **Recursos Globales:** Un diccionario (clave: `"recursos_globales"`) que contenga los recursos disponibles para todo el complejo. La gestión de cada recurso es diferente:

      * `tanque_agua_litros`: **Recurso estratégico (mensual).** Representa la reserva total de agua para toda la simulación de 10 días. **No se reinicia.**
      * `energia_diaria_max_kwh`: El máximo de energía disponible por día (para reiniciar).
      * `energia_diaria_kwh`: **Recurso táctico (diario).** Representa el presupuesto de energía disponible cada día. Este valor se **reinicia a su máximo cada 24 horas.**

  * **Lista de Invernaderos:** Una lista (clave: `"serres"`) que contenga diccionarios, donde cada diccionario representa un invernadero con la siguiente estructura:

      * `nombre`: El nombre único del invernadero (por ejemplo, `"Serre Tropicale"`).
      * `ambiente`: Un diccionario para las condiciones actuales (`temperatura`, `humedad_relativa`).
      * `especie`: El nombre de la especie albergada.
      * `requerimientos`: Un diccionario que define los parámetros de la especie:
          * `temperatura_optima`: Una tupla `(min, max)`.
          * `humedad_suelo_optima`: Una tupla `(min, max)`.
          * `k_T`: Constante de estrés térmico (flotante).
          * `k_M`: Constante de estrés hídrico (flotante).
      * `plantas`: Una lista de diccionarios, donde cada planta tiene:
          * `id`: Identificador único.
          * `humedad_suelo`: Nivel actual (flotante) entre 0 y 100.
          * `salud`: Nivel de salud de `100` a `0` (flotante).
          * `estado`: `'viva'` o `'muerta'`.

### Modelo de Salud

La salud de una planta se actualizará cada día según la siguiente lógica:

  * **Cálculo de Desviaciones:**

      * Desviación térmica ($\Delta T$): La diferencia absoluta entre la temperatura actual del invernadero y el rango óptimo. Es $0$ si la temperatura está dentro del rango.
      * Desviación de humedad del suelo ($\Delta M$): La diferencia entre la humedad mínima óptima y la humedad actual del suelo. Es $0$ si la humedad está por encima del mínimo.

  * **Fórmula de Daño por Estrés:** El cambio diario en la salud ($\Delta H$) se calcula con la fórmula:
    $$ \Delta H = - \left( k_T \cdot (\Delta T)^2 + k_M \cdot (\Delta M)^2 \right) $$
    Esta fórmula indica que el daño aumenta cuadráticamente con la desviación.

  * **Recuperación:** Si una planta se encuentra en condiciones óptimas ($\Delta T = 0$ y $\Delta M = 0$), su salud se recupera en `+0.5` por día, sin exceder el máximo de `100.0`.

  * **Muerte:** Una planta cambia su estado a `'muerta'` si su `salud` llega a `0.0` o menos.

### Gestión de Recursos y Ciclo de Juego Diario

La persona jugadora tomará decisiones cada día a través de una interfaz de comandos en la consola.

  * **Costos de las Acciones:** Cada acción que ordene tiene un costo:

      * `Calefacción`: Consume `5 kWh` de energía.
      * `Ventilación`: Consume `3 kWh` de energía.
      * `Riego`: Consume `1 litro` de agua por cada `10%` de humedad de suelo que se necesite reponer para alcanzar el máximo del rango óptimo.

  * **Ciclo de Decisión del Jugador:** Cada día, el programa ejecutará el siguiente bucle interactivo:

    1.  **Presentar Informe de Estado:** El programa le mostrará un informe claro de la situación:
          * El estado de los recursos globales (agua y energía para el día).
          * Las condiciones ambientales de cada invernadero.
          * El estado (ID, salud, humedad del suelo) de cada planta viva, destacando las que se encuentren en estado crítico.
    2.  **Solicitar Comandos al Usuario:** El programa le pedirá que introduzca una serie de acciones para el día (ej: `regar <id_planta>`, `calefaccion <nombre_invernadero>`, `pasar`, `ayuda`, `condiciones`).
    3.  **Validar Acciones:** El sistema deberá comprobar si las acciones solicitadas son válidas y si los recursos disponibles (agua, energía) son suficientes para llevarlas a cabo. Si una acción no es posible, se le debe notificar.
    4.  **Confirmar y Ejecutar:** Una vez que usted finalice su turno (e.g., con el comando `pasar`), el sistema aplicará las acciones válidas que ha ordenado.

### Interacciones Ambientales (Física Simplificada)

Las acciones de control deben tener efectos primarios y secundarios.

  * **Efecto Primario:**
      * `Calefacción`: `+2.0 °C` a la temperatura.
      * `Ventilación`: `-2.0 °C` a la temperatura.
      * `Riego`: Aumenta `humedad_suelo` al valor máximo de su rango óptimo.
  * **Efecto Secundario:**
      * Al activar la `Calefacción`, disminuya la `humedad_relativa` en `-5.0%`.
      * Al activar la `Ventilación`, aumente la `humedad_relativa` en `+5.0%`.

### Flujo de la Simulación 10 Días

El programa principal debe ejecutar un ciclo de simulación durante 10 días. El orden de las operaciones dentro de cada día es fundamental:

1.  **Inicio del Día:** Imprimir estado y reiniciar presupuesto de energía. Anunciar si ocurre un evento climático especial para ese día.
2.  **Evaluación y Actualización de Salud:** Calcular y aplicar $\Delta H$ a cada planta viva.
3.  **Decisión del Jugador (Interacción):** Iniciar el ciclo de juego para que la persona jugadora introduzca y confirme sus acciones.
4.  **Ejecución de Acciones:** Aplicar efectos primarios y secundarios de las acciones ordenadas.
5.  **Cambios Naturales Pasivos:** Simular la evolución del ambiente para preparar el día siguiente. Esto incluye:
      * **Eventos Climáticos (Ocasional):** Al inicio del día, existe una pequeña probabilidad (e.g., 15%) de que ocurra un evento que altere la temperatura base:
          * *Ola de Frío:* Reduce la temperatura de todos los invernaderos en 4.0°C.
          * *Día Soleado Intenso:* Aumenta la temperatura de todos los invernaderos en 4.0°C.
      * **Fluctuación Diaria (Siempre):** Una fluctuación estocástica menor para simular el 'ruido' ambiental. Modifique la temperatura de cada invernadero en un valor aleatorio entre **-1.0°C y +1.0°C**.
      * **Evapotranspiración:** Una disminución de la `humedad_suelo` para cada planta viva. Esta disminución depende de la `humedad_relativa` del ambiente para simular la evapotranspiración de forma más realista:
          * **Tasa base de desecación:** `-4.0%`. Esta es la tasa en condiciones de humedad ambiental normales.
          * **Modificador (aire seco):** Si la `humedad_relativa` es inferior al 50%, la desecación se acelera. Añada un `-2.0%` adicional (total `-6.0%`).
          * **Modificador (aire húmedo):** Si la `humedad_relativa` es superior al 80%, la desecación se ralentiza. La tasa total se reduce a `-2.0%`.
6.  **Reporte Final:** Al concluir los 10 días, generar un informe con el número de plantas supervivientes y muertas, calificando el rendimiento de la persona jugadora con 90% plantas vivas excelente, entre 90 y 75 muy bien, entre 75 y 50 aceptable y menor que 50 puede mejorar.