---
marp: true
theme: default
size: 16:9
paginate: true
header: 'Principios de Informática'
footer: '© [Your Name] | [Date]'
math: mathjax
style: |
  /* Diseño minimalista con paleta de colores sofisticada */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
  
  section {
    background: #FAFAFA;
    color: #1A1A1A;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 26px;
    line-height: 1.6;
    padding: 50px;
    font-weight: 400;
  }
  
  h1 {
    color: #2D3A6E;
    font-size: 46px;
    font-weight: 700;
    margin-bottom: 16px;
    border-bottom: 2px solid #E1E2E3;
    padding-bottom: 12px;
    letter-spacing: -0.02em;
  }
  
  h2 {
    color: #3C313D;
    font-size: 36px;
    font-weight: 600;
    margin-top: 24px;
    margin-bottom: 16px;
    letter-spacing: -0.01em;
  }
  
  h3 {
    color: #55535B;
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 12px;
    letter-spacing: -0.005em;
  }
  
  h4 {
    color: #3C313D;
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 8px;
  }
  
  p, li {
    color: #1A1A1A;
    margin-bottom: 8px;
    font-size: 22px;
    line-height: 1.7;
  }
  
  strong {
    color: #18141D;
    font-weight: 600;
  }
  
  code {
    background: #F5F5F5;
    color: #732F3E;
    font-family: 'JetBrains Mono', 'SF Mono', 'Monaco', 'Courier New', monospace;
    padding: 3px 6px;
    border-radius: 4px;
    font-size: 18px;
    font-weight: 500;
  }
  
  pre {
    background: #F8F8F8;
    border: 1px solid #E1E2E3;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
    overflow-x: auto;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  
  pre code {
    background: transparent;
    color: #1A1A1A;
    padding: 0;
    font-size: 17px;
    line-height: 1.5;
    font-weight: 400;
  }
  
  table {
    border-collapse: collapse;
    width: 85%;
    margin: 20px auto;
    background: #FFFFFF;
    border: none;
    border-radius: 12px;
    overflow: hidden;
    font-size: 20px;
  }
  
  thead th {
    background: #F8F8F8;
    color: #1A1A1A;
    font-weight: 600;
    padding: 16px 20px;
    text-align: left;
    border: none;
    border-bottom: 2px solid #E1E2E3;
  }
  
  tbody td {
    padding: 14px 20px;
    border: none;
    border-bottom: 1px solid #F0F0F0;
  }
  
  tbody tr:last-child td {
    border-bottom: none;
  }
  
  tr:last-child td {
    border-bottom: none;
  }
  
  tr:nth-child(even) {
    background: #FAFAFA;
  }
  
  ul, ol {
    margin: 16px 0;
    padding-left: 24px;
  }
  
  li {
    margin-bottom: 8px;
  }
  
  li::marker {
    color: #9D9BA2;
  }
  
  blockquote {
    border-left: 4px solid #2D3A6E;
    background: #F8F8F8;
    margin: 24px 0;
    padding: 20px 24px;
    font-style: italic;
    color: #3C313D;
    font-size: 18px;
  }
  
  /* Encabezados y pies de página elegantes */
  header {
    position: absolute;
    top: 20px;
    left: 50px;
    right: 50px;
    height: 24px;
    font-size: 13px;
    color: #9D9BA2;
    font-weight: 400;
  }
  
  footer {
    position: absolute;
    bottom: 20px;
    left: 50px;
    right: 50px;
    height: 24px;
    font-size: 13px;
    color: #9D9BA2;
    font-weight: 400;
  }
  
  /* Paginación sutil */
  section::after {
    position: absolute;
    bottom: 20px;
    right: 50px;
    font-size: 13px;
    color: #9D9BA2;
    font-weight: 400;
    background: transparent;
  }
  
  /* Espaciado cuidadoso */
  section {
    padding-top: 70px;
    padding-bottom: 70px;
  }
  
  /* Colores de énfasis refinados */
  em code, strong code {
    background: #EBEAEC;
    color: #2D3A6E;
  }
  
  /* Estilo de código en tablas */
  table code {
    background: #F5F5F5;
    color: #732F3E;
  }
  
  /* Jerarquía visual clara */
  section > *:first-child {
    margin-top: 0;
  }
  
  section > *:last-child {
    margin-bottom: 0;
  }
  
  section h2 + h3 {
    margin-top: 12px;
  }
  
  /* Fondo principal limpio */
  section {
    background: #FFFFFF;
  }
  
  /* Espaciado mejorado para listas */
  ul li, ol li {
    padding-left: 4px;
  }
  
  /* Títulos con mejor contraste */
  h1, h2 {
    text-rendering: optimizeLegibility;
  }
---

# Principios de Informática: Tipos de Datos y Variables en Python
### Las piezas fundamentales de cualquier programa
**Persona Docente:** [Tu Nombre]
**Curso:** Principios de Informática

---

## Módulo 1: ¿Por Qué Nos Importa Esto? 🛰️💥
### El Caso del Mars Climate Orbiter

![bg right:40%](https://images.unsplash.com/photo-1614726347317-53a81d4a9914?q=80&w=1974&auto=format&fit=crop)

En 1999, la NASA perdió el Mars Climate Orbiter de $125 millones.

* **La Causa Raíz:** Un error de software increíblemente simple.
    * Un sistema en Tierra enviaba datos en **libras-fuerza/segundo** (tipo imperial).
    * La nave esperaba los datos en **newtons/segundo** (tipo métrico).

* **La Lección:** ¡El manejo incorrecto de tipos de datos tiene consecuencias en el mundo real! Es crucial para la ingeniería de precisión.

---

## Módulo 1: Agenda de la Sesión 🗺️
### Nuestro Recorrido de Hoy

1.  🔢 **Tipos de Datos Fundamentales**: `int`, `float`, `bool`, `str`.
2.  🏷️ **Variables**: Cómo nombrar y almacenar datos.
3.  💎 **Mutabilidad vs. Inmutabilidad**: ¿Pueden cambiar nuestros datos?
4.  🔩 **Conversión de Tipos (Casting)**: Cómo transformar un tipo en otro.

---

## Módulo 2: Tipos de Datos Fundamentales
### Los "Átomos" de la Información

Un **tipo de dato** define dos cosas sobre un valor:
1.  **Qué es**: El tipo de información que representa.
2.  **Qué puede hacer**: Las operaciones válidas para él.

---

## Módulo 2: Tabla de Tipos Fundamentales

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Python</th>
      <th>Descripción</th>
      <th>Ejemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Entero</td>
      <td><code>int</code></td>
      <td>Números enteros</td>
      <td><code>42</code>, <code>-100</code></td>
    </tr>
    <tr>
      <td>Flotante</td>
      <td><code>float</code></td>
      <td>Números con decimales</td>
      <td><code>3.14</code>, <code>-0.001</code></td>
    </tr>
    <tr>
      <td>Booleano</td>
      <td><code>bool</code></td>
      <td>Verdadero o falso</td>
      <td><code>True</code>, <code>False</code></td>
    </tr>
    <tr>
      <td>Cadena</td>
      <td><code>str</code></td>
      <td>Texto (caracteres)</td>
      <td><code>"Hola"</code>, <code>'Sensor'</code></td>
    </tr>
  </tbody>
</table>

---

## Módulo 2: Enteros (`int`) 🔢

**Precisión Absoluta**: Sin parte fraccionaria.

```python
revoluciones_motor = 5000
poblacion_bacterias = 1_000_000_000  # Guiones para legibilidad
```

**Ejemplo de Ingeniería**: Conteo de ciclos, paquetes de datos.

---

## Módulo 2: Flotantes (`float`) 🔢

**Precisión Finita**: Representan números reales con limitaciones.

```python
voltaje = 4.95
pi_aproximado = 3.14159
constante_planck = 6.626e-34  # Notación científica
```

**Ejemplo de Ingeniería**: Medidas de sensores, cálculos físicos.

---

## Módulo 2: Booleanos (`bool`) ✅❌

El tipo más simple: solo `True` o `False`.

* Internamente, `True` es `1` y `False` es `0`.
* Resultado de **operaciones de comparación**.

```python
temperatura_actual = 95.5
temperatura_maxima = 90.0

alarma_activada = temperatura_actual > temperatura_maxima
print(f"¿Alarma activada? {alarma_activada}")  # True
```

-----

## Módulo 3: Ejercicio 1 - Cilindro 💻

**Objetivo**: Calcular propiedades de un cilindro.

1. Declara `radio` y `altura` (flotantes)
2. Calcula volumen: $V = \pi r^2 h$
3. Calcula área lateral: $A = 2 \pi r h$
4. ¿Es volumen > 50 m³? (booleano)

---

## Módulo 3: Solución del Cilindro

```python
radio = 3.5    # metros
altura = 8.0   # metros
pi = 3.14159

volumen = pi * radio**2 * altura
area_lateral = 2 * pi * radio * altura
es_gran_capacidad = volumen > 50

print(f"Volumen: {volumen:.2f} m³")
print(f"Área lateral: {area_lateral:.2f} m²")
print(f"¿Gran capacidad? {es_gran_capacidad}")
```

-----

## Módulo 4: Cadenas (`str`) 📝

Secuencia **ordenada** e **inmutable** de caracteres.

* **Creación**: Comillas simples (`'...'`) o dobles (`"..."`)
* **Inmutable**: No se puede cambiar después de creada

```python
nombre_sensor = "Sensor de Temperatura DHT22"
id_componente = 'X-48-AB-v2'
letra = 'A'  # Un carácter es una cadena de longitud 1
```

---

## Módulo 4: Mutabilidad vs. Inmutabilidad

### ¿Se puede cambiar un objeto después de crearlo?

**💎 Inmutable**: `int`, `float`, `bool`, `str`
- No puedes alterar su contenido
- Necesitas crear un objeto nuevo

**🛠️ Mutable**: `list`, `dict` (futuros)
- Puedes modificar el contenido interno

---

## Módulo 4: Demostración con `id()`

```python
x = 10
print(f"Valor: {x}, ID: {id(x)}")

x = x + 1  # ¡Crea un nuevo objeto!
print(f"Valor: {x}, ID: {id(x)}")  # ID diferente
```

El `id()` es como el "DNI" de un objeto en memoria.

-----

## Módulo 5: Variables 🏷️

### En Matemáticas vs. Informática

**Matemáticas**: Símbolo para valor **desconocido**
- $x + 5 = 10$

**Informática**: **Nombre** que apunta a objeto **conocido**
- `voltaje_entrada = 5.0`

El `=` **no es igualdad**, es **asignación**.

---

## Módulo 5: Reglas de Nombramiento

**Obligatorias:**
* Empiezan con letra o `_`
* Solo `A-z`, `0-9`, `_`
* Sensibles a mayúsculas (`voltaje != Voltaje`)

**Convenciones (PEP 8):**
* `snake_case`: minúsculas con guiones bajos
* Nombres descriptivos

---

## Módulo 5: Ejemplos de Nombramiento

| ✅ Bueno               | ❌ Malo              | Razón                    |
| :--------------------- | :------------------- | :----------------------- |
| `velocidad_angular`    | `VelocidadAngular`   | No es snake_case         |
| `sensor_temp_celsius`  | `t`                  | No es descriptivo        |
| `_variable_interna`    | `__variable`         | `__` tiene uso especial  |

-----

## Módulo 6: Conversión de Tipos (Casting) 🔩

A veces necesitamos convertir un dato de un tipo a otro:

* `int(valor)`: Convierte a entero (trunca decimales)
* `float(valor)`: Convierte a flotante
* `str(valor)`: Convierte a cadena
* `bool(valor)`: Convierte a booleano

---

## Módulo 6: Ejemplos de Casting

```python
# float → int (truncamiento)
valor_float = 9.81
valor_int = int(valor_float)  # valor_int será 9

# str → número
dato_leido = "1024"
numero_real = int(dato_leido)  # numero_real será 1024

# número → str (para mensajes)
temperatura = 25.5
mensaje = f"Temperatura: {temperatura} °C"
```

---

## Módulo 6: La Función `input()` ⚠️

**¡Regla de oro!** `input()` **siempre devuelve `str`**

```python
# ❌ Error común
edad_str = input("Tu edad: ")  # "21" (str)
# edad_en_10_anios = edad_str + 10  # ¡TypeError!

# ✅ Forma correcta
edad_str = input("Tu edad: ")
edad_int = int(edad_str)  # Casting necesario
edad_en_10_anios = edad_int + 10
```

-----

## Módulo 7: Ejercicio 2 - Parseo de Datos 💻

**Contexto**: Log con formato `"ID_SENSOR:VALOR:UNIDAD"`

**Ejemplo**: `log_data = "TEMP01:98.6:F"`

**Tareas**:
1. Separar con `split(':')`
2. Asignar a variables: `sensor_id`, `valor_str`, `unidad`
3. Convertir valor a `float`
4. Si es Fahrenheit, convertir a Celsius

---

## Módulo 7: Solución del Parseo

```python
log_data = "TEMP01:98.6:F"

# Parsear
partes = log_data.split(':')
sensor_id, valor_str, unidad = partes[0], partes[1], partes[2]

# Convertir
valor_float = float(valor_str)

if unidad == "F":
    valor_celsius = (valor_float - 32) * 5/9
else:
    valor_celsius = valor_float

print(f"Sensor {sensor_id}: {valor_celsius:.1f}°C")
```

-----

## Módulo 8: Resumen de Conceptos Clave

* **Tipos de Datos**: `int`, `float`, `bool`, `str`
* **Inmutabilidad**: Los tipos fundamentales no se alteran
* **Variables**: Nombres que apuntan a objetos (`=` asigna)
* **Nomenclatura**: Usar `snake_case` descriptivo
* **Casting**: Conversión explícita esencial con datos externos

**Relevancia**: Previene errores y es base de simulación/control.
