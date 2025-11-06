"""
📘 OPERADORES DE IDENTIDAD EN PYTHON
------------------------------------

Los operadores de identidad verifican si dos variables apuntan al
mismo OBJETO exacto en la memoria, no solo si tienen el mismo valor.

Esto es diferente a '==' (Operador de Comparación), que solo mira el valor.

OPERADORES DISPONIBLES:
Operador | Descripción | Ejemplo | Resultado
---------|-------------|---------|----------
   is    | Identidad   | a is b  | True si 'a' y 'b' son el MISMO objeto.
  is not | No Identidad| a is not b| True si 'a' y 'b' NO son el mismo objeto.
"""

# --- ESCENARIO 1: Identidad y Valor COINCIDEN ---
# Python es eficiente y reutiliza objetos inmutables pequeños (como enteros)

x = 10
y = 10
z = x # Z apunta al mismo objeto que X

print("--- 1. MISMO OBJETO (Identidad y Valor) ---")
print(f"¿x == y? {x == y}")       # True (Mismo valor)
print(f"¿x is y? {x is y}")       # True (Mismo objeto en memoria por optimización)
print(f"¿x is z? {x is z}")       # True (Asignación directa)
print("-" * 40)


# --- ESCENARIO 2: Mismo VALOR, Diferente IDENTIDAD ---
# Las listas son mutables (cambiables), por lo que siempre son objetos diferentes,
# incluso si sus contenidos son iguales.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print("--- 2. Mismo VALOR, Diferente IDENTIDAD ---")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

# 1. Comparación de Valor (==)
print(f"¿lista1 == lista2? {lista1 == lista2}")  # True (Tienen el mismo contenido/valor)

# 2. Comparación de Identidad (is)
print(f"¿lista1 is lista2? {lista1 is lista2}")  # False (Son dos objetos distintos en memoria)

# 3. Operador 'is not' (Negación de identidad)
print(f"¿lista1 is not lista2? {lista1 is not lista2}") # True (Efectivamente NO son el mismo objeto)
print("-" * 40)


# --- ESCENARIO 3: Caso especial con None ---

# LA MEJOR PRÁCTICA: Siempre usa 'is None' en lugar de '== None'.
# 'is' verifica la identidad, y None siempre es un objeto único.

mi_variable = None

print("--- 3. Uso con None (Mejor Práctica) ---")
print(f"¿mi_variable == None? {mi_variable == None}")  # True (Funciona, pero no es el estándar)
print(f"¿mi_variable is None? {mi_variable is None}")  # True (Uso correcto y preferido en Python)