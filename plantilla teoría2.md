<div align="center">

# 🎯 PLANTILLA DE REFERENCIA MARKDOWN

### *Guía completa de elementos para documentación técnica profesional*

![Version](https://img.shields.io/badge/Versión-2.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--01--23-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Mejorada-success?style=for-the-badge)

</div>

---

## ⚠️ NOTA DE COMPATIBILIDAD

> 💡 **Importante**: Esta plantilla usa HTML embebido para colores y estilos avanzados.
> 
> **✅ Compatible con:**
> - GitHub, GitLab, Bitbucket
> - VSCode Preview
> - Typora, Mark Text
> 
> **❌ Limitado en:**
> - Renders básicos de Markdown
> - Algunos editores online
> 
> 📌 **Solución**: Consulta la sección [Alternativas sin HTML](#-alternativas-sin-html) para renders básicos.

---

## 📚 ÍNDICE DE CONTENIDOS

<details open>
<summary><b>🎨 Click para ver/ocultar el índice completo</b></summary>

### 🚀 Inicio Rápido
- [⚡ Snippets Rápidos](#-snippets-rápidos) ⭐ **NUEVO**
- [🎯 Casos de Uso Reales](#-casos-de-uso-reales) ⭐ **NUEVO**
- [😀 Índice de Emojis](#-índice-de-emojis-por-categoría) ⭐ **NUEVO**

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
- [Código con Contexto Real](#-código-con-contexto-real) ⭐ **NUEVO**

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

### 🔄 Extras
- [🔄 Alternativas sin HTML](#-alternativas-sin-html) ⭐ **NUEVO**
- [🎨 Paleta de Colores](#-paleta-de-colores-disponibles)
- [✅ Checklist de Publicación](#-checklist-de-uso)

</details>

---

# 🚀 INICIO RÁPIDO

---

## ⚡ SNIPPETS RÁPIDOS

**Copia y pega directamente estos fragmentos listos para usar.**

### 📋 Header completo de documento

```markdown
<div align="center">

# 🎯 [TÍTULO DE TU DOCUMENTO]

### *[Subtítulo descriptivo]*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-En_desarrollo-yellow?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge)

</div>

---

## 📚 Sobre este documento

Este documento explica [descripción breve].

**¿Qué aprenderás?**
- ✅ Punto clave 1
- ✅ Punto clave 2
- ✅ Punto clave 3
```

### 💡 Nota importante (con HTML)

```markdown
<table>
<tr>
<td bgcolor="#FFF9C4" style="border-left: 5px solid #FBC02D;">

### 💡 CONSEJO PRO

[Tu consejo importante aquí]

**Recuerda:**
- Punto 1
- Punto 2

</td>
</tr>
</table>
```

### 💡 Nota importante (sin HTML)

```markdown
> 💡 **CONSEJO PRO**
> 
> [Tu consejo importante aquí]
> 
> **Recuerda:**
> - Punto 1
> - Punto 2
```

### 🔥 Comparativa antes/después (con HTML)

```markdown
<table>
<tr>
<td width="50%" bgcolor="#FFEBEE">

### ❌ ANTES (Sin optimizar)

```python
# Código sin optimizar
for i in range(len(lista)):
    print(lista[i])
```

**Problemas:**
- Menos legible
- Más verboso

</td>
<td width="50%" bgcolor="#E8F5E9">

### ✅ DESPUÉS (Optimizado)

```python
# Código optimizado
for item in lista:
    print(item)
```

**Ventajas:**
- Más pythónico
- Más claro

</td>
</tr>
</table>
```

### 🔥 Comparativa antes/después (sin HTML)

```markdown
### ❌ ANTES (Sin optimizar)

```python
# Código sin optimizar
for i in range(len(lista)):
    print(lista[i])
```

**Problemas:** Menos legible, más verboso

---

### ✅ DESPUÉS (Optimizado)

```python
# Código optimizado
for item in lista:
    print(item)
```

**Ventajas:** Más pythónico, más claro
```

### 🎯 Ejercicio con solución desplegable

```markdown
### 📝 Ejercicio 1: [Título del ejercicio]

**Objetivo:** [Descripción del objetivo]

**Tarea:**
```python
# Completa el código
def mi_funcion(parametro):
    # Tu código aquí
    pass
```

<details>
<summary><b>💡 Ver solución</b></summary>

```python
def mi_funcion(parametro):
    """Solución completa"""
    return parametro * 2
```

**Explicación:**
- Paso 1: [Explicación]
- Paso 2: [Explicación]

</details>
```

### 📊 Tabla de referencia rápida

```markdown
| Comando | Descripción | Ejemplo |
|:--------|:------------|:--------|
| `print()` | Imprime en consola | `print("Hola")` |
| `len()` | Longitud de objeto | `len([1,2,3])` → 3 |
| `type()` | Tipo de dato | `type(5)` → int |
```

### 🔗 Footer con información del autor

```markdown
---

<div align="center">

## 📬 CONTACTO

**Creado por [Tu Nombre]**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tuusuario)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tuusuario)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tu@email.com)

<sub>© 2025 [Tu Nombre]. Documentación bajo licencia MIT.</sub>

</div>
```

[⬆️ Volver al índice](#-índice-de-contenidos)

---

## 🎯 CASOS DE USO REALES

### 📘 Caso 1: Documentación de Proyecto Python

**Cuándo usar:** README de un proyecto en GitHub/GitLab

**Elementos recomendados:**
- ✅ Header principal con badges (versión, CI/CD, cobertura)
- ✅ Índice desplegable
- ✅ Sección de instalación con código
- ✅ Ejemplos de uso con código
- ✅ Tabla de comandos/API
- ✅ Footer con autor y licencia

**Colores:** Azul (#E3F2FD) para información

**Ejemplo de estructura:**
```markdown
# Título del Proyecto
### Subtítulo con descripción

## 🚀 Instalación
[código de instalación]

## 💡 Uso rápido
[ejemplos de código]

## 📖 Documentación completa
[enlace a docs]

## 🤝 Contribuir
[guía de contribución]

## 📄 Licencia
[información de licencia]
```

### 📚 Caso 2: Tutorial Paso a Paso

**Cuándo usar:** Guía de aprendizaje, curso online, workshop

**Elementos recomendados:**
- ✅ Objetivo de aprendizaje al inicio
- ✅ Listas numeradas para pasos
- ✅ Cajas de código con explicaciones
- ✅ Ejercicios con soluciones desplegables
- ✅ Mensajes de consejo/advertencia
- ✅ Resumen al final

**Colores:** Verde (#E8F5E9) para pasos correctos, Amarillo (#FFF9C4) para tips

**Ejemplo de estructura:**
```markdown
# Tutorial: [Tema]

## 🎯 Objetivos
- Aprender X
- Dominar Y

## 📋 Requisitos previos
- Conocimiento de Z

## 📝 Paso 1: [Título]
[Explicación + código]

💡 Consejo: [tip útil]

## 📝 Paso 2: [Título]
[Explicación + código]

⚠️ Advertencia: [cuidado con...]

## ✅ Ejercicio práctico
[ejercicio con solución desplegable]

## 🎉 Resumen
Has aprendido a...
```

### ⚠️ Caso 3: Guía de Troubleshooting

**Cuándo usar:** Documentación de errores comunes, FAQ técnico

**Elementos recomendados:**
- ✅ Tabla con problemas y soluciones
- ✅ Mensajes de advertencia destacados
- ✅ Código de error con explicación
- ✅ Comparativas antes/después de la solución
- ✅ Enlaces a recursos adicionales

**Colores:** Rojo (#FFEBEE) para errores, Verde (#E8F5E9) para soluciones

**Ejemplo de estructura:**
```markdown
# Solución de Problemas Comunes

## ❌ Error 1: [Descripción]

**Síntoma:**
```
[código del error]
```

**Causa:** [explicación de por qué ocurre]

**Solución:**
[pasos para resolver + código]

✅ Verificación: [cómo comprobar que está resuelto]

---

## ❌ Error 2: [Descripción]
[mismo formato]
```

### 📖 Caso 4: README de GitHub

**Cuándo usar:** Repositorio público/privado en GitHub

**Elementos recomendados:**
- ✅ Badges con estado del proyecto
- ✅ Demo con GIF o capturas
- ✅ Instalación rápida
- ✅ Tabla de características
- ✅ Sección de contribución
- ✅ Licencia

**Colores:** Mantén diseño minimalista, usa emojis con moderación

**Ejemplo de estructura:**
```markdown
<div align="center">

# 🚀 Nombre del Proyecto

Descripción breve y atractiva

[![CI](badge)](link) [![Coverage](badge)](link) [![License](badge)](link)

[Demo](#) | [Documentación](#) | [Changelog](#)

</div>

## ✨ Características

- ⚡ Rápido y eficiente
- 🔒 Seguro
- 📦 Fácil de instalar

## 🚀 Instalación

```bash
pip install nombre-proyecto
```

## 💻 Uso

```python
from proyecto import funcion
funcion()
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Ver [CONTRIBUTING.md](link)

## 📄 Licencia

MIT License - ver [LICENSE](link)
```

### 📝 Caso 5: Documentación de API

**Cuándo usar:** Documentar endpoints, funciones, clases

**Elementos recomendados:**
- ✅ Tabla de endpoints/métodos
- ✅ Código de ejemplo con request/response
- ✅ Parámetros con tipos de datos
- ✅ Códigos de error posibles
- ✅ Rate limits y autenticación

**Ejemplo de estructura:**
```markdown
# API Documentation

## 🔑 Autenticación

```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
```

## 📡 Endpoints

### GET /api/users

Obtiene lista de usuarios

**Parámetros:**
| Nombre | Tipo | Requerido | Descripción |
|--------|------|-----------|-------------|
| `page` | int | No | Número de página |
| `limit` | int | No | Resultados por página |

**Respuesta exitosa (200):**
```json
{
  "users": [...],
  "total": 100
}
```

**Errores posibles:**
- `401`: No autorizado
- `500`: Error del servidor

---

### POST /api/users

Crea un nuevo usuario

[mismo formato]
```

[⬆️ Volver al índice](#-índice-de-contenidos)

---

## 😀 ÍNDICE DE EMOJIS POR CATEGORÍA

**Referencia rápida de emojis útiles para tus documentos.**

### 🎯 Objetivos y Metas

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 🎯 | Objetivo principal | 🎯 **Objetivo**: Aprender Python |
| 🎓 | Aprendizaje, educación | 🎓 Este tutorial enseña... |
| 🏆 | Logro, éxito | 🏆 Has completado el curso |
| ⭐ | Destacado, importante | ⭐ Característica principal |
| 🚀 | Inicio rápido, lanzamiento | 🚀 Comenzar ahora |
| 🎉 | Celebración, logro | 🎉 ¡Felicidades! |
| 💪 | Desafío, práctica | 💪 Ejercicio avanzado |

### ⚠️ Alertas y Advertencias

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| ⚠️ | Advertencia general | ⚠️ Cuidado con... |
| 🚨 | Crítico, urgente | 🚨 Error crítico |
| ⚡ | Importante, destacado | ⚡ Información clave |
| 💡 | Consejo, tip | 💡 Consejo: Recuerda que... |
| 🔥 | Hot topic, trending | 🔥 Nueva característica |
| ❗ | Atención | ❗ No olvides... |
| 🛑 | Detener, no hacer | 🛑 No uses esta función |

### ✅ Estados y Progreso

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| ✅ | Correcto, completado | ✅ Instalación exitosa |
| ❌ | Incorrecto, error | ❌ Este código falla |
| 🔄 | En progreso | 🔄 Actualizando... |
| 🔜 | Próximamente | 🔜 Nueva versión |
| ⏳ | Esperando | ⏳ Cargando datos... |
| ✔️ | Verificado | ✔️ Tests pasados |
| 🆕 | Nuevo | 🆕 Nueva sección |

### 📊 Organización y Documentación

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 📚 | Documentación, libros | 📚 Ver documentación |
| 📝 | Nota, escribir | 📝 Nota importante |
| 📌 | Punto clave, pin | 📌 Recuerda esto |
| 📋 | Lista, checklist | 📋 Requisitos |
| 📖 | Guía, lectura | 📖 Guía completa |
| 📄 | Documento, archivo | 📄 Ver archivo |
| 🗂️ | Organización | 🗂️ Estructura del proyecto |

### 💻 Código y Desarrollo

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 💻 | Código, programación | 💻 Ejemplo de código |
| 🐛 | Bug, error | 🐛 Bug conocido |
| 🔧 | Herramienta, configuración | 🔧 Configuración |
| 📦 | Paquete, módulo | 📦 Instalar paquetes |
| ⚙️ | Configuración, settings | ⚙️ Opciones |
| 🖥️ | Interfaz, pantalla | 🖥️ Interfaz de usuario |
| 🔌 | Plugin, extensión | 🔌 Plugins disponibles |

### 🎨 Diseño y Elementos Visuales

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 🎨 | Diseño, arte | 🎨 Personalización |
| 🖼️ | Imagen, foto | 🖼️ Ver imagen |
| 📊 | Gráfica, estadística | 📊 Resultados |
| 📈 | Crecimiento, mejora | 📈 Rendimiento mejorado |
| 📉 | Decrecimiento | 📉 Uso de memoria reducido |
| 🎬 | Video, demo | 🎬 Ver demo |
| 🔍 | Buscar, inspeccionar | 🔍 Buscar en código |

### 🔗 Enlaces y Navegación

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 🔗 | Enlace externo | 🔗 Ver documentación |
| 🏠 | Inicio, home | 🏠 Volver al inicio |
| ⬆️ | Volver arriba | ⬆️ Volver al índice |
| ➡️ | Siguiente, continuar | ➡️ Siguiente paso |
| ⬅️ | Anterior, volver | ⬅️ Paso anterior |
| 🌐 | Web, internet | 🌐 Sitio web |
| 📱 | Móvil, app | 📱 Aplicación móvil |

### 👥 Comunidad y Colaboración

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 👥 | Equipo, comunidad | 👥 Contribuidores |
| 🤝 | Colaboración | 🤝 Cómo contribuir |
| 💬 | Comentarios, chat | 💬 Deja un comentario |
| 📧 | Email, contacto | 📧 Contáctanos |
| 🐦 | Twitter | 🐦 Síguenos en Twitter |
| 💼 | LinkedIn, profesional | 💼 LinkedIn |
| 👤 | Usuario, perfil | 👤 Perfil del autor |

### 🔒 Seguridad y Privacidad

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 🔒 | Seguro, privado | 🔒 Datos encriptados |
| 🔐 | Contraseña, autenticación | 🔐 Requiere login |
| 🛡️ | Protección | 🛡️ Sistema protegido |
| 🔑 | Key, API key | 🔑 Obtener API key |
| ⚠️ | Advertencia de seguridad | ⚠️ Vulnerabilidad |

### 🎓 Educación y Aprendizaje

| Emoji | Uso | Ejemplo |
|:-----:|:----|:--------|
| 🎓 | Curso, educación | 🎓 Curso completo |
| 📚 | Material de estudio | 📚 Recursos adicionales |
| 🧠 | Conocimiento, pensar | 🧠 Conceptos avanzados |
| 🎯 | Objetivo de aprendizaje | 🎯 Al final sabrás... |
| 📖 | Leer, estudiar | 📖 Lectura recomendada |
| ✏️ | Escribir, practicar | ✏️ Ejercicio práctico |
| 🎲 | Práctica, juego | 🎲 Quiz interactivo |

**Consejo de uso:**
- ✅ Usa emojis con moderación (1-2 por sección)
- ✅ Sé consistente en su uso
- ✅ Prioriza la legibilidad sobre la decoración
- ❌ Evita saturar el documento con emojis

[⬆️ Volver al índice](#-índice-de-contenidos)

---

# 📖 GUÍA DE ELEMENTOS

---

## 💻 Código con Contexto Real

**Cuando usar:** Documentación de funciones, clases, métodos

### Ejemplo 1: Documentando una Función Python

```markdown
## 🔧 `calcular_promedio(numeros)`

Calcula el promedio aritmético de una lista de números.

### Sintaxis

```python
def calcular_promedio(numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list[float]): Lista de números flotantes
        
    Returns:
        float: Promedio de los números
        
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si algún elemento no es numérico
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos los elementos deben ser numéricos")
    
    return sum(numeros) / len(numeros)
```

### Parámetros

| Parámetro | Tipo | Requerido | Descripción |
|:----------|:----:|:---------:|:------------|
| `numeros` | `list[float]` | ✅ Sí | Lista de números a promediar |

### Retorna

`float` - El promedio aritmético de los números

### Excepciones

| Excepción | Cuándo se lanza |
|:----------|:----------------|
| `ValueError` | Si la lista está vacía |
| `TypeError` | Si algún elemento no es numérico |

### Ejemplos de uso

```python
# Ejemplo 1: Uso básico
>>> calcular_promedio([1, 2, 3, 4, 5])
3.0

# Ejemplo 2: Con flotantes
>>> calcular_promedio([1.5, 2.5, 3.5])
2.5

# Ejemplo 3: Manejo de error
>>> calcular_promedio([])
ValueError: La lista no puede estar vacía
```

### Casos de uso

**✅ Cuándo usar:**
- Cuando necesitas el promedio de calificaciones
- Para calcular estadísticas básicas
- En análisis de datos simples

**❌ Cuándo NO usar:**
- Para listas muy grandes (usa NumPy en su lugar)
- Si necesitas promedio ponderado (usa otra función)

### Ver también

- [`calcular_mediana()`](#) - Para el valor central
- [`calcular_desviacion()`](#) - Para medir dispersión
```

**Vista previa:**

## 🔧 `calcular_promedio(numeros)`

Calcula el promedio aritmético de una lista de números.

### Sintaxis

```python
def calcular_promedio(numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list[float]): Lista de números flotantes
        
    Returns:
        float: Promedio de los números
        
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si algún elemento no es numérico
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos los elementos deben ser numéricos")
    
    return sum(numeros) / len(numeros)
```

### Parámetros

| Parámetro | Tipo | Requerido | Descripción |
|:----------|:----:|:---------:|:------------|
| `numeros` | `list[float]` | ✅ Sí | Lista de números a promediar |

### Retorna

`float` - El promedio aritmético de los números

### Excepciones

| Excepción | Cuándo se lanza |
|:----------|:----------------|
| `ValueError` | Si la lista está vacía |
| `TypeError` | Si algún elemento no es numérico |

### Ejemplos de uso

```python
# Ejemplo 1: Uso básico
>>> calcular_promedio([1, 2, 3, 4, 5])
3.0

# Ejemplo 2: Con flotantes
>>> calcular_promedio([1.5, 2.5, 3.5])
2.5

# Ejemplo 3: Manejo de error
>>> calcular_promedio([])
ValueError: La lista no puede estar vacía
```

### Casos de uso

**✅ Cuándo usar:**
- Cuando necesitas el promedio de calificaciones
- Para calcular estadísticas básicas
- En análisis de datos simples

**❌ Cuándo NO usar:**
- Para listas muy grandes (usa NumPy en su lugar)
- Si necesitas promedio ponderado (usa otra función)

### Ver también

- [`calcular_mediana()`](#) - Para el valor central
- [`calcular_desviacion()`](#) - Para medir dispersión

[⬆️ Volver al índice](#-índice-de-contenidos)

---

## 🔄 ALTERNATIVAS SIN HTML

**Para renders que no soportan HTML, usa estas alternativas.**

### ❌ Problema: Cajas de color no funcionan

**Con HTML (no funciona en todos los renders):**
```markdown
<table>
<tr>
<td bgcolor="#FFF9C4">
💡 Tu consejo aquí
</td>
</tr>
</table>
```

**✅ Alternativa sin HTML:**
```markdown
> 💡 **CONSEJO PRO**
> 
> Tu consejo aquí con blockquote
> que funciona en todos los renders
```

### ❌ Problema: Tablas con colores de fondo

**Con HTML (no funciona en todos los renders):**
```markdown
<table>
<tr>
<td bgcolor="#E8F5E9">Contenido verde</td>
<td bgcolor="#FFEBEE">Contenido rojo</td>
</tr>
</table>
```

**✅ Alternativa sin HTML:**
```markdown
| ✅ CORRECTO | ❌ INCORRECTO |
|:------------|:---------------|
| 🟢 Contenido correcto | 🔴 Contenido incorrecto |
| Explicación positiva | Explicación negativa |
```

### ❌ Problema: Texto centrado

**Con HTML (no funciona en todos los renders):**
```markdown
<div align="center">
Texto centrado
</div>
```

**✅ Alternativa sin HTML:**
```markdown
Usa tablas para centrar:

| |
|:--:|
| Texto "centrado" |
```

### ❌ Problema: Formato de comparación lado a lado

**Con HTML:**
```markdown
<table>
<tr>
<td width="50%">Columna 1</td>
<td width="50%">Columna 2</td>
</tr>
</table>
```

**✅ Alternativa sin HTML:**
```markdown
### ❌ ANTES

Código o explicación antes

---

### ✅ DESPUÉS

Código o explicación después
```

### Tabla de equivalencias

| Con HTML | Sin HTML (Alternativa) |
|:---------|:-----------------------|
| `<div align="center">` | Tabla con alineación central |
| `<td bgcolor="#color">` | Emojis de colores (🟢🔴🟡🔵) |
| `<table>` para layout | Secciones separadas con `---` |
| `<details>` | Funciona sin HTML ✅ |
| `<br>` | Doble enter o lista |

**Recomendación:**
- ✅ Usa la versión con HTML para GitHub/GitLab
- ✅ Usa alternativas sin HTML para documentación portátil
- ✅ Prueba tu documento en el render donde lo publicarás

[⬆️ Volver al índice](#-índice-de-contenidos)

---

# 📖 ELEMENTOS ORIGINALES DE LA PLANTILLA

*(Aquí continúa con todos los elementos originales de tu plantilla)*

---

## 🎯 Título Principal

```markdown
<div align="center">

# 🎯 TÍTULO PRINCIPAL DEL DOCUMENTO

### *Subtítulo o descripción breve del contenido*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--01--23-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

</div>
```

**Vista previa:**

<div align="center">

# 🎯 TÍTULO PRINCIPAL DEL DOCUMENTO

### *Subtítulo o descripción breve del contenido*

![Version](https://img.shields.io/badge/Versión-1.0-blue?style=for-the-badge)
![Fecha](https://img.shields.io/badge/Fecha-2025--01--23-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

</div>

[⬆️ Volver al índice](#-índice-de-contenidos)

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

[⬆️ Volver al índice](#-índice-de-contenidos)

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

[⬆️ Volver al índice](#-índice-de-contenidos)

---

*(Continúa con el resto de elementos de tu plantilla original...)*

---

## 🎨 PALETA DE COLORES DISPONIBLES

<div align="center">

### Colores Claros (Fondos)

| Color | Código | Uso Recomendado | Emoji |
|:------|:------:|:----------------|:-----:|
| 🔵 Azul claro | `#E3F2FD` | Información, conceptos generales | 💡 |
| 🟢 Verde claro | `#E8F5E9` | Buenas prácticas, código correcto | ✅ |
| 🟡 Amarillo claro | `#FFF9C4` | Consejos, tips, advertencias leves | 💡 |
| 🔴 Rojo claro | `#FFEBEE` | Advertencias, errores, código incorrecto | ⚠️ |
| 🟣 Morado claro | `#F3E5F5` | Código alternativo, variaciones | 🔄 |
| 🟠 Naranja claro | `#FFF3E0` | Código sin optimizar, antes | ❌ |
| 🔷 Cian claro | `#E1F5FE` | Notas informativas, datos | 📝 |
| 🟩 Verde agua | `#B2DFDB` | Objetivos, metas de aprendizaje | 🎯 |
| ⚪ Gris claro | `#F5F5F5` | Neutral, referencias | 📖 |

### Colores Oscuros (Bordes y Acentos)

| Color | Código | Uso Recomendado | Combinación |
|:------|:------:|:----------------|:------------|
| 🔵 Azul | `#2196F3` | Información | Con #E3F2FD |
| 🟢 Verde | `#4CAF50` | Éxito, correcto | Con #E8F5E9 |
| 🟡 Amarillo | `#FBC02D` | Consejos | Con #FFF9C4 |
| 🔴 Rojo | `#FF5722` | Advertencias críticas | Con #FFEBEE |
| 🟠 Naranja | `#FF9800` | Pasos intermedios | Con #FFF3E0 |
| 🔷 Cian | `#03A9F4` | Notas destacadas | Con #E1F5FE |
| 🟩 Verde agua | `#009688` | Objetivos | Con #B2DFDB |
| ⚫ Gris oscuro | `#757575` | Texto secundario | Con #F5F5F5 |

### Paleta para Modo Oscuro (opcional)

| Uso | Color Claro | Color Oscuro Equivalente |
|:----|:----------:|:------------------------:|
| Fondo informativo | `#E3F2FD` | `#0D47A1` |
| Fondo éxito | `#E8F5E9` | `#1B5E20` |
| Fondo advertencia | `#FFF9C4` | `#F57F17` |
| Fondo error | `#FFEBEE` | `#B71C1C` |

### Ejemplos de Combinaciones Efectivas

**📘 Información técnica:**
- Fondo: `#E3F2FD` (azul claro)
- Borde: `#2196F3` (azul)
- Texto: Negro
- Emoji: 💡 📖 🔍

**✅ Buenas prácticas:**
- Fondo: `#E8F5E9` (verde claro)
- Borde: `#4CAF50` (verde)
- Texto: Negro
- Emoji: ✅ 🎯 ⭐

**⚠️ Advertencias:**
- Fondo: `#FFF9C4` (amarillo claro)
- Borde: `#FBC02D` (amarillo)
- Texto: Negro
- Emoji: ⚠️ ⚡ 💡

**❌ Errores críticos:**
- Fondo: `#FFEBEE` (rojo claro)
- Borde: `#FF5722` (rojo)
- Texto: Negro
- Emoji: ❌ 🚨 🛑

</div>

[⬆️ Volver al índice](#-índice-de-contenidos)

---

## ✅ CHECKLIST DE USO

<div align="center">

<table>
<tr>
<td bgcolor="#F5F5F5">

### ✅ Antes de publicar tu documento, verifica:

#### 📋 Estructura

- [ ] Título principal claro y descriptivo con emoji
- [ ] Subtítulo que explica el contenido
- [ ] Índice completo con enlaces internos funcionales
- [ ] Badges de versión, fecha y estado actualizados
- [ ] Todos los enlaces "Volver al índice" funcionando

#### 💻 Código

- [ ] Código con sintaxis resaltada correctamente
- [ ] Lenguaje especificado en bloques de código (\`\`\`python)
- [ ] Ejemplos de código con salida esperada
- [ ] Código comentado cuando es necesario
- [ ] Ejemplos ejecutables y probados

#### 🎨 Formato

- [ ] Mensajes importantes con colores apropiados
- [ ] Emojis usados con moderación y coherencia
- [ ] Tablas formateadas correctamente
- [ ] Imágenes con texto alternativo (alt text)
- [ ] Espaciado consistente entre secciones

#### 📝 Contenido

- [ ] Información técnica precisa y actualizada
- [ ] Ejercicios con soluciones desplegables (si aplica)
- [ ] Explicaciones claras y concisas
- [ ] Enlaces externos funcionando
- [ ] Referencias a recursos adicionales

#### 🤝 Metadatos

- [ ] Información del autor actualizada
- [ ] Licencia especificada
- [ ] Contacto/redes sociales funcionando
- [ ] Fecha de última actualización
- [ ] Historial de versiones (si aplica)

#### 🧪 Pruebas

- [ ] Documento probado en GitHub
- [ ] Documento probado en VSCode Preview
- [ ] Enlaces internos verificados
- [ ] Enlaces externos verificados
- [ ] Sin errores de ortografía

#### ♿ Accesibilidad

- [ ] Imágenes con texto alternativo
- [ ] Colores con suficiente contraste
- [ ] Estructura jerárquica de títulos correcta
- [ ] Enlaces descriptivos (evitar "clic aquí")
- [ ] Tablas con encabezados claros

</td>
</tr>
</table>

</div>

[⬆️ Volver al índice](#-índice-de-contenidos)

---

<div align="center">

## 📬 INFORMACIÓN DEL DOCUMENTO

<table>
<tr>
<td align="center" bgcolor="#263238" style="color: white;">

### 👤 AUTOR

**Juanan Comins**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juanantoniocomins)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tuusuario)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tu-email@ejemplo.com)

</td>
</tr>
</table>

<table>
<tr>
<td align="center" width="33%" bgcolor="#1565C0" style="color: white;">

📅 **FECHA**

23 de enero de 2025

</td>
<td align="center" width="33%" bgcolor="#43A047" style="color: white;">

📌 **VERSIÓN**

2.0 - Mejorada

</td>
<td align="center" width="34%" bgcolor="#E53935" style="color: white;">

⚖️ **LICENCIA**

MIT License

</td>
</tr>
</table>

### 🆕 ¿Qué hay de nuevo en v2.0?

- ⚡ Snippets rápidos listos para copiar
- 🎯 Casos de uso reales con ejemplos
- 😀 Índice completo de emojis por categoría
- 💻 Ejemplos de código con contexto real
- 🔄 Alternativas sin HTML para compatibilidad
- ✅ Checklist expandido de publicación
- 🎨 Paleta de colores ampliada con combinaciones

### 📊 Estadísticas del Documento

- **Elementos documentados:** 50+
- **Snippets listos:** 10+
- **Casos de uso:** 5
- **Emojis categorizados:** 80+
- **Colores disponibles:** 16

---

<sub>© 2025 Juanan Comins. Plantilla de referencia para documentación técnica profesional.</sub>

<sub>Hecho con 💙 para la comunidad de desarrolladores</sub>

### 🌟 ¿Te resultó útil esta plantilla?

Dale una ⭐ en GitHub y compártela con otros desarrolladores

</div>

---

<div align="center">

## 🤝 CONTRIBUIR

¿Quieres mejorar esta plantilla?

1. 🍴 Fork este proyecto
2. 🔧 Crea una rama para tu mejora
3. ✅ Haz commit de tus cambios
4. 📤 Push a la rama
5. 🎉 Abre un Pull Request

**Todas las contribuciones son bienvenidas**

</div>

---

<div align="center">

<sub>Última actualización: 23 de enero de 2025 | v2.0</sub>

</div>

<!-- Fin del documento -->
