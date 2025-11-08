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

<div align="center">

# 🧮 **Tipos de Datos en Python**

### *Guía técnica y profesional sobre los tipos de datos integrados en Python*

![Versión](https://img.shields.io/badge/Versión-1.0-1565C0?style=for-the-badge)
![Actualización](https://img.shields.io/badge/Actualizado-2025--10--31-43A047?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Estable-00C853?style=for-the-badge)

</div>

---

Python es un lenguaje **dinámicamente tipado**, lo que significa que **no es necesario declarar el tipo de dato** al crear una variable.  
Cada valor en Python pertenece a una **clase u objeto**, y el intérprete asigna el tipo automáticamente según el valor.  

A continuación, se muestra una tabla con los **tipos de datos más comunes y avanzados**, junto con ejemplos y descripciones para cada uno.

---

## 🔹 **Tabla de tipos de datos en Python**

| Categoría | Tipo | Ejemplo | Descripción |
|------------|------|----------|--------------|
| **Numéricos** | `int` | `x = 42` | Números enteros (positivos o negativos, sin decimales). |
|  | `float` | `pi = 3.1416` | Números con decimales. |
|  | `complex` | `z = 2 + 3j` | Números complejos con parte real e imaginaria. |
| **Texto** | `str` | `nombre = "Python"` | Cadenas de texto (secuencias de caracteres Unicode). |
| **Booleanos** | `bool` | `activo = True` | Valores lógicos: `True` o `False`. |
| **Secuencias** | `list` | `numeros = [1, 2, 3]` | Lista ordenada y mutable. |
|  | `tuple` | `coordenadas = (10, 20)` | Tupla ordenada e inmutable. |
|  | `range` | `rango = range(5)` | Secuencia numérica generada automáticamente. |
| **Colecciones sin orden** | `set` | `colores = {"rojo", "verde", "azul"}` | Conjunto sin duplicados ni orden. |
|  | `frozenset` | `dias = frozenset(["lu", "ma", "mi"])` | Versión inmutable de un `set`. |
| **Mapeos (clave-valor)** | `dict` | `usuario = {"nombre": "Juan", "edad": 30}` | Diccionario de pares clave-valor. |
| **Binarios** | `bytes` | `data = b"Hola"` | Secuencia inmutable de bytes. |
|  | `bytearray` | `ba = bytearray(5)` | Versión mutable de `bytes`. |
|  | `memoryview` | `mv = memoryview(b"Hola")` | Vista eficiente para manipular datos binarios. |
| **Nulos / especiales** | `NoneType` | `valor = None` | Representa la ausencia de valor o nulo. |
| **Tipos avanzados** | `type` | `type(x)` | Devuelve o define el tipo de un objeto. |
|  | `object` | `obj = object()` | Clase base de todos los objetos. |
|  | `callable`, `function`, `module`, `class` | — | Tipos internos para funciones, módulos y clases. |

---

| Categoría | Tipos principales |
|------------|------------------|
| 🔢 **Numéricos** | `int`, `float`, `complex` |
| 💬 **Texto** | `str` |
| ⚙️ **Booleanos** | `bool` |
| 📦 **Secuencias** | `list`, `tuple`, `range` |
| 🧩 **Conjuntos** | `set`, `frozenset` |
| 🗂️ **Mapeos** | `dict` |
| 💾 **Binarios** | `bytes`, `bytearray`, `memoryview` |
| ⛔ **Nulo o vacío** | `NoneType` |

## 💡 **Conversión de tipos (Casting)**

```python
# Conversión entre tipos
x = int("10")        # str → int
y = float(5)         # int → float
z = str(3.14)        # float → str
b = bool(0)          # int → bool (False)
l = list("abc")      # str → list

# Comprobación de tipos
x = [1, 2, 3]
print(type(x))            # <class 'list'>
print(isinstance(x, list))  # True

```

<div align="center">

## 📄 **Información del documento**

<table>
<tr>
<td align="center" bgcolor="#212121" style="color:white; padding:20px; border-radius:10px;">

### 👤 **Autor**

**Juanan Comins**

<a href="https://github.com/juanantoniocomins" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-juanantoniocomins-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>
<a href="https://www.linkedin.com/in/juan-comins-9222aa212/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Juanan_Comins-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:juanancomins@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contacto-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

</td>
</tr>
</table>

</div>
