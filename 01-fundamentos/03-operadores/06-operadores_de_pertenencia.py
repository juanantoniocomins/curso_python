"""
📘 OPERADORES DE PERTENENCIA EN PYTHON
--------------------------------------

Los operadores de pertenencia se utilizan para verificar si un valor o una variable
se encuentra presente DENTRO de una secuencia (cadenas, listas, tuplas, conjuntos).
El resultado siempre es 'True' o 'False'.

OPERADORES DISPONIBLES:
Operador | Descripción | Ejemplo | Resultado
---------|-------------|---------|----------
   in    | Pertenece   | 'a' in secuencia | True si el valor se encuentra.
  not in | No Pertenece| 'z' not in secuencia | True si el valor NO se encuentra.
"""

# --- VARIABLES DE PRUEBA (Colecciones) ---
cadena_texto = "Python Avanzado"
lista_frutas = ["manzana", "banana", "cereza"]
tupla_numeros = (10, 20, 30)

# --- OPERACIONES DE PERTENENCIA ---

print("--- 1. Operador 'in' (Verificar Existencia) ---")

# 1A. En Cadenas de Texto
existe_p = 'P' in cadena_texto  # La P mayúscula ¿está?
existe_avanz = "Avanzado" in cadena_texto # La subcadena ¿está?

print(f"¿'P' en '{cadena_texto}'? {existe_p}")
print(f"¿'Avanzado' en '{cadena_texto}'? {existe_avanz}")

# 1B. En Listas
existe_banana = "banana" in lista_frutas
existe_uva = "uva" in lista_frutas

print(f"¿'banana' en {lista_frutas}? {existe_banana}")
print(f"¿'uva' en {lista_frutas}? {existe_uva}")
print("-" * 30)


print("--- 2. Operador 'not in' (Verificar Ausencia) ---")

# not in: Devuelve True si el valor NO está en la colección.

# 2A. En Tuplas
no_existe_5 = 5 not in tupla_numeros
no_existe_20 = 20 not in tupla_numeros

print(f"¿5 NO está en {tupla_numeros}? {no_existe_5}")
print(f"¿20 NO está en {tupla_numeros}? {no_existe_20}")

# 2B. En Cadenas
no_existe_z = 'z' not in cadena_texto

print(f"¿'z' NO está en '{cadena_texto}'? {no_existe_z}")
print("-" * 30)