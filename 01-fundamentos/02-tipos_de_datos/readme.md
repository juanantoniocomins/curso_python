<div align="center">

# 🧮 **Tipos de Datos en Python**

### *Guía técnica y profesional sobre los tipos de datos integrados en Python*

![Versión](https://img.shields.io/badge/Versión-1.0-1565C0?style=for-the-badge)
![Actualización](https://img.shields.io/badge/Actualizado-2025--10--31-43A047?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Estable-00C853?style=for-the-badge)

</div>

---

<p align="justify">

Python es un lenguaje **dinámicamente tipado**, lo que significa que **no es necesario declarar el tipo de dato** al crear una variable.  
Cada valor en Python pertenece a una **clase u objeto**, y el intérprete asigna el tipo automáticamente según el valor.  
A continuación, se presenta una tabla con los **tipos de datos más comunes y avanzados**, junto con ejemplos y descripciones para cada uno.

</p>

---

## 🔹 **Tabla de tipos de datos en Python**

| Categoría | Tipo | Ejemplo | Descripción |
|------------|------|----------|--------------|
| **Numéricos** | `int` | `x = 42` | Números enteros (positivos o negativos, sin decimales). |
|  | `float` | `pi = 3.1416` | Números con decimales. |
|  | `complex` | `z = 2 + 3j` | Números complejos con parte real e imaginaria. |
| **Texto** | `str` | `nombre = "Python"` | Cadenas de texto (secuencias de caracteres Unicode). |
| **Booleanos** | `bool` | `activo = True` | Valores lógicos: `True` o `False`. |
| **Secuencias** | `list` | `numeros = [1, 2, 3]` | Lista ordenada y mutable. Permite distintos tipos de datos. |
|  | `tuple` | `coordenadas = (10, 20)` | Tupla ordenada e inmutable. |
|  | `range` | `rango = range(5)` | Secuencia numérica generada automáticamente. |
| **Colecciones sin orden** | `set` | `colores = {"rojo", "verde", "azul"}` | Conjunto sin elementos duplicados ni orden. |
|  | `frozenset` | `dias = frozenset(["lu", "ma", "mi"])` | Versión inmutable de un `set`. |
| **Mapeos (clave-valor)** | `dict` | `usuario = {"nombre": "Juan", "edad": 30}` | Diccionario de pares clave-valor. Mutable y muy utilizado. |
| **Binarios** | `bytes` | `data = b"Hola"` | Secuencia inmutable de bytes. |
|  | `bytearray` | `ba = bytearray(5)` | Versión mutable de `bytes`. |
|  | `memoryview` | `mv = memoryview(b"Hola")` | Vista de memoria eficiente para manipular datos binarios. |
| **Nulos / especiales** | `NoneType` | `valor = None` | Representa la ausencia de valor o un valor nulo. |
| **Tipos avanzados** | `type` | `type(x)` | Devuelve o define el tipo de un objeto. |
|  | `object` | `obj = object()` | Clase base de todos los objetos en Python. |
|  | `callable`, `function`, `module`, `class` | — | Tipos definidos a nivel interno para funciones, módulos y clases. |

---

## 💡 **Conversión de tipos (Casting)**

```python
# Conversión entre tipos
x = int("10")        # str → int
y = float(5)         # int → float
z = str(3.14)        # float → str
b = bool(0)          # int → bool (False)
l = list("abc")      # str → list

🧠 Comprobación de tipos
# Comprobar el tipo de una variable
x = [1, 2, 3]
print(type(x))         # <class 'list'>
print(isinstance(x, list))  # True

# 🐍 **Tipos de Datos en Python**

> En Python, **todo es un objeto**, y cada valor tiene un tipo que determina cómo se comporta y qué operaciones se pueden realizar.  
> Los tipos de datos se infieren automáticamente (no necesitas declararlos explícitamente).

---

## 🧩 **Clasificación general**

| Categoría | Tipos principales |
|------------|------------------|
| 🔢 **Numéricos** | `int`, `float`, `complex` |
| 💬 **Texto** | `str` |
| ⚙️ **Booleanos** | `bool` |
| 📦 **Secuencias** | `list`, `tuple`, `range` |
| 🧮 **Conjuntos** | `set`, `frozenset` |
| 🗂️ **Mapeos** | `dict` |
| 💾 **Binarios** | `bytes`, `bytearray` |
| 🚫 **Nulo o vacío** | `NoneType` |

---

## 📊 **Tabla completa de tipos de datos**

| Categoría | Tipo | Ejemplo | Descripción |
|------------|------|----------|--------------|
| **Numéricos** | `int` | `x = 42` | Números enteros (positivos o negativos, sin decimales). |
|  | `float` | `pi = 3.1416` | Números con decimales. |
|  | `complex` | `z = 2 + 3j` | Números complejos con parte real e imaginaria. |
| **Texto** | `str` | `nombre = "Python"` | Cadenas de texto (secuencias de caracteres Unicode). |
| **Booleanos** | `bool` | `activo = True` | Valores lógicos: `True` o `False`. |
| **Secuencias** | `list` | `numeros = [1, 2, 3]` | Lista ordenada y mutable. Permite distintos tipos de datos. |
|  | `tuple` | `coordenadas = (10, 20)` | Tupla ordenada e inmutable. |
|  | `range` | `rango = range(5)` | Secuencia numérica generada automáticamente. |
| **Colecciones sin orden** | `set` | `colores = {"rojo", "verde", "azul"}` | Conjunto sin elementos duplicados ni orden. |
|  | `frozenset` | `dias = frozenset(["lu", "ma", "mi"])` | Versión inmutable de un `set`. |
| **Mapeos (clave-valor)** | `dict` | `usuario = {"nombre": "Juan", "edad": 30}` | Diccionario de pares clave-valor. Mutable y muy utilizado. |
| **Binarios** | `bytes` | `data = b"Hola"` | Secuencia inmutable de bytes. |
|  | `bytearray` | `ba = bytearray(5)` | Versión mutable de `bytes`. |
|  | `memoryview` | `mv = memoryview(b"Hola")` | Vista de memoria eficiente para manipular datos binarios. |
| **Nulos / especiales** | `NoneType` | `valor = None` | Representa la ausencia de valor o un valor nulo. |
| **Tipos avanzados** | `type` | `type(x)` | Devuelve o define el tipo de un objeto. |
|  | `object` | `obj = object()` | Clase base de todos los objetos en Python. |
|  | `callable`, `function`, `module`, `class` | — | Tipos definidos a nivel interno para funciones, módulos y clases. |

---

## 🧠 **Ejemplo práctico**

```python
# Ejemplo de distintos tipos de datos
entero = 42
decimal = 3.14
complejo = 2 + 5j
texto = "Python"
booleano = True
lista = [1, 2, 3]
tupla = (4, 5, 6)
conjunto = {7, 8, 9}
diccionario = {"nombre": "Juan", "edad": 30}
vacio = None

print(type(texto))  # <class 'str'>

🧭 Conversión entre tipos (Casting)

Python permite convertir entre tipos de datos usando funciones integradas:

int("10")        # ➜ 10
float(5)         # ➜ 5.0
str(123)         # ➜ "123"
list("abc")      # ➜ ['a', 'b', 'c']
tuple([1, 2, 3]) # ➜ (1, 2, 3)
set([1, 2, 2, 3]) # ➜ {1, 2, 3}

## 🧰 **Funciones útiles relacionadas con tipos**

## 🧰 **Funciones útiles relacionadas con tipos**

<table>
  <tr>
    <th>🔧 Función</th>
    <th>📖 Descripción</th>
    <th>💡 Ejemplo</th>
  </tr>
  <tr>
    <td><code>type(obj)</code></td>
    <td>Devuelve el tipo del objeto</td>
    <td><code>type(10)</code> → <code>&lt;class 'int'&gt;</code></td>
  </tr>
  <tr>
    <td><code>isinstance(obj, tipo)</code></td>
    <td>Verifica si un objeto pertenece a un tipo específico</td>
    <td><code>isinstance(3.14, float)</code> → <code>True</code></td>
  </tr>
  <tr>
    <td><code>id(obj)</code></td>
    <td>Devuelve el identificador único en memoria del objeto</td>
    <td><code>id(x)</code></td>
  </tr>
  <tr>
    <td><code>dir(obj)</code></td>
    <td>Lista los atributos y métodos disponibles para un objeto</td>
    <td><code>dir(str)</code></td>
  </tr>
  <tr>
    <td><code>vars(obj)</code></td>
    <td>Devuelve el diccionario con los atributos de un objeto (si los tiene)</td>
    <td><code>vars(mi_objeto)</code></td>
  </tr>
  <tr>
    <td><code>callable(obj)</code></td>
    <td>Verifica si el objeto se puede llamar (por ejemplo, una función o clase)</td>
    <td><code>callable(print)</code> → <code>True</code></td>
  </tr>
  <tr>
    <td><code>help(obj)</code></td>
    <td>Muestra la documentación integrada del objeto o módulo</td>
    <td><code>help(list)</code></td>
  </tr>
  <tr>
    <td><code>issubclass(cls1, cls2)</code></td>
    <td>Comprueba si una clase es subclase de otra</td>
    <td><code>issubclass(bool, int)</code> → <code>True</code></td>
  </tr>
  <tr>
    <td><code>repr(obj)</code></td>
    <td>Devuelve una representación en cadena del objeto, útil para depuración</td>
    <td><code>repr("hola")</code> → <code>'hola'</code></td>
  </tr>
  <tr>
    <td><code>str(obj)</code></td>
    <td>Convierte el objeto a su representación en texto legible</td>
    <td><code>str(3.14)</code> → <code>'3.14'</code></td>
  </tr>
  <tr>
    <td><code>len(obj)</code></td>
    <td>Devuelve la longitud o número de elementos (si aplica)</td>
    <td><code>len([1,2,3])</code> → <code>3</code></td>
  </tr>
</table>

