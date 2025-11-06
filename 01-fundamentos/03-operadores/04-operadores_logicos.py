"""
📘 OPERADORES LÓGICOS EN PYTHON
--------------------------------

Los operadores lógicos se usan para combinar múltiples condiciones Booleanas
(el resultado de operadores de comparación) o para invertir el valor de una.
El resultado siempre es 'True' o 'False'.

OPERADORES DISPONIBLES:
Operador | Descripción | Ejemplo | Resultado
---------|-------------|---------|----------
  and    | Y Lógico    | A and B | True si A Y B son True.
  or     | O Lógico    | A or B  | True si A O B es True.
  not    | NO Lógico   | not A   | Invierte el valor de A.
"""

# --- VARIABLES DE PRUEBA (Condiciones) ---
tiene_saldo = True
es_mayor_edad = True
tiene_credito = False

# --- OPERACIONES LÓGICAS ---

print("--- 1. Operador AND (Y Lógico) ---")

# AND: Solo es True si AMBAS condiciones son True
puedo_comprar_1 = tiene_saldo and es_mayor_edad  # True and True -> True
puedo_comprar_2 = tiene_saldo and tiene_credito  # True and False -> False

print(f"¿Saldo AND Mayor de edad? {puedo_comprar_1}")
print(f"¿Saldo AND Crédito? {puedo_comprar_2}")
print("-" * 30)


print("--- 2. Operador OR (O Lógico) ---")

# OR: Es True si AL MENOS UNA condición es True
puedo_entrar_1 = es_mayor_edad or tiene_credito  # True or False -> True
puedo_entrar_2 = tiene_credito or False          # False or False -> False

print(f"¿Mayor de edad OR Crédito? {puedo_entrar_1}")
print(f"¿Crédito OR False? {puedo_entrar_2}")
print("-" * 30)


print("--- 3. Operador NOT (NO Lógico) ---")

# NOT: Invierte el valor Booleano
no_hay_saldo = not tiene_saldo
no_tengo_credito = not tiene_credito

print(f"¿Tiene saldo? {tiene_saldo}")
print(f"¿NOT Saldo? {no_hay_saldo}")
print(f"¿NOT Crédito? {no_tengo_credito}")