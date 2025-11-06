"""
📘 OPERADORES DE COMPARACIÓN EN PYTHON
-------------------------------------

Los operadores de comparación se utilizan para comparar dos valores.
El resultado de cualquier comparación siempre es un valor Booleano:
'True' (Verdadero) o 'False' (Falso).

OPERADORES DISPONIBLES:
    ==  Igual a: Comprueba si los valores son idénticos.
    !=  Diferente de: Comprueba si los valores NO son idénticos.
    >   Mayor que: Comprueba si el valor de la izquierda es mayor.
    <   Menor que: Comprueba si el valor de la izquierda es menor.
    >=  Mayor o igual que: Comprueba si es mayor o igual.
    <=  Menor o igual que: Comprueba si es menor o igual.
"""

# --- VARIABLES DE PRUEBA ---
valor_a = 50
valor_b = 50
valor_c = 75

# --- OPERACIONES DE COMPARACIÓN ---

# 1. Igual a (==)
es_igual_ab = valor_a == valor_b
es_igual_ac = valor_a == valor_c

# 2. Diferente de (!=)
es_diferente_ab = valor_a != valor_b
es_diferente_ac = valor_a != valor_c

# 3. Mayor que (>)
es_mayor_ac = valor_a > valor_c
es_mayor_ca = valor_c > valor_a

# 4. Menor que (<)
es_menor_ac = valor_a < valor_c
es_menor_ca = valor_c < valor_a

# 5. Mayor o igual que (>=)
es_mayor_o_igual_ab = valor_a >= valor_b
es_mayor_o_igual_ca = valor_c >= valor_a

# 6. Menor o igual que (<=)
es_menor_o_igual_ab = valor_a <= valor_b
es_menor_o_igual_ca = valor_c <= valor_a


# --- IMPRESIÓN DE RESULTADOS ---

print(f"\n--- VALORES: A={valor_a}, B={valor_b}, C={valor_c} ---")

# Igualdad y Diferencia
print(f"1. {valor_a} == {valor_b}: {es_igual_ab} (A y B son iguales)")
print(f"2. {valor_a} != {valor_b}: {es_diferente_ab} (A y B son diferentes)")

# Mayor y Menor
print(f"3. {valor_a} > {valor_c}: {es_mayor_ac} (A es mayor que C)")
print(f"4. {valor_c} > {valor_a}: {es_mayor_ca} (C es mayor que A)")

# Mayor/Menor o Igual
print(f"5. {valor_a} >= {valor_b}: {es_mayor_o_igual_ab} (A es mayor o igual que B)")
print(f"6. {valor_c} <= {valor_a}: {es_menor_o_igual_ca} (C es menor o igual que A)")