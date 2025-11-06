"""
📘 OPERADORES BIT A BIT (BITWISE) EN PYTHON
--------------------------------------------

Estos operadores actúan directamente sobre la representación binaria
(bits) de los números enteros. Son usados principalmente en programación
de bajo nivel y optimización.

Representación binaria de los valores de prueba:
5 en binario (8-bit): 0000 0101
3 en binario (8-bit): 0000 0011

OPERADORES DISPONIBLES:
Operador | Descripción | Función
---------|-------------|----------------------------------------------------
    &    | AND bit a bit | Devuelve 1 si AMBOS bits en la misma posición son 1.
    |    | OR bit a bit  | Devuelve 1 si AL MENOS UN bit en la posición es 1.
    ^    | XOR bit a bit | Devuelve 1 si los bits en la posición son DIFERENTES.
    ~    | NOT bit a bit | Invierte todos los bits (complemento a uno).
    <<   | Desplazamiento izquierda | Mueve bits a la izquierda (equivale a * 2^N).
    >>   | Desplazamiento derecha | Mueve bits a la derecha (equivale a // 2^N).
"""

# --- VARIABLES DE PRUEBA ---
a = 5  # Binario: 0101
b = 3  # Binario: 0011

print(f"--- Valores de Prueba: a = {a} (0101), b = {b} (0011) ---\n")

# 1. AND bit a bit (&)
#   0101
# & 0011
# ------
#   0001 (Decimal 1)
and_result = a & b
print(f"1. {a} & {b} (AND) = {and_result}")

# 2. OR bit a bit (|)
#   0101
# | 0011
# ------
#   0111 (Decimal 7)
or_result = a | b
print(f"2. {a} | {b} (OR) = {or_result}")

# 3. XOR bit a bit (^)
#   0101
# ^ 0011
# ------
#   0110 (Decimal 6)
xor_result = a ^ b
print(f"3. {a} ^ {b} (XOR) = {xor_result}")

# 4. NOT bit a bit (~)
# Lógica: ~(x) = -(x + 1)
not_result = ~a 
print(f"4. ~{a} (NOT) = {not_result}") # El resultado es -6

print("-" * 30)

# 5. Desplazamiento a la Izquierda (<<)
# 0101 << 1 (Mueve un bit a la izquierda, añade un 0 al final) = 1010 (Decimal 10)
shift_left_result = a << 1
print(f"5. {a} << 1 (Izquierda) = {shift_left_result} (Equivale a {a} * 2)")

# 6. Desplazamiento a la Derecha (>>)
# 0101 >> 1 (Mueve un bit a la derecha, quita el último bit) = 0010 (Decimal 2)
shift_right_result = a >> 1
print(f"6. {a} >> 1 (Derecha) = {shift_right_result} (Equivale a {a} // 2)")