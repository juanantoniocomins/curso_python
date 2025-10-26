# 🧠 TÍTULO PRINCIPAL DEL DOCUMENTO
> Breve descripción o resumen del contenido.  
> *(Opcional: puedes incluir fecha o versión)*  
> **Fecha:** 2025-10-26  
> **Versión:** 1.0  

---

## 🧩 1. PRIMER NIVEL DE SECCIÓN

<p align="justify">
Este es el párrafo principal justificado.  
Aquí puedes introducir el tema general, los objetivos o la idea central de esta sección.  
El texto se mostrará alineado a ambos márgenes, lo que facilita la lectura en temas más extensos o teóricos.
Puedes usar **negritas** para resaltar términos clave o *cursivas* para definiciones o notas importantes.
</p>

### 🔹 1.1. Subtítulo de segundo nivel
<p align="justify">
Este nivel es ideal para desarrollar conceptos secundarios o explicaciones más concretas.  
Puedes incluir ejemplos, fórmulas o pasos específicos de un procedimiento técnico.
</p>

#### 🔸 1.1.1. Subtítulo de tercer nivel
<p align="justify">
Aquí puedes detallar aún más, por ejemplo casos prácticos, detalles de configuración o fragmentos de código.
</p>

---

## 📋 2. LISTAS DE EJEMPLO

### Lista numerada
1. Primer paso o concepto
2. Segundo paso
3. Tercer paso

### Lista con viñetas
- Punto importante
- Otro elemento
  - Subnivel con sangría
- Último punto

### Lista de tareas
- [x] Concepto comprendido
- [ ] Pendiente de repasar
- [ ] Añadir ejemplo práctico

---

## 📊 3. TABLAS CON CABECERA

### Tabla básica
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |

### Tabla con alineación
| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto     | Texto  | Texto   |
| Más texto | Más    | Más     |

### Tabla con formato interno
| Tipo de dato | Sintaxis | Ejemplo |
|:-------------|:--------:|---------|
| **Entero**   | `int`    | `42`    |
| **Decimal**  | `float`  | `3.14`  |
| **Texto**    | `str`    | `"Hola"` |
| **Booleano** | `bool`   | `True`  |

**Explicación de alineación:**
- `:---` = Alineación a la izquierda
- `:---:` = Alineación al centro
- `---:` = Alineación a la derecha

---

## ✍️ 4. TEXTO Y FORMATO

### Formato de texto básico
- **Negrita** para resaltar términos clave: `**texto**` → **importante**
- *Cursiva* para definiciones o notas: `*texto*` → *definición*
- `Código` para variables o comandos cortos: `` `código` `` → `variable_nombre`
- ~~Tachado~~ para correcciones o cambios: `~~texto~~` → ~~obsoleto~~

### Combinaciones
- **Negrita y *cursiva combinadas*** → `**negrita y *cursiva***`
- **`Negrita con código`** → `**`código`**`
- *`Cursiva con código`* → `*`código`*`

### Notas y bloques informativos

> 📝 **Nota:** Este es un bloque de nota general.  
> Puedes añadir información adicional o aclaraciones aquí.

> ⚠️ **Advertencia:** Ten cuidado con este aspecto.  
> Puede causar errores si no se maneja correctamente.

> ✅ **Tip:** Consejo práctico o buena práctica.  
> Esto te ayudará a mejorar tu código.

> ❌ **Error común:** Descripción del error frecuente.  
> Evita hacer esto en tu código.

> 💡 **Ejemplo:** Caso práctico o demostración.  
> Observa cómo se aplica este concepto.

> 🔍 **Información adicional:** Datos complementarios.  
> Para usuarios avanzados o curiosos.

---

## 💻 5. BLOQUES DE CÓDIGO

### Código en línea
Usa la función `print()` para mostrar un mensaje en pantalla.

### Bloque de código simple (sin resaltado)
Este es un bloque de código sin resaltado de sintaxis.
Útil para mostrar texto plano o pseudocódigo.

### Bloque de código con resaltado de sintaxis (Python)
Ejemplo de variables en Python
nombre = "Juan"
edad = 25
es_estudiante = True

Función simple
def saludar(nombre):
return f"Hola, {nombre}!"

Uso de la función
mensaje = saludar(nombre)
print(mensaje)

### Bloque de código con comentarios explicativos
Declaración de variables
x = 10 # Variable entera
y = 3.14 # Variable decimal
nombre = "Ana" # Variable de texto

Operaciones
suma = x + 5 # suma = 15
print(suma) # Imprime: 15

### Otros lenguajes soportados
Bash/Terminal
python --version
pip install numpy
undefined
{
"nombre": "Python",
"version": "3.12",
"activo": true
}

📦 7. CAJAS O BLOQUES INFORMATIVOS
Usando citas (blockquotes)
💡 CONSEJO
Usa nombres de variables descriptivos para mejorar la legibilidad del código.
Ejemplo: precio_total es mejor que pt.

⚠️ IMPORTANTE
Python es sensible a mayúsculas y minúsculas.
variable y Variable son diferentes.

❌ ERROR COMÚN
No puedes sumar directamente un entero y un string:

text
x = 10
y = "5"
resultado = x + y  # TypeError
✅ SOLUCIÓN
Convierte el tipo antes de operar:

text
x = 10
y = "5"
resultado = x + int(y)  # 15
📚 CONCEPTO CLAVE
Tipado dinámico: Python determina el tipo de variable automáticamente en tiempo de ejecución.

🎯 OBJETIVO
Al finalizar esta sección deberás:

Comprender qué es una variable

Saber declarar variables correctamente

Conocer los tipos de datos básicos

📐 8. SEPARADORES VISUALES
Separador simple
Separador con línea
Separador alternativo
Separador con emoji
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹

🖼️ 9. IMÁGENES
Imagen simple
Texto alternativo

Imagen con título
Logo de Python

Imagen con enlace
Texto alternativo

Imagen centrada con HTML
<p align="center"> <img src="./imagen.png" alt="Descripción" width="500"/> </p>
Imagen redimensionada
<img src="./imagen.png" alt="Descripción" width="300" height="200"/>
📝 10. EJEMPLO COMPLETO DE SECCIÓN
<p align="justify"> Las <strong>variables</strong> son contenedores de datos que permiten almacenar información en memoria. En Python, las variables utilizan <em>tipado dinámico</em>, lo que significa que no es necesario declarar explícitamente su tipo. </p>
Declaración de variables
text
# Variables numéricas
edad = 25              # int
altura = 1.75          # float

# Variables de texto
nombre = "Ana"         # str

# Variables booleanas
es_estudiante = True   # bool
💡 Tip: Usa la función type() para verificar el tipo de una variable:

text
print(type(edad))  # <class 'int'>

Tabla de tipos de datos
Tipo	Descripción	Ejemplo	Uso común
int	Números enteros	42	Contadores, edades
float	Números decimales	3.14	Precios, medidas
str	Cadenas de texto	"Hola"	Nombres, mensajes
bool	Valores lógicos	True	Condiciones, flags
⚠️ Advertencia: Python es fuertemente tipado. No puedes sumar directamente tipos incompatibles:

text
x = 10
y = "5"
print(x + y)  # ❌ TypeError
Enlaces útiles
Documentación oficial de Python

PEP 8 - Guía de estilo

🔄 11. ELEMENTOS ADICIONALES
Líneas de código destacadas
Para resaltar variables o comandos importantes en el texto: usa variable_nombre o python --version.

Citas textuales
"La simplicidad es la máxima sofisticación."
— Leonardo da Vinci

Listas anidadas con código
Primer paso: Instalar Python

text
sudo apt install python3
Segundo paso: Verificar instalación

text
python3 --version
Tercer paso: Crear primer programa

Abre un editor

Escribe print("Hola Mundo")

Guarda como hola.py

Tabla con código y formato
Operador	Nombre	Ejemplo	Resultado
+	Suma	5 + 3	8
-	Resta	5 - 3	2
*	Multiplicación	5 * 3	15
/	División	5 / 2	2.5
//	División entera	5 // 2	2
%	Módulo	5 % 2	1
**	Potencia	5 ** 2	25
📚 12. RECURSOS Y REFERENCIAS
Documentación oficial
Python Docs

PEP 8 Style Guide

Tutoriales recomendados
Real Python

W3Schools Python

Comunidad
Stack Overflow

Reddit r/learnpython

✅ 13. RESUMEN Y CONCLUSIÓN
<p align="justify"> En este documento hemos cubierto los conceptos fundamentales de [tema principal]. Los puntos clave a recordar son: </p>
Primer concepto: Breve explicación

Segundo concepto: Breve explicación

Tercer concepto: Breve explicación

🎯 Próximos pasos:

 Practicar con los ejercicios propuestos

 Revisar la documentación oficial

 Crear un proyecto personal aplicando lo aprendido

📌 PIE DE DOCUMENTO
<div align="center">
✍️ Autor: Juanan Comins
📅 Última actualización: 26 de octubre de 2025
📁 Repositorio: github.com/juanantoniocomins
📧 Contacto: tu-email@ejemplo.com
⭐ Licencia: MIT License

</div> <!-- Espacio final para mejor visualización -->
<!-- Fin del documento -->
text

***

## 🎨 **GUÍA RÁPIDA DE REFERENCIA**

### Tablas
```markdown
| Columna 1 | Columna 2 | Columna 3 |
|:----------|:---------:|----------:|
| Izquierda | Centro    | Derecha   |
Formato de texto
text
**negrita** *cursiva* `código` ~~tachado~~
Bloques de código
text
```
# Tu código aquí
print("Hola")
```
```

### Notas informativas
```markdown
> 💡 **Nota:** Tu mensaje aquí
```

### Enlaces
```markdown
[Texto](URL)
[Texto](#seccion-interna)
```

### Imágenes
```markdown
![Alt](ruta/imagen.png)
```

📌 PIE DE DOCUMENTO
<div align="center">

✍️ Autor: Juanan Comins
📅 Última actualización: 26 de octubre de 2025
📁 Repositorio: github.com/juanantoniocomins

📧 Contacto: tu-email@ejemplo.com

⭐ Licencia: MIT License

</div>
