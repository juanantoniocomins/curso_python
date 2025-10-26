<div align="center">

# 🎯 PLANTILLA DE REFERENCIA MARKDOWN

### *Guía completa de elementos para documentación de Python*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--10--26-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

</div>

---

## 📚 ÍNDICE DE ELEMENTOS DISPONIBLES

<details open>
<summary><b>🎨 Click para ver todos los elementos</b></summary>

### 🎯 Estructura y Navegación
- [Título Principal](#-título-principal)
- [Títulos de Sección](#-títulos-de-sección)
- [Subtítulos de Nivel](#-subtítulos-de-nivel)
- [Tabla de Contenidos Desplegable](#-tabla-de-contenidos-desplegable)
- [Separadores Visuales](#-separadores-visuales)

### ✍️ Texto y Formato
- [Párrafo Justificado](#-párrafo-justificado)
- [Formato de Texto Básico](#-formato-de-texto-básico)
- [Citas Textuales](#-citas-textuales)
- [Código en Línea](#-código-en-línea)

### 📋 Listas
- [Listas Numeradas](#-listas-numeradas)
- [Listas con Viñetas](#-listas-con-viñetas)
- [Listas de Tareas](#-listas-de-tareas)
- [Listas Anidadas](#-listas-anidadas)

### 📊 Tablas
- [Tabla Básica](#-tabla-básica)
- [Tabla con Alineación](#-tabla-con-alineación)
- [Tabla con Formato Interno](#-tabla-con-formato-interno)
- [Tabla con Colores de Fondo](#-tabla-con-colores-de-fondo)
- [Tabla Comparativa](#-tabla-comparativa)

### 💻 Código
- [Bloque de Código Python](#-bloque-de-código-python)
- [Bloque de Código con Comentarios](#-bloque-de-código-con-comentarios)
- [Bloques de Código Múltiples Lenguajes](#-bloques-de-código-múltiples-lenguajes)

### 🎨 Elementos Visuales
- [Cajas de Color con Texto](#-cajas-de-color-con-texto)
- [Ejemplos Antes/Después](#-ejemplos-antesdespués)
- [Diagramas ASCII](#-diagramas-ascii)
- [Badges y Escudos](#-badges-y-escudos)

### 🔔 Mensajes Importantes
- [Consejo Profesional](#-consejo-profesional)
- [Advertencia Crítica](#-advertencia-crítica)
- [Buena Práctica](#-buena-práctica)
- [Objetivo de Aprendizaje](#-objetivo-de-aprendizaje)
- [Error Común](#-error-común)
- [Nota Informativa](#-nota-informativa)

### 📝 Ejercicios y Soluciones
- [Ejercicio con Solución Desplegable](#-ejercicio-con-solución-desplegable)
- [Solución Paso a Paso](#-solución-paso-a-paso)

### 🔗 Enlaces
- [Enlaces Externos](#-enlaces-externos)
- [Enlaces Internos](#-enlaces-internos)
- [Botones de Enlace](#-botones-de-enlace)

### 🖼️ Imágenes
- [Imagen Simple](#-imagen-simple)
- [Imagen Centrada](#-imagen-centrada)
- [Imagen Redimensionada](#-imagen-redimensionada)

### 📦 Secciones Especiales
- [Referencia Rápida](#-referencia-rápida)
- [Resumen Ejecutivo](#-resumen-ejecutivo)
- [Recursos Adicionales](#-recursos-adicionales)
- [Información del Autor](#-información-del-autor)

</details>

---

# 📖 GUÍA DE ELEMENTOS

---

## 🎯 Título Principal

```markdown
<div align="center">

# 🎯 TÍTULO PRINCIPAL DEL DOCUMENTO

### *Subtítulo o descripción breve del contenido*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--10--26-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

</div>
```

**Vista previa:**

<div align="center">

# 🎯 TÍTULO PRINCIPAL DEL DOCUMENTO

### *Subtítulo o descripción breve del contenido*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--10--26-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

</div>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📋 Títulos de Sección

```markdown
## 📋 Título de Sección Principal

### 🔹 Subtítulo de Segundo Nivel

#### 🔸 Subtítulo de Tercer Nivel

##### 📌 Subtítulo de Cuarto Nivel
```

**Vista previa:**

## 📋 Título de Sección Principal

### 🔹 Subtítulo de Segundo Nivel

#### 🔸 Subtítulo de Tercer Nivel

##### 📌 Subtítulo de Cuarto Nivel

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🎯 Subtítulos de Nivel

```markdown
## 🔵 Concepto Principal con Emoji Azul

### 🟢 Concepto Secundario con Emoji Verde

### 🔴 Concepto Crítico con Emoji Rojo

### 🟡 Concepto de Advertencia con Emoji Amarillo
```

**Vista previa:**

## 🔵 Concepto Principal con Emoji Azul

### 🟢 Concepto Secundario con Emoji Verde

### 🔴 Concepto Crítico con Emoji Rojo

### 🟡 Concepto de Advertencia con Emoji Amarillo

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📚 Tabla de Contenidos Desplegable

```markdown
<details>
<summary><b>Click para expandir</b></summary>

- [Sección 1](#sección-1)
- [Sección 2](#sección-2)
  - [Subsección 2.1](#subsección-21)
  - [Subsección 2.2](#subsección-22)
- [Sección 3](#sección-3)

</details>
```

**Vista previa:**

<details>
<summary><b>Click para expandir</b></summary>

- [Introducción](#introducción)
- [Conceptos Fundamentales](#conceptos-fundamentales)
  - [Variables](#variables)
  - [Tipos de Datos](#tipos-de-datos)
- [Ejemplos Prácticos](#ejemplos-prácticos)

</details>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ➖ Separadores Visuales

```markdown
---

***

___

🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```

**Vista previa:**

---

***

___

🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📝 Párrafo Justificado

```markdown
<p align="justify">
Este es un párrafo de texto justificado. El texto se alineará a ambos márgenes,
creando un aspecto más profesional y ordenado. Es ideal para textos largos,
explicaciones teóricas o definiciones importantes que requieren una presentación
formal y estructurada.
</p>
```

**Vista previa:**

<p align="justify">
Este es un párrafo de texto justificado. El texto se alineará a ambos márgenes,
creando un aspecto más profesional y ordenado. Es ideal para textos largos,
explicaciones teóricas o definiciones importantes que requieren una presentación
formal y estructurada.
</p>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ✍️ Formato de Texto Básico

```markdown
**Texto en negrita**

*Texto en cursiva*

***Texto en negrita y cursiva***

`código en línea`

~~Texto tachado~~

**`Negrita con código`**

*`Cursiva con código`*
```

**Vista previa:**

**Texto en negrita**

*Texto en cursiva*

***Texto en negrita y cursiva***

`código en línea`

~~Texto tachado~~

**`Negrita con código`**

*`Cursiva con código`*

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💬 Citas Textuales

```markdown
> "La simplicidad es la máxima sofisticación."
> — Leonardo da Vinci

> 📝 Esta es una cita con emoji para darle énfasis visual.
```

**Vista previa:**

> "La simplicidad es la máxima sofisticación."
> — Leonardo da Vinci

> 📝 Esta es una cita con emoji para darle énfasis visual.

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💻 Código en Línea

```markdown
Usa la función `print()` para mostrar texto en pantalla.

La variable `nombre` almacena un valor de tipo `str`.

Ejecuta el comando `python --version` en tu terminal.
```

**Vista previa:**

Usa la función `print()` para mostrar texto en pantalla.

La variable `nombre` almacena un valor de tipo `str`.

Ejecuta el comando `python --version` en tu terminal.

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔢 Listas Numeradas

```markdown
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
4. Cuarto elemento
```

**Vista previa:**

1. Primer elemento
2. Segundo elemento
3. Tercer elemento
4. Cuarto elemento

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📌 Listas con Viñetas

```markdown
- Primer punto importante
- Segundo punto importante
- Tercer punto importante
  - Subpunto con sangría
  - Otro subpunto
- Cuarto punto principal
```

**Vista previa:**

- Primer punto importante
- Segundo punto importante
- Tercer punto importante
  - Subpunto con sangría
  - Otro subpunto
- Cuarto punto principal

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ✅ Listas de Tareas

```markdown
- [x] Tarea completada
- [x] Otra tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente
```

**Vista previa:**

- [x] Tarea completada
- [x] Otra tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📋 Listas Anidadas

```markdown
1. **Primer paso**: Configuración inicial
   - Instalar Python
   - Verificar versión
   - Configurar IDE
   
2. **Segundo paso**: Crear proyecto
   - Crear directorio
   - Inicializar git
   - Crear archivo principal
     - Importar librerías
     - Definir funciones
     
3. **Tercer paso**: Ejecutar programa
```

**Vista previa:**

1. **Primer paso**: Configuración inicial
   - Instalar Python
   - Verificar versión
   - Configurar IDE
   
2. **Segundo paso**: Crear proyecto
   - Crear directorio
   - Inicializar git
   - Crear archivo principal
     - Importar librerías
     - Definir funciones
     
3. **Tercer paso**: Ejecutar programa

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📊 Tabla Básica

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
| Dato 7    | Dato 8    | Dato 9    |
```

**Vista previa:**

| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
| Dato 7    | Dato 8    | Dato 9    |

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📊 Tabla con Alineación

```markdown
| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto     | Texto  | Texto   |
| Más texto | Más    | Más     |
| Último    | Dato   | Final   |
```

**Explicación:**
- `:---` = Alineación a la izquierda
- `:---:` = Alineación al centro
- `---:` = Alineación a la derecha

**Vista previa:**

| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto     | Texto  | Texto   |
| Más texto | Más    | Más     |
| Último    | Dato   | Final   |

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📊 Tabla con Formato Interno

```markdown
| Tipo de dato | Sintaxis | Ejemplo | Descripción |
|:-------------|:--------:|---------|:------------|
| **Entero**   | `int`    | `42`    | Números sin decimales |
| **Decimal**  | `float`  | `3.14`  | Números con decimales |
| **Texto**    | `str`    | `"Hola"` | Cadenas de caracteres |
| **Booleano** | `bool`   | `True`  | Valores lógicos |
```

**Vista previa:**

| Tipo de dato | Sintaxis | Ejemplo | Descripción |
|:-------------|:--------:|---------|:------------|
| **Entero**   | `int`    | `42`    | Números sin decimales |
| **Decimal**  | `float`  | `3.14`  | Números con decimales |
| **Texto**    | `str`    | `"Hola"` | Cadenas de caracteres |
| **Booleano** | `bool`   | `True`  | Valores lógicos |

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🎨 Tabla con Colores de Fondo

```markdown
<table>
<tr>
<td bgcolor="#E3F2FD">

### Caja azul claro

Este es contenido dentro de una caja con fondo azul claro.
Ideal para conceptos informativos.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#E8F5E9">

### Caja verde claro

Este es contenido dentro de una caja con fondo verde claro.
Ideal para buenas prácticas.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFF9C4">

### Caja amarillo claro

Este es contenido dentro de una caja con fondo amarillo claro.
Ideal para consejos y tips.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFEBEE">

### Caja rojo claro

Este es contenido dentro de una caja con fondo rojo claro.
Ideal para advertencias.

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#E3F2FD">

### Caja azul claro

Este es contenido dentro de una caja con fondo azul claro.
Ideal para conceptos informativos.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#E8F5E9">

### Caja verde claro

Este es contenido dentro de una caja con fondo verde claro.
Ideal para buenas prácticas.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFF9C4">

### Caja amarillo claro

Este es contenido dentro de una caja con fondo amarillo claro.
Ideal para consejos y tips.

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFEBEE">

### Caja rojo claro

Este es contenido dentro de una caja con fondo rojo claro.
Ideal para advertencias.

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📊 Tabla Comparativa

```markdown
| Criterio | Opción A | Opción B | Recomendación |
|:---------|:--------:|:--------:|:-------------:|
| **Velocidad** | ⚡⚡⚡ | ⚡⚡ | Opción A |
| **Simplicidad** | ⭐⭐ | ⭐⭐⭐⭐ | Opción B |
| **Escalabilidad** | ⬆️⬆️⬆️⬆️ | ⬆️⬆️ | Opción A |
| **Costo** | 💰💰💰 | 💰 | Opción B |
```

**Vista previa:**

| Criterio | Opción A | Opción B | Recomendación |
|:---------|:--------:|:--------:|:-------------:|
| **Velocidad** | ⚡⚡⚡ | ⚡⚡ | Opción A |
| **Simplicidad** | ⭐⭐ | ⭐⭐⭐⭐ | Opción B |
| **Escalabilidad** | ⬆️⬆️⬆️⬆️ | ⬆️⬆️ | Opción A |
| **Costo** | 💰💰💰 | 💰 | Opción B |

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💻 Bloque de Código Python

````markdown
```python
# Este es un ejemplo de código Python
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"¡Hola, {nombre}!"

# Uso de la función
mensaje = saludar("Ana")
print(mensaje)
```
````

**Vista previa:**

```python
# Este es un ejemplo de código Python
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"¡Hola, {nombre}!"

# Uso de la función
mensaje = saludar("Ana")
print(mensaje)
```

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💻 Bloque de Código con Comentarios

````markdown
```python
# Declaración de variables
x = 10        # Variable entera
y = 3.14      # Variable decimal
nombre = "Ana" # Variable de texto

# Operaciones matemáticas
suma = x + 5      # suma = 15
producto = x * 2  # producto = 20

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Producto: {producto}")
```
````

**Vista previa:**

```python
# Declaración de variables
x = 10        # Variable entera
y = 3.14      # Variable decimal
nombre = "Ana" # Variable de texto

# Operaciones matemáticas
suma = x + 5      # suma = 15
producto = x * 2  # producto = 20

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Producto: {producto}")
```

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💻 Bloques de Código Múltiples Lenguajes

````markdown
**Python:**
```python
print("Hola Mundo")
```

**JavaScript:**
```javascript
console.log("Hola Mundo");
```

**Bash:**
```bash
echo "Hola Mundo"
```

**JSON:**
```json
{
  "mensaje": "Hola Mundo",
  "idioma": "español"
}
```
````

**Vista previa:**

**Python:**
```python
print("Hola Mundo")
```

**JavaScript:**
```javascript
console.log("Hola Mundo");
```

**Bash:**
```bash
echo "Hola Mundo"
```

**JSON:**
```json
{
  "mensaje": "Hola Mundo",
  "idioma": "español"
}
```

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🎨 Cajas de Color con Texto

```markdown
<table>
<tr>
<td bgcolor="#E3F2FD" style="border-left: 5px solid #2196F3;">

### 📘 Información

<p align="justify">
Este es un bloque informativo con borde azul. Útil para definiciones,
conceptos teóricos o explicaciones generales.
</p>

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#E3F2FD" style="border-left: 5px solid #2196F3;">

### 📘 Información

<p align="justify">
Este es un bloque informativo con borde azul. Útil para definiciones,
conceptos teóricos o explicaciones generales.
</p>

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔄 Ejemplos Antes/Después

```markdown
<table>
<tr>
<td width="50%" bgcolor="#FFF3E0">

**❌ ANTES**

```python
# Código sin optimizar
x = 10
y = 5
z = x + y
print(z)
```

</td>
<td width="50%" bgcolor="#E8F5E9">

**✅ DESPUÉS**

```python
# Código optimizado
suma = lambda x, y: x + y
resultado = suma(10, 5)
print(f"Resultado: {resultado}")
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td width="50%" bgcolor="#FFF3E0">

**❌ ANTES**

```python
# Código sin optimizar
x = 10
y = 5
z = x + y
print(z)
```

</td>
<td width="50%" bgcolor="#E8F5E9">

**✅ DESPUÉS**

```python
# Código optimizado
suma = lambda x, y: x + y
resultado = suma(10, 5)
print(f"Resultado: {resultado}")
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📐 Diagramas ASCII

```markdown
```plaintext
┌─────────────────────────────────────────────────┐
│  ✓ Primera característica importante           │
│  ✓ Segunda característica relevante            │
│  ✓ Tercera característica destacada            │
│  ✓ Cuarta característica fundamental           │
└─────────────────────────────────────────────────┘
```

```plaintext
╔════════════════════════════════════════════════════╗
║  BENCHMARK DE RENDIMIENTO                          ║
╠════════════════════════════════════════════════════╣
║  Lista tradicional:    1000ms  ████████████████    ║
║  Comprensión de lista:  650ms  ██████████          ║
║  Generador:             320ms  █████               ║
║  NumPy array:           120ms  ██                  ║
╚════════════════════════════════════════════════════╝
```
````

**Vista previa:**

```plaintext
┌─────────────────────────────────────────────────┐
│  ✓ Primera característica importante           │
│  ✓ Segunda característica relevante            │
│  ✓ Tercera característica destacada            │
│  ✓ Cuarta característica fundamental           │
└─────────────────────────────────────────────────┘
```

```plaintext
╔════════════════════════════════════════════════════╗
║  BENCHMARK DE RENDIMIENTO                          ║
╠════════════════════════════════════════════════════╣
║  Lista tradicional:    1000ms  ████████████████    ║
║  Comprensión de lista:  650ms  ██████████          ║
║  Generador:             320ms  █████               ║
║  NumPy array:           120ms  ██                  ║
╚════════════════════════════════════════════════════╝
```

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🏷️ Badges y Escudos

```markdown
![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--10--26-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)
```

**Vista previa:**

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--10--26-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 💡 Consejo Profesional

```markdown
<table>
<tr>
<td bgcolor="#FFF9C4" style="border-left: 5px solid #FBC02D;">

### 💡 CONSEJO PROFESIONAL

<p align="justify">
<b>Nomenclatura descriptiva:</b> Utiliza nombres de variables y funciones que sean 
autodescriptivos. Esto mejora significativamente la legibilidad y mantenibilidad 
del código.
</p>

```python
# ❌ Evitar
x = calcular(y, z)

# ✅ Preferir
precio_total = calcular_precio_con_impuestos(precio_base, tasa_impuesto)
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#FFF9C4" style="border-left: 5px solid #FBC02D;">

### 💡 CONSEJO PROFESIONAL

<p align="justify">
<b>Nomenclatura descriptiva:</b> Utiliza nombres de variables y funciones que sean 
autodescriptivos. Esto mejora significativamente la legibilidad y mantenibilidad 
del código.
</p>

```python
# ❌ Evitar
x = calcular(y, z)

# ✅ Preferir
precio_total = calcular_precio_con_impuestos(precio_base, tasa_impuesto)
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ⚠️ Advertencia Crítica

```markdown
<table>
<tr>
<td bgcolor="#FFCCBC" style="border-left: 5px solid #FF5722;">

### ⚠️ ADVERTENCIA CRÍTICA

<p align="justify">
<b>Sensibilidad a mayúsculas:</b> Python distingue entre mayúsculas y minúsculas. 
Las variables <code>Usuario</code>, <code>usuario</code> y <code>USUARIO</code> 
son completamente diferentes.
</p>

```python
nombre = "Ana"    # Variable diferente
Nombre = "Juan"   # Variable diferente
NOMBRE = "Pedro"  # Variable diferente
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#FFCCBC" style="border-left: 5px solid #FF5722;">

### ⚠️ ADVERTENCIA CRÍTICA

<p align="justify">
<b>Sensibilidad a mayúsculas:</b> Python distingue entre mayúsculas y minúsculas. 
Las variables <code>Usuario</code>, <code>usuario</code> y <code>USUARIO</code> 
son completamente diferentes.
</p>

```python
nombre = "Ana"    # Variable diferente
Nombre = "Juan"   # Variable diferente
NOMBRE = "Pedro"  # Variable diferente
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ✅ Buena Práctica

```markdown
<table>
<tr>
<td bgcolor="#C8E6C9" style="border-left: 5px solid #4CAF50;">

### ✅ BUENA PRÁCTICA

<p align="justify">
<b>Validación de tipos:</b> Siempre valida y convierte los tipos de datos antes 
de realizar operaciones para evitar errores en tiempo de ejecución.
</p>

```python
def suma_segura(a, b):
    """Realiza suma con validación de tipos."""
    try:
        return float(a) + float(b)
    except (TypeError, ValueError):
        return "Error: Tipos incompatibles"

resultado = suma_segura(10, "5")  # Resultado: 15.0
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#C8E6C9" style="border-left: 5px solid #4CAF50;">

### ✅ BUENA PRÁCTICA

<p align="justify">
<b>Validación de tipos:</b> Siempre valida y convierte los tipos de datos antes 
de realizar operaciones para evitar errores en tiempo de ejecución.
</p>

```python
def suma_segura(a, b):
    """Realiza suma con validación de tipos."""
    try:
        return float(a) + float(b)
    except (TypeError, ValueError):
        return "Error: Tipos incompatibles"

resultado = suma_segura(10, "5")  # Resultado: 15.0
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🎯 Objetivo de Aprendizaje

```markdown
<table>
<tr>
<td bgcolor="#B2DFDB" style="border-left: 5px solid #009688;">

### 🎯 OBJETIVO DE APRENDIZAJE

<p align="justify">
Al completar esta sección, deberás ser capaz de:
</p>

- [x] Comprender los conceptos fundamentales del tema
- [x] Aplicar las técnicas presentadas en casos prácticos
- [x] Identificar y evitar errores comunes
- [x] Optimizar el código siguiendo las mejores prácticas
- [ ] Crear proyectos propios utilizando estos conocimientos

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#B2DFDB" style="border-left: 5px solid #009688;">

### 🎯 OBJETIVO DE APRENDIZAJE

<p align="justify">
Al completar esta sección, deberás ser capaz de:
</p>

- [x] Comprender los conceptos fundamentales del tema
- [x] Aplicar las técnicas presentadas en casos prácticos
- [x] Identificar y evitar errores comunes
- [x] Optimizar el código siguiendo las mejores prácticas
- [ ] Crear proyectos propios utilizando estos conocimientos

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## ❌ Error Común

```markdown
<table>
<tr>
<td bgcolor="#FFCDD2" style="border-left: 5px solid #F44336;">

### ❌ ERROR COMÚN

<p align="justify">
<b>Problema:</b> Intentar sumar tipos incompatibles sin conversión.
</p>

```python
# ❌ Esto genera un TypeError
x = 10
y = "5"
resultado = x + y  # Error!
```

<p align="justify">
<b>Solución:</b> Convertir los tipos antes de operar.
</p>

```python
# ✅ Forma correcta
x = 10
y = "5"
resultado = x + int(y)  # Resultado: 15
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#FFCDD2" style="border-left: 5px solid #F44336;">

### ❌ ERROR COMÚN

<p align="justify">
<b>Problema:</b> Intentar sumar tipos incompatibles sin conversión.
</p>

```python
# ❌ Esto genera un TypeError
x = 10
y = "5"
resultado = x + y  # Error!
```

<p align="justify">
<b>Solución:</b> Convertir los tipos antes de operar.
</p>

```python
# ✅ Forma correcta
x = 10
y = "5"
resultado = x + int(y)  # Resultado: 15
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📝 Nota Informativa

```markdown
<table>
<tr>
<td bgcolor="#E1F5FE" style="border-left: 5px solid #03A9F4;">

### 📝 NOTA INFORMATIVA

<p align="justify">
Python utiliza <b>tipado dinámico</b>, lo que significa que el tipo de una variable
se determina automáticamente en tiempo de ejecución según el valor asignado.
</p>

```python
# El tipo se asigna automáticamente
x = 10        # x es int
x = "texto"   # Ahora x es str
x = 3.14      # Ahora x es float
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#E1F5FE" style="border-left: 5px solid #03A9F4;">

### 📝 NOTA INFORMATIVA

<p align="justify">
Python utiliza <b>tipado dinámico</b>, lo que significa que el tipo de una variable
se determina automáticamente en tiempo de ejecución según el valor asignado.
</p>

```python
# El tipo se asigna automáticamente
x = 10        # x es int
x = "texto"   # Ahora x es str
x = 3.14      # Ahora x es float
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📝 Ejercicio con Solución Desplegable

```markdown
<table>
<tr>
<td bgcolor="#E8F5E9" style="border-left: 5px solid #4CAF50;">

### 📝 EJERCICIO 1: Nivel Básico

**Objetivo:** Crear una función que calcule el factorial de un número.

**Requisitos:**
- Usar recursividad
- Validar entrada
- Manejar casos especiales

<details>
<summary><b>💡 Ver solución</b></summary>

```python
def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número entero positivo
        
    Returns:
        int: Factorial de n
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Debe ser un entero positivo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Prueba
print(factorial(5))  # Salida: 120
```

</details>

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#E8F5E9" style="border-left: 5px solid #4CAF50;">

### 📝 EJERCICIO 1: Nivel Básico

**Objetivo:** Crear una función que calcule el factorial de un número.

**Requisitos:**
- Usar recursividad
- Validar entrada
- Manejar casos especiales

<details>
<summary><b>💡 Ver solución</b></summary>

```python
def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número entero positivo
        
    Returns:
        int: Factorial de n
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Debe ser un entero positivo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Prueba
print(factorial(5))  # Salida: 120
```

</details>

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔧 Solución Paso a Paso

```markdown
<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #2196F3;">

**PASO 1: Configuración inicial**

```python
# Importar dependencias necesarias
import numpy as np
import pandas as pd

# Configurar parámetros
config = {
    'version': '1.0',
    'debug': True,
    'timeout': 30
}
```

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #4CAF50;">

**PASO 2: Procesamiento de datos**

```python
# Cargar y procesar datos
def procesar_datos(archivo):
    """Procesa los datos del archivo especificado."""
    datos = pd.read_csv(archivo)
    datos_limpios = datos.dropna()
    return datos_limpios
```

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #FF9800;">

**PASO 3: Análisis y resultados**

```python
# Realizar análisis
resultados = {
    'media': datos_limpios.mean(),
    'desviacion': datos_limpios.std()
}

# Mostrar resultados
for clave, valor in resultados.items():
    print(f"{clave}: {valor}")
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #2196F3;">

**PASO 1: Configuración inicial**

```python
# Importar dependencias necesarias
import numpy as np
import pandas as pd

# Configurar parámetros
config = {
    'version': '1.0',
    'debug': True,
    'timeout': 30
}
```

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #4CAF50;">

**PASO 2: Procesamiento de datos**

```python
# Cargar y procesar datos
def procesar_datos(archivo):
    """Procesa los datos del archivo especificado."""
    datos = pd.read_csv(archivo)
    datos_limpios = datos.dropna()
    return datos_limpios
```

</td>
</tr>
</table>

<table>
<tr>
<td bgcolor="#FFFFFF" style="border-left: 4px solid #FF9800;">

**PASO 3: Análisis y resultados**

```python
# Realizar análisis
resultados = {
    'media': datos_limpios.mean(),
    'desviacion': datos_limpios.std()
}

# Mostrar resultados
for clave, valor in resultados.items():
    print(f"{clave}: {valor}")
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔗 Enlaces Externos

```markdown
[Texto del enlace](https://www.ejemplo.com)

[Documentación oficial de Python](https://docs.python.org)

[Tutorial de NumPy](https://numpy.org/doc/)
```

**Vista previa:**

[Texto del enlace](https://www.ejemplo.com)

[Documentación oficial de Python](https://docs.python.org)

[Tutorial de NumPy](https://numpy.org/doc/)

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔗 Enlaces Internos

```markdown
[Ir a la sección de tablas](#-tabla-básica)

[Volver al inicio](#-plantilla-de-referencia-markdown)

[Ver ejemplos de código](#-bloque-de-código-python)
```

**Vista previa:**

[Ir a la sección de tablas](#-tabla-básica)

[Volver al inicio](#-plantilla-de-referencia-markdown)

[Ver ejemplos de código](#-bloque-de-código-python)

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🔘 Botones de Enlace

```markdown
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ejemplo@email.com)
```

**Vista previa:**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ejemplo@email.com)

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🖼️ Imagen Simple

```markdown
![Texto alternativo](ruta/a/la/imagen.png)

![Logo de Python](https://www.python.org/static/community_logos/python-logo.png)
```

**Vista previa:**

![Logo de Python](https://www.python.org/static/community_logos/python-logo.png)

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🖼️ Imagen Centrada

```markdown
<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" />
</p>
```

**Vista previa:**

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" />
</p>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 🖼️ Imagen Redimensionada

```markdown
<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="300"/>

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="400"/>
</p>
```

**Vista previa:**

<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="300"/>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📚 Referencia Rápida

```markdown
<table>
<tr>
<td width="50%" bgcolor="#E1F5FE">

### 🔤 SINTAXIS BÁSICA

```python
# Variables
nombre = "valor"
numero = 42

# Condicionales
if condicion:
    # código
    
# Bucles
for item in lista:
    print(item)
```

</td>
<td width="50%" bgcolor="#F3E5F5">

### 🛠️ FUNCIONES ÚTILES

```python
# Función básica
def mi_funcion(param):
    return param * 2

# Lambda
cuadrado = lambda x: x ** 2

# List comprehension
numeros = [x for x in range(10)]
```

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td width="50%" bgcolor="#E1F5FE">

### 🔤 SINTAXIS BÁSICA

```python
# Variables
nombre = "valor"
numero = 42

# Condicionales
if condicion:
    # código
    
# Bucles
for item in lista:
    print(item)
```

</td>
<td width="50%" bgcolor="#F3E5F5">

### 🛠️ FUNCIONES ÚTILES

```python
# Función básica
def mi_funcion(param):
    return param * 2

# Lambda
cuadrado = lambda x: x ** 2

# List comprehension
numeros = [x for x in range(10)]
```

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📊 Resumen Ejecutivo

```markdown
<table>
<tr>
<td bgcolor="#E3F2FD">

### 🎯 Puntos Clave

<div align="center">

```plaintext
╔═══════════════════════════════════════════════════════╗
║                   CONCEPTOS ESENCIALES                 ║
╠═══════════════════════════════════════════════════════╣
║                                                        ║
║  1️⃣  Fundamentos teóricos y definiciones base        ║
║                                                        ║
║  2️⃣  Aplicaciones prácticas en proyectos reales      ║
║                                                        ║
║  3️⃣  Optimización y mejores prácticas                ║
║                                                        ║
╚═══════════════════════════════════════════════════════╝
```

</div>

### 🚀 Próximos Pasos

1. **Practica con ejercicios**
2. **Crea proyectos personales**
3. **Lee código de otros**
4. **Participa en comunidades**

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#E3F2FD">

### 🎯 Puntos Clave

<div align="center">

```plaintext
╔═══════════════════════════════════════════════════════╗
║                   CONCEPTOS ESENCIALES                 ║
╠═══════════════════════════════════════════════════════╣
║                                                        ║
║  1️⃣  Fundamentos teóricos y definiciones base        ║
║                                                        ║
║  2️⃣  Aplicaciones prácticas en proyectos reales      ║
║                                                        ║
║  3️⃣  Optimización y mejores prácticas                ║
║                                                        ║
╚═══════════════════════════════════════════════════════╝
```

</div>

### 🚀 Próximos Pasos

1. **Practica con ejercicios**
2. **Crea proyectos personales**
3. **Lee código de otros**
4. **Participa en comunidades**

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 📚 Recursos Adicionales

```markdown
<table>
<tr>
<td bgcolor="#F5F5F5">

### 🌐 Documentación Oficial

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/doc/)

</div>

### 📺 Tutoriales Recomendados

| Recurso | Nivel | Duración |
|:--------|:-----:|:--------:|
| **Tutorial Python** | Principiante | 5h |
| **Real Python** | Intermedio | Variable |
| **Python Avanzado** | Avanzado | 10h |

### 💬 Comunidades

- 🌍 Stack Overflow - Preguntas y respuestas
- 💬 Reddit r/learnpython - Comunidad de aprendizaje
- 🐦 Python en Twitter - Noticias

</td>
</tr>
</table>
```

**Vista previa:**

<table>
<tr>
<td bgcolor="#F5F5F5">

### 🌐 Documentación Oficial

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/doc/)

</div>

### 📺 Tutoriales Recomendados

| Recurso | Nivel | Duración |
|:--------|:-----:|:--------:|
| **Tutorial Python** | Principiante | 5h |
| **Real Python** | Intermedio | Variable |
| **Python Avanzado** | Avanzado | 10h |

### 💬 Comunidades

- 🌍 Stack Overflow - Preguntas y respuestas
- 💬 Reddit r/learnpython - Comunidad de aprendizaje
- 🐦 Python en Twitter - Noticias

</td>
</tr>
</table>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

## 👤 Información del Autor

```markdown
<div align="center">

## 📬 INFORMACIÓN DEL DOCUMENTO

<table>
<tr>
<td align="center" bgcolor="#263238" style="color: white;">

### 👤 AUTOR

**Juanan Comins**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juanantoniocomins)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tu-email@ejemplo.com)

</td>
</tr>
</table>

<table>
<tr>
<td align="center" width="33%" bgcolor="#1565C0" style="color: white;">

📅 **FECHA**

26 de octubre de 2025

</td>
<td align="center" width="33%" bgcolor="#43A047" style="color: white;">

📌 **VERSIÓN**

1.0 - Estable

</td>
<td align="center" width="34%" bgcolor="#E53935" style="color: white;">

⚖️ **LICENCIA**

MIT License

</td>
</tr>
</table>

</div>
```

**Vista previa:**

<div align="center">

## 📬 INFORMACIÓN DEL DOCUMENTO

<table>
<tr>
<td align="center" bgcolor="#263238" style="color: white;">

### 👤 AUTOR

**Juanan Comins**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juanantoniocomins)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tu-email@ejemplo.com)

</td>
</tr>
</table>

<table>
<tr>
<td align="center" width="33%" bgcolor="#1565C0" style="color: white;">

📅 **FECHA**

26 de octubre de 2025

</td>
<td align="center" width="33%" bgcolor="#43A047" style="color: white;">

📌 **VERSIÓN**

1.0 - Estable

</td>
<td align="center" width="34%" bgcolor="#E53935" style="color: white;">

⚖️ **LICENCIA**

MIT License

</td>
</tr>
</table>

</div>

[⬆️ Volver al índice](#-índice-de-elementos-disponibles)

---

<div align="center">

## 🎨 PALETA DE COLORES DISPONIBLES

### Colores Claros (Fondos)

| Color | Código | Uso Recomendado |
|:------|:------:|:----------------|
| 🔵 Azul claro | `#E3F2FD` | Información, conceptos |
| 🟢 Verde claro | `#E8F5E9` | Buenas prácticas, éxito |
| 🟡 Amarillo claro | `#FFF9C4` | Consejos, tips |
| 🔴 Rojo claro | `#FFEBEE` | Advertencias, errores |
| 🟣 Morado claro | `#F3E5F5` | Código alternativo |
| 🟠 Naranja claro | `#FFF3E0` | Código antes/sin optimizar |
| 🔷 Cian claro | `#E1F5FE` | Notas informativas |
| 🟩 Verde agua | `#B2DFDB` | Objetivos, metas |

### Colores Oscuros (Bordes)

| Color | Código | Uso Recomendado |
|:------|:------:|:----------------|
| 🔵 Azul | `#2196F3` | Información |
| 🟢 Verde | `#4CAF50` | Éxito, correcto |
| 🟡 Amarillo | `#FBC02D` | Consejos |
| 🔴 Rojo | `#FF5722` | Advertencias |
| 🟠 Naranja | `#FF9800` | Pasos intermedios |
| 🔷 Cian | `#03A9F4` | Notas |
| 🟩 Verde agua | `#009688` | Objetivos |

</div>

---

<div align="center">

## ✅ CHECKLIST DE USO

<table>
<tr>
<td bgcolor="#F5F5F5">

### Antes de publicar tu documento, verifica:

- [ ] Título principal claro y descriptivo
- [ ] Índice con enlaces internos funcionales
- [ ] Badges de versión, fecha y estado actualizados
- [ ] Código con sintaxis resaltada correctamente
- [ ] Mensajes importantes con colores apropiados
- [ ] Ejercicios con soluciones desplegables (si aplica)
- [ ] Tablas formateadas correctamente
- [ ] Enlaces externos funcionando
- [ ] Información del autor actualizada
- [ ] Todos los enlaces "Volver al índice" funcionando

</td>
</tr>
</table>

</div>

---

<div align="center">

<sub>© 2025 Juanan Comins. Plantilla de referencia para documentación técnica.</sub>

<sub>Hecho con 💙 para la comunidad de Python</sub>

</div>

<!-- Fin del documento -->
