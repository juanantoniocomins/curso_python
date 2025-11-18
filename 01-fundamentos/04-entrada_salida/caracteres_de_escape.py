"""
-----------------------------------------
 Guía práctica de caracteres de escape
-----------------------------------------

Los caracteres de escape se usan dentro de cadenas
para representar saltos de línea, tabulaciones,
comillas, barras, etc.
"""

print("=== Caracteres de escape en Python ===\n")

# Salto de línea
print("1. Salto de línea: \\n")
print("Hola\nMundo")
print("-" * 40)

# Tabulador
print("2. Tabulador: \\t")
print("Columna1\tColumna2")
print("-" * 40)

# Retorno de carro
print("3. Retorno de carro: \\r")
print("12345\rXX")
print("-" * 40)

# Backspace (borra un carácter atrás visualmente)
print("4. Backspace: \\b")
print("Hola\b!")
print("-" * 40)

# Comillas simples dentro de cadena con comillas simples
print("5. Comilla simple: \\'")
print('Esto es una comilla: \' dentro del texto')
print("-" * 40)

# Comillas dobles dentro de cadena con comillas dobles
print('6. Comilla doble: \\"')
print("Esto es una comilla: \" dentro del texto")
print("-" * 40)

# Barra invertida
print("7. Barra invertida: \\\\")
print("Ruta Windows: C:\\\\Users\\\\Juan")
print("-" * 40)

# Campana (en muchas consolas hace un sonido)
print("8. Campana: \\a")
print("Sonido (puede no funcionar en todas las consolas): \a")
print("-" * 40)

# Avance de página (poco usado)
print("9. Avance de página: \\f")
print("Linea1\fLinea2")
print("-" * 40)

# Nueva línea universal (similar a \n)
print("10. Nueva línea: \\v (vertical tab)")
print("Linea1\vLinea2")
print("-" * 40)

# Unicode: \uXXXX
print("11. Unicode básico: \\uXXXX")
print("\u2605 Estrella unicode")
print("-" * 40)

# Unicode extendido: \UXXXXXXXX
print("12. Unicode extendido: \\UXXXXXXXX")
print("\U0001F600 Emoji cara sonriente")
print("-" * 40)

# Octal \ooo
print("13. Código octal: \\ooo")
print("\110\145\154\154\157")  # "Hello"
print("-" * 40)

# Hexadecimal \xhh
print("14. Código hex: \\xhh")
print("\x48\x6F\x6C\x61")  # "Hola"
print("-" * 40)

print("\n=== Fin de los ejemplos ===")
