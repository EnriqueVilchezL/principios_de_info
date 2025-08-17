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
    .left   { text-align: left; }
    .center { text-align: center; }
    .right  { text-align: right; }

paginate: true
---
                    
<!-- _header: ![Logo UCR](../resources/ucr.png) Principios de informática ![Logo ECCI](../resources/ecci.png) -->

# Ejercicios de Programación Avanzados 🚀

### Ciclos y Repetición de Procesos

---

## 💡 Introducción

**Preparando ejemplos que aumenten la complejidad de manera gradual**

Los siguientes ejercicios incorporan la necesidad de usar **ciclos** (repetición de pasos), manteniendo la estructura detallada que hemos trabajado.

---

## 🏭 Ejercicio 5: Procesamiento de Lote para Control de Calidad

---

## 📋 Contexto del Problema

**Fábrica de componentes aeroespaciales** 🛩️

La producción ha aumentado. Ahora, en lugar de verificar las piezas una por una, la estación de medición debe procesar un **lote completo** y generar un reporte que resuma cuántas piezas fueron aprobadas y rechazadas.

---

## 🎯 Requerimientos del Sistema

1. Solicitar el **número total de piezas** del lote
2. Para cada pieza, solicitar:
   - Longitud (cm) 
   - Peso (kg)
3. Aplicar **criterios de aprobación**:
   - Longitud: [15.0, 15.2] cm (inclusive)
   - Peso: [7.5, 7.8] kg (inclusive)

---

## 📊 Salida Esperada

Al finalizar la revisión de todas las piezas:

**Reporte Final del Lote:**
- Conteo total de piezas **"Aprobadas"**
- Conteo total de piezas **"Rechazadas"**

---

## 🔍 Análisis y Descomposición

---

### **Entradas del Sistema** 📥

- `total_piezas_lote`: Valor numérico entero (cuántas veces se repetirá)
- Para cada repetición:
  - `longitud_pieza` (numérico)
  - `peso_pieza` (numérico)

---

### **Salidas del Sistema** 📤

- `conteo_aprobadas`: Total de piezas que cumplieron criterios
- `conteo_rechazadas`: Total de piezas que no cumplieron

---

### **Casos Especiales (Edge Cases)** ⚠️

- Usuario ingresa `0` piezas → Mostrar 0 aprobadas, 0 rechazadas
- Lote de una sola pieza → Ciclo se ejecuta una vez
- Datos fuera de rangos válidos

---

### **Patrones Identificados** 🧩

1. **Repetición (Ciclo Definido):** Ciclo `PARA` (for)
2. **Acumulación (Contadores):** Variables que se incrementan
3. **Decisión Compuesta:** Lógica "Y" para verificación

---

## 💻 Diseño de la Solución

---

### **Versión 1: Pseudocódigo Híbrido**

```
INICIO
  // Inicializar contadores a cero
  asignar conteo_aprobadas = 0
  asignar conteo_rechazadas = 0

  // Preguntar cuántas piezas procesar
  LEER total_piezas_lote
```

---

```
  // Repetir para cada pieza del lote
  PARA cada pieza DESDE 1 HASTA total_piezas_lote:
    LEER longitud_pieza
    LEER peso_pieza

    SI (longitud_pieza >= 15.0 Y longitud_pieza <= 15.2) Y 
       (peso_pieza >= 7.5 Y peso_pieza <= 7.8) ENTONCES
      incrementar conteo_aprobadas en 1
    SINO
      incrementar conteo_rechazadas en 1
    FIN SI
  FIN PARA
```

---

```
  // Mostrar el reporte final
  MOSTRAR "Reporte Final del Lote:"
  MOSTRAR "Piezas Aprobadas: ", conteo_aprobadas
  MOSTRAR "Piezas Rechazadas: ", conteo_rechazadas
FIN
```

---

### **Versión 2: Lenguaje Natural** 🍳

**Procedimiento para Procesar Lote:**

1. **Preparación:** Toma dos hojas de conteo, una para "Aprobadas" y otra para "Rechazadas". Anota un '0' en ambas.

2. **Determinar el tamaño:** Pregunta cuántas piezas hay en total.

---

3. **Proceso repetitivo:** Para cada pieza del lote:
   a. Mide su longitud y peso
   b. Comprueba si cumple ambos criterios
   c. Haz una marca en la hoja correspondiente

4. **Reporte final:** Cuenta las marcas y anuncia resultados.

---

### **Versión 3: Pseudocódigo Estilo Python**

```python
funcion procesar_lote_calidad():
    conteo_aprobadas = 0
    conteo_rechazadas = 0
    
    total_piezas_lote = entrada_numerica(
        "Número total de piezas: ")
```

---

```python
    # Ciclo 'para' con número definido de repeticiones
    para pieza_actual en rango(total_piezas_lote):
        imprimir(f"--- Pieza {pieza_actual + 1} ---")
        longitud_pieza = entrada_numerica("Longitud (cm): ")
        peso_pieza = entrada_numerica("Peso (kg): ")
        
        si (longitud_pieza >= 15.0 y longitud_pieza <= 15.2) y 
           (peso_pieza >= 7.5 y peso_pieza <= 7.8):
            conteo_aprobadas = conteo_aprobadas + 1
        sino:
            conteo_rechazadas = conteo_rechazadas + 1
```

---

```python
    imprimir("\n--- Reporte Final del Lote ---")
    imprimir(f"Piezas Aprobadas: {conteo_aprobadas}")
    imprimir(f"Piezas Rechazadas: {conteo_rechazadas}")

procesar_lote_calidad()
```

---

## ✅ Validación y Verificación

**Ejemplo de prueba:** Lote de 3 piezas

- **Entradas:** `total_piezas_lote` = 3
  - Pieza 1: longitud=15.1, peso=7.6 → **Aprobada**
  - Pieza 2: longitud=16.0, peso=7.7 → **Rechazada**
  - Pieza 3: longitud=15.0, peso=7.5 → **Aprobada**

- **Salida:** "Piezas Aprobadas: 2", "Piezas Rechazadas: 1"

---

## 💰 Ejercicio 6: Simulación de Crecimiento de Inversión

---

## 📈 Contexto del Problema

**Asesor financiero** 🏦

Necesita una herramienta para visualizar el **poder del interés compuesto**. El programa debe simular año por año cómo crece una inversión hasta que **alcance o supere el doble** de su valor original.

---

## 🎯 Requerimientos del Sistema

**Entradas necesarias:**
1. `monto_inicial` de la inversión
2. `tasa_interes_anual` en porcentaje (ej. 5 para 5%)

**Proceso:**
- Calcular crecimiento año por año
- Repetir hasta duplicar el monto inicial
- Informar **cuántos años** se necesitaron

---

## 🔍 Análisis y Descomposición

---

### **Entradas del Sistema** 📥

- `monto_inicial`: Valor numérico
- `tasa_interes_anual`: Valor numérico (porcentaje)

### **Salida del Sistema** 📤

- `anios_requeridos`: Tiempo que duró la simulación

---

### **Casos Especiales (Edge Cases)** ⚠️

- `tasa_interes_anual` es 0 o negativa → Programa nunca terminaría
- `monto_inicial` es 0 o negativo → Lógica sin sentido

*Para este nivel, asumimos valores positivos válidos.*

---

### **Patrones Identificados** 🧩

1. **Repetición (Ciclo Condicional):** Ciclo `MIENTRAS` (while)
2. **Actualización de Estado:** Variable cambia su valor en cada iteración
3. **Acumulación (Contador):** Contar años transcurridos

---

## 💻 Diseño de la Solución

---

### **Versión 1: Pseudocódigo Híbrido**

```
INICIO
  LEER monto_inicial
  LEER tasa_interes_anual

  // Preparar variables para simulación
  asignar saldo_actual = monto_inicial
  asignar meta_duplicar = monto_inicial * 2
  asignar anios_requeridos = 0
  asignar tasa_decimal = tasa_interes_anual / 100
```

---

```
  // Repetir MIENTRAS no se alcance la meta
  MIENTRAS saldo_actual < meta_duplicar:
    // Calcular interés del año actual
    asignar interes_ganado = saldo_actual * tasa_decimal
    
    // Actualizar saldo (añadir interés)
    asignar saldo_actual = saldo_actual + interes_ganado
    
    // Contar un año más
    incrementar anios_requeridos en 1
  FIN MIENTRAS

  MOSTRAR "Se necesitaron ", anios_requeridos, 
          " años para duplicar la inversión."
FIN
```

---

### **Versión 2: Lenguaje Natural** 🍳

**Procedimiento para Simular Inversión:**

1. **Datos Iniciales:** Anota monto inicial y tasa de interés. Calcula la meta (doble del monto).

2. **Preparación:** Prepara contador de años en 0. Saldo actual = monto inicial.

---

3. **Ciclo de Crecimiento:** Repite hasta alcanzar la meta:
   a. Calcula el interés del año (saldo × tasa)
   b. Suma el interés al saldo actual
   c. Añade 1 al contador de años

4. **Resultado Final:** Anuncia el número de años transcurridos.

---

### **Versión 3: Pseudocódigo Estilo Python**

```python
funcion simular_inversion():
    monto_inicial = entrada_numerica("Monto inicial: ")
    tasa_interes_anual = entrada_numerica("Tasa de interés (%): ")
    
    saldo_actual = monto_inicial
    meta_duplicar = monto_inicial * 2
    anios_requeridos = 0
    tasa_decimal = tasa_interes_anual / 100
```

---

```python
    # Ciclo 'mientras' - condición evaluada antes de cada iteración
    mientras saldo_actual < meta_duplicar:
        interes_ganado = saldo_actual * tasa_decimal
        saldo_actual = saldo_actual + interes_ganado
        anios_requeridos = anios_requeridos + 1

    imprimir(f"Se necesitaron {anios_requeridos} años para duplicar la inversión.")

simular_inversion()
```

---

## ✅ Validación y Verificación

**Ejemplo de prueba:**
- **Entradas:** `monto_inicial` = 1000, `tasa_interes_anual` = 10

**Proceso Manual:**
- Año 0: Saldo = 1000, Meta = 2000
- Año 1: Interés = 100, Saldo = 1100
- Año 2: Interés = 110, Saldo = 1210
- ...

**Resultado:** 8 años (saldo llega a ~2143)

---

## 🔑 Conceptos Clave Aprendidos

---

### **Tipos de Ciclos** 🔄

- **Ciclo FOR:** Número **definido** de repeticiones
- **Ciclo WHILE:** Repetir **mientras** se cumpla condición

### **Patrones de Programación** 🧩

- **Contadores:** Variables que se incrementan
- **Acumuladores:** Variables que suman valores
- **Actualización de Estado:** Variables que cambian su valor

---

## 🎯 Reflexión Final

**¿Cuándo usar cada tipo de ciclo?**

- **FOR:** Cuando sabes exactamente cuántas veces repetir
- **WHILE:** Cuando repites hasta que algo suceda

**Ambos ejercicios muestran la potencia de la repetición automática en la programación.** 🚀

---

## 🌟 Próximos Pasos

**Práctica recomendada:**
1. Implementar ambos algoritmos en Python
2. Probar con diferentes casos de entrada
3. Agregar validación de datos de entrada
4. Optimizar la presentación de resultados

**¡La programación se aprende programando!** 💻

---

**¿Preguntas?** 🤔
