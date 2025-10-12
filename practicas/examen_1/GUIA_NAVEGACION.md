# 🗺️ Guía de Navegación del Código - Simulación Serres

## 📍 Mapa del Código

Esta es una guía para navegar el archivo `solucion_practica_examen_3.py` de forma eficiente.

---

## 🏗️ Estructura del Archivo (por secciones)

### 1. **Documentación Principal** (Líneas 1-63)
- 📖 Descripción del juego
- 📚 Conceptos de programación utilizados
- 🗂️ Estructura de datos completa
- 📐 Fórmula matemática del modelo de salud

👉 **Se recomienda comenzar aquí** para entender el panorama general

---

### 2. **Constantes del Juego** (Líneas 70-102)
```python
DIAS_SIMULACION = 10
PROBABILIDAD_EVENTO_CLIMATICO = 0.15
COSTO_CALEFACCION_KWH = 5
# ... etc
```

📝 **Qué encontrarás**: Todos los valores numéricos que controlan el juego  
🎯 **Para qué sirve**: Ajustar la dificultad sin tocar la lógica

---

### 3. **Configuraciones Iniciales** (Líneas 105-344)

#### Funciones principales:
- `obtener_configuracion_facil()` → Devuelve dict con 1 invernadero, 2 plantas
- `obtener_configuracion_media()` → Devuelve dict con 1 invernadero, 3 plantas  
- `obtener_configuracion_dificil()` → Devuelve dict con 2 invernaderos, 4 plantas
- `mostrar_introduccion_juego()` → Imprime bienvenida
- `seleccionar_configuracion()` → Menú interactivo de dificultad

📝 **Qué encontrarás**: Datos iniciales del juego según dificultad  
🎯 **Para qué sirve**: Definir el estado inicial de recursos, plantas e invernaderos

---

### 4. **Sistema de Salud y Estrés** (Líneas 347-498)

#### Funciones principales:
```python
calcular_desviacion_termica(temp_actual, rango_optimo)
calcular_desviacion_hidrica(humedad_actual, rango_optimo)
calcular_cambio_salud(planta, ambiente, requerimientos)
actualizar_salud_plantas(configuracion)
```

📝 **Qué encontrarás**: La lógica matemática del modelo de salud  
🎯 **Para qué sirve**: Calcular cómo afectan las condiciones a las plantas  
⚙️ **Fórmula clave**: `ΔH = -(k_T·ΔT² + k_M·ΔM²)`

---

### 5. **Eventos Climáticos y Ambiente** (Líneas 502-601)

#### Funciones principales:
```python
generar_evento_climatico()           # 15% probabilidad
aplicar_evento_climatico(config, evento)
aplicar_fluctuacion_diaria(config)   # ±1°C aleatorio
aplicar_evapotranspiracion(config)   # Pérdida de agua
```

📝 **Qué encontrarás**: Cambios automáticos del ambiente  
🎯 **Para qué sirve**: Simular naturaleza impredecible

---

### 6. **Acciones del Jugador** (Líneas 603-897)

#### Funciones de búsqueda:
```python
buscar_planta_por_id(config, "ORQ01")
buscar_serre_por_nombre(config, "Serre Tropicale")
```

#### Funciones de cálculo:
```python
calcular_costo_riego(planta, requerimientos)
```

#### Funciones de ejecución:
```python
ejecutar_riego(config, planta_id)
ejecutar_calefaccion(config, nombre_serre)
ejecutar_ventilacion(config, nombre_serre)
```

#### Procesamiento de comandos:
```python
procesar_comando(config, "regar ORQ01")
```

📝 **Qué encontrarás**: Toda la lógica de las acciones del jugador  
🎯 **Para qué sirve**: Validar, calcular costos y aplicar efectos

---

### 7. **Interfaz y Reportes** (Líneas 899-1145)

#### Funciones de ayuda:
```python
mostrar_ayuda()
mostrar_condiciones_optimas(config)
```

#### Funciones de visualización:
```python
mostrar_estado_recursos(config)
mostrar_estado_serre(serre)
mostrar_informe_diario(config, dia)
```

#### Funciones de estadísticas:
```python
contar_plantas_vivas(config)
mostrar_informe_final(config)
```

📝 **Qué encontrarás**: Todo lo que se muestra en pantalla  
🎯 **Para qué sirve**: Comunicar el estado del juego al jugador

---

### 8. **Bucle Principal del Juego** (Líneas 1147-1283)

#### Funciones principales:
```python
ciclo_decision_jugador(config)    # Bucle de comandos
simular_dia(config, dia)          # Orquesta un día completo
jugar()                           # Función principal
```

📝 **Qué encontrarás**: El flujo de ejecución completo  
🎯 **Para qué sirve**: Coordinar todas las partes del juego

---

## 🔄 Flujo de Ejecución del Programa

```
1. if __name__ == "__main__":
   └─> jugar()
       ├─> mostrar_introduccion_juego()
       ├─> seleccionar_configuracion()
       │   └─> obtener_configuracion_XXX()
       │
       └─> for dia in range(1, 11):
           └─> simular_dia(config, dia)
               │
               ├─> 1. Reiniciar energía
               │
               ├─> 2. generar_evento_climatico()
               │   └─> aplicar_evento_climatico()
               │
               ├─> 3. mostrar_informe_diario()
               │   ├─> mostrar_estado_recursos()
               │   └─> mostrar_estado_serre() (para cada serre)
               │
               ├─> 4. actualizar_salud_plantas()
               │   └─> calcular_cambio_salud() (para cada planta)
               │       ├─> calcular_desviacion_termica()
               │       └─> calcular_desviacion_hidrica()
               │
               ├─> 5. ciclo_decision_jugador()
               │   └─> while True:
               │       ├─> input("Comando > ")
               │       └─> procesar_comando()
               │           ├─> ejecutar_riego()
               │           ├─> ejecutar_calefaccion()
               │           ├─> ejecutar_ventilacion()
               │           ├─> mostrar_ayuda()
               │           └─> mostrar_condiciones_optimas()
               │
               └─> 6. Cambios pasivos
                   ├─> aplicar_fluctuacion_diaria()
                   └─> aplicar_evapotranspiracion()
```

---

## 🎯 Puntos Clave para Entender

### 1. **El Diccionario `configuracion` es el Corazón del Juego**
- Se crea al inicio con `obtener_configuracion_XXX()`
- Se pasa a TODAS las funciones
- Se modifica directamente (sin necesidad de retornarlo)

### 2. **Dos Tipos de Recursos**
- **Agua**: Recurso estratégico (NO se renueva)
- **Energía**: Recurso táctico (se renueva cada día)

### 3. **El Modelo de Salud es Cuadrático**
```python
daño = -(k_T·ΔT² + k_M·ΔM²)
```
Significa: El daño aumenta RÁPIDAMENTE con la desviación

### 4. **Orden de Ejecución Diaria es Importante**
1. Evento climático (altera temperatura)
2. Mostrar estado
3. Actualizar salud (evalúa condiciones actuales)
4. Jugador actúa (modifica condiciones)
5. Cambios pasivos (prepara siguiente día)

---

## 🔍 Cómo Buscar Algo Específico

### ¿Quieres entender cómo...?

| **Acción** | **Busca la función** |
|-----------|---------------------|
| ...se calcula el daño a las plantas | `calcular_cambio_salud()` |
| ...se riega una planta | `ejecutar_riego()` |
| ...se procesa un comando | `procesar_comando()` |
| ...se decide si hay evento climático | `generar_evento_climatico()` |
| ...se pierde agua del suelo | `aplicar_evapotranspiracion()` |
| ...se muestra el estado | `mostrar_informe_diario()` |
| ...funciona el bucle principal | `simular_dia()` y `jugar()` |

---

## 📝 Ejercicios Sugeridos

### Nivel Principiante:
1. Cambiar `DIAS_SIMULACION` a 5 días
2. Modificar el costo de riego a 2L por cada 10%
3. Aumentar la probabilidad de eventos climáticos a 30%

### Nivel Intermedio:
4. Agregar un nuevo comando `estado <ID_PLANTA>` que muestre solo esa planta
5. Crear una nueva dificultad "Experto" con 3 invernaderos
6. Modificar `calcular_cambio_salud()` para que la recuperación sea +1.0

### Nivel Avanzado:
7. Agregar un nuevo recurso "fertilizante" que mejore la recuperación
8. Implementar un sistema de logros (ej: "Salvaste todas las plantas")
9. Crear un modo "sandbox" con recursos ilimitados

---

## 💡 Recomendaciones de Lectura del Código

1. **Leer "de arriba hacia abajo"**: Comenzar por el docstring principal
2. **Seguir el flujo**: Desde `jugar()` hasta las funciones específicas
3. **Utilizar los comentarios**: Explican el "por qué", no solo el "qué"
4. **Experimentar**: Cambiar valores y observar los resultados
5. **Diagramar**: Elaborar diagramas de la estructura de datos

---

## 🆘 Preguntas Frecuentes

### P: ¿Por qué las funciones no retornan `configuracion`?
**R**: Porque los diccionarios se pasan "por referencia". Cuando se modifica `planta["salud"]` dentro de una función, se está modificando el diccionario original.

### P: ¿Qué significa `tuple[bool, str]`?
**R**: Es una anotación de tipo que indica que la función retorna una tupla con un booleano y un string, ejemplo: `(True, "¡Éxito!")`

### P: ¿Por qué usar constantes en MAYÚSCULAS?
**R**: Es una convención de Python para indicar que ese valor NO debe cambiar durante la ejecución.

### P: ¿Qué es `if __name__ == "__main__":`?
**R**: Código que solo se ejecuta cuando se corre este archivo directamente, no cuando se importa desde otro módulo.

---

**🎓 Nota Final**

Se recomienda recordar que el mejor modo de aprender es **experimentar**. No debe temer modificar el código, es la mejor forma de comprenderlo a profundidad.
