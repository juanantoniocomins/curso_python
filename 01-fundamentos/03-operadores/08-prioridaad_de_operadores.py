"""
📘 PRIORIDAD DE OPERADORES (JERARQUÍA)
--------------------------------------

La prioridad define el orden en que Python evalúa las operaciones en una expresión.
Sin paréntesis, las operaciones de mayor prioridad se resuelven antes que las de menor.

JERARQUÍA BÁSICA (De Mayor a Menor Prioridad):
1. () Paréntesis (Cambian el orden)
2. ** Exponenciación
3. *, /, //, % Multiplicativos y División
4. +, - Aditivos
5. Comparación (==, >, <, etc.)
6. not, and, or (Lógicos)

NOTA: Python evalúa las expresiones de izquierda a derecha respetando esta jerarquía,
a menos que se utilicen paréntesis para alterar el orden.
"""

# --- VARIABLES DE PRUEBA ---
a = 10
b = 5
c = 2
d = 4

print("--- 1. Demostración de Jerarquía por Defecto ---")

# Ejemplo 1: Multiplicación (*) tiene mayor prioridad que Suma (+)
# Cálculo: (b * c) + a  => (5 * 2) + 10 => 10 + 10 = 20
resultado_1 = a + b * c 
print(f"1. {a} + {b} * {c} = {resultado_1}") # Resultado: 20

# Ejemplo 2: División (/) tiene mayor prioridad que Resta (-)
# Cálculo: a - (b / c)  => 10 - (5 / 2) => 10 - 2.5 = 7.5
resultado_2 = a - b / c
print(f"2. {a} - {b} / {c} = {resultado_2}") # Resultado: 7.5

print("-" * 40)

# --- 2. Alterando la Jerarquía con Paréntesis () ---

# Usaremos los mismos ejemplos, pero forzando un orden diferente.

# Ejemplo 3: Forzamos la Suma (+) antes que la Multiplicación (*)
# Cálculo: (a + b) * c  => (10 + 5) * 2 => 15 * 2 = 30
resultado_3 = (a + b) * c
print(f"3. ({a} + {b}) * {c} = {resultado_3}") # Resultado: 30

# Ejemplo 4: Forzamos la Resta (-) antes que la División (/)
# Cálculo: (a - b) / c  => (10 - 5) / 2 => 5 / 2 = 2.5
resultado_4 = (a - b) / c
print(f"4. ({a} - {b}) / {c} = {resultado_4}") # Resultado: 2.5

print("-" * 40)

# --- 3. Jerarquía Lógica ---

es_mayor = a > b  # True
es_par = b % c == 0 # False (5 % 2 = 1)

# El operador 'and' se resuelve antes que 'or'
# Cálculo: es_mayor or (es_par and False) => True or (False) => True
resultado_5 = es_mayor or es_par and False 
print(f"5. True or False and False = {resultado_5}") # Resultado: True

# Alterando el orden con paréntesis
# Cálculo: (es_mayor or es_par) and False => (True or False) and False => True and False => False
resultado_6 = (es_mayor or es_par) and False
print(f"6. (True or False) and False = {resultado_6}") # Resultado: False

print("-" * 40)