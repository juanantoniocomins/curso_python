# 📝 Variables en Python

## 🔍 ¿Qué son las variables?

Las variables son espacios en memoria que almacenan datos. En Python, no necesitas declarar el tipo de variable explícitamente.

---

## 📌 Conceptos clave

### Creación de variables
```python
# Sintaxis básica
nombre_variable = valor

# Ejemplos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True
```

### Reglas para nombres de variables

✅ **Permitido**:
- Letras (a-z, A-Z)
- Números (0-9), pero no al inicio
- Guiones bajos (_)

❌ **No permitido**:
- Comenzar con números
- Usar palabras reservadas (`if`, `for`, `while`, etc.)
- Espacios en blanco
- Caracteres especiales (@, #, %, etc.)
```python
# ✅ Correcto
mi_variable = 10
nombre_completo = "Ana García"
edad2 = 30

# ❌ Incorrecto
2edad = 30        # No puede empezar con número
mi-variable = 10  # No se permiten guiones
for = 5           # 'for' es palabra reservada
```

---

## 🎨 Convenciones de nomenclatura

### Snake Case (Recomendado en Python)
```python
nombre_completo = "Juan Pérez"
edad_usuario = 25
total_compra = 150.50
```

### Camel Case
```python
nombreCompleto = "Juan Pérez"
edadUsuario = 25
totalCompra = 150.50
```

### Pascal Case (para clases)
```python
class NombreClase:
    pass
```

---

## 💡 Tipos de variables

### Variables numéricas
```python
# Enteros (int)
edad = 25
habitantes = 1000000

# Decimales (float)
precio = 19.99
temperatura = -5.3

# Complejos (complex)
numero_complejo = 3 + 4j
```

### Variables de texto
```python
# Strings (str)
nombre = "Ana"
apellido = 'García'
descripcion = """
Este es un texto
en varias líneas
"""
```

### Variables booleanas
```python
# Boolean (bool)
es_mayor_edad = True
tiene_descuento = False
```

---

## 🔄 Asignación múltiple
```python
# Asignar el mismo valor a múltiples variables
x = y = z = 0

# Asignar diferentes valores
nombre, edad, ciudad = "Juan", 25, "Madrid"

# Intercambiar valores
a, b = 10, 20
a, b = b, a  # Ahora a=20 y b=10
```

---

## 🧪 Verificar tipo de variable
```python
nombre = "Juan"
edad = 25

print(type(nombre))  # <class 'str'>
print(type(edad))    # <class 'int'>
```

---

## ⚠️ Errores comunes

### 1. Variable no definida
```python
# ❌ Error
print(nombre)  # NameError: name 'nombre' is not defined

# ✅ Correcto
nombre = "Juan"
print(nombre)
```

### 2. Reasignación de tipo
```python
# Python permite cambiar el tipo de una variable
numero = 10        # int
numero = "diez"    # ahora es str
# Esto es válido pero puede causar confusión
```

---

## 🎯 Buenas prácticas

1. **Usa nombres descriptivos**
```python
   # ❌ Evita
   x = 25
   
   # ✅ Mejor
   edad_usuario = 25
```

2. **Evita nombres de una letra** (excepto en bucles)
```python
   # ❌ Evita
   n = "Juan"
   
   # ✅ Mejor
   nombre = "Juan"
```

3. **Usa MAYÚSCULAS para constantes**
```python
   PI = 3.14159
   MAX_INTENTOS = 3
   RUTA_BASE = "/home/usuario"
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Variable** | Espacio en memoria para almacenar datos |
| **Asignación** | Usar el operador `=` para dar valor |
| **Tipo dinámico** | Python infiere el tipo automáticamente |
| **Snake case** | Convención recomendada en Python |

---

## 🏋️ Ejercicio rápido

Crea variables para almacenar:
- Tu nombre
- Tu edad
- Tu altura
- Si eres estudiante
```python
# Tu código aquí
```

---

## ➡️ Siguiente tema

[Tipos de datos](02_tipos_datos.md)

---

<p align="center">
  <a href="../README.md">🔙 Volver al módulo</a>
</p>
