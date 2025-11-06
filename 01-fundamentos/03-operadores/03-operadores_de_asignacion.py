"""
📘 OPERADORES DE ASIGNACIÓN EN PYTHON
-------------------------------------

Los operadores de asignación se usan para asignar un valor a una variable.
Los operadores compuestos (+=, -=, etc.) realizan una operación aritmética
y luego asignan el resultado a la misma variable de forma abreviada.

OPERADORES DISPONIBLES:
Operador | Descripción | Ejemplo | Equivale a
---------|-------------|---------|------------
    =    | Asignación  | x = 5   | —
   +=    | Suma y asigna| x += 3  | x = x + 3
   -=    | Resta y asigna| x -= 3  | x = x - 3
   *=    | Multiplica y asigna| x *= 3  | x = x * 3
   /=    | Divide y asigna| x /= 3  | x = x / 3
   //=   | División entera y asigna| x //= 3 | x = x // 3
   %=    | Módulo y asigna| x %= 3  | x = x % 3
   **=   | Exponente y asigna| x **= 3 | x = x ** 3
"""

# --- VARIABLE INICIAL ---
x = 10
print(f"Valor inicial de x: {x}")
print("-" * 30)

# 1. Suma y Asigna (+=)
x += 5 
print(f"1. x += 5 (x = x + 5): x ahora es {x}") # x ahora es 15

# 2. Resta y Asigna (-=)
x -= 2
print(f"2. x -= 2 (x = x - 2): x ahora es {x}") # x ahora es 13

# 3. Multiplica y Asigna (*=)
x *= 4
print(f"3. x *= 4 (x = x * 4): x ahora es {x}") # x ahora es 52

# 4. Divide y Asigna (/=) - El resultado siempre será float
x /= 2
print(f"4. x /= 2 (x = x / 2): x ahora es {x}") # x ahora es 26.0

# 5. División Entera y Asigna (//=)
x = 26.5 # Resetear x para el ejemplo
x //= 8
print(f"5. x //= 8 (x = x // 8): x ahora es {x}") # x ahora es 3.0

# 6. Módulo y Asigna (%=)
x = 17 # Resetear x
x %= 5
print(f"6. x %= 5 (x = x % 5): x ahora es {x}") # x ahora es 2 (el residuo de 17/5)

# 7. Exponente y Asigna (**=)
x = 2 # Resetear x
x **= 3
print(f"7. x **= 3 (x = x ** 3): x ahora es {x}") # x ahora es 8 (2*2*2)

print("-" * 30)