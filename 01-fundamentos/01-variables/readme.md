<div align="center">

# 💾 **Variables en Python**

### *Guía técnica y profesional sobre la asignación y manejo de variables en Python*

![Versión](https://img.shields.io/badge/Versión-1.0-1565C0?style=for-the-badge)
![Actualización](https://img.shields.io/badge/Actualizado-2025--10--31-43A047?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Estable-00C853?style=for-the-badge)

</div>

---

<p align="justify">

Una **variable** es un espacio en memoria utilizado para **almacenar datos** que pueden ser modificados o reutilizados a lo largo de un programa.  
En Python, las variables funcionan como **etiquetas simbólicas** que apuntan a objetos en memoria, sin necesidad de declarar su tipo previamente.  
Esto se debe a que Python es un lenguaje **dinámicamente tipado**, lo que significa que el tipo de dato se infiere automáticamente al asignar el valor.

</p>

---

## 🧩 **Características principales**

- No es necesario indicar el tipo de dato al declarar la variable.  
- Pueden cambiar de tipo según el valor asignado.  
- Todo en Python es un **objeto**, y las variables son referencias a esos objetos.  

---

## 🧠 **Reglas para nombres de variables**

| Regla | Descripción |
|--------|--------------|
| ✅ **Caracteres válidos** | Letras (`a-z`, `A-Z`), números (`0-9`) y guiones bajos (`_`) |
| 🚫 **Inicio** | Deben comenzar con una letra o guion bajo (**no con un número**) |
| 🔠 **Sensibilidad** | Son sensibles a mayúsculas/minúsculas → `edad` ≠ `Edad` |
| ⛔ **Palabras reservadas** | No pueden usar *keywords* de Python (`if`, `for`, `class`, etc.)|

---

## 🧰 **Buenas prácticas**

- Usar nombres **descriptivos y claros** → `edad_usuario` mejor que `x`.  
- Evitar cambiar el **tipo de dato** de una variable durante su uso.  
- No usar nombres de **una sola letra** excepto en bucles (`i`, `j`, `k`).  
- Preferir **nombres en inglés** en proyectos colaborativos o de equipo.  

---

## ⚙️ **Declaración y asignación**

```python
# Asignación simple
nombre_variable = valor

# Asignación múltiple del mismo valor
var1 = var2 = var3 = valor

# Asignación múltiple con distintos valores
var1, var2, var3 = valor1, valor2, valor3

nombre = "Juanan"
edad = 30
altura = 1.80
activo = True

# Asignación múltiple
x = y = z = 0

# Desempaquetado múltiple
a, b, c = 10, 20, 30

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

