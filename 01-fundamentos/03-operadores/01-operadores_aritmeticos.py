"""
📘 OPERADORES ARITMÉTICOS EN PYTHON
-----------------------------------

Los operadores aritméticos permiten realizar cálculos numéricos
con variables de tipo int, float o incluso bool.

OPERADORES DISPONIBLES:
    +   Suma: a + b
    -   Resta: a - b
    *   Multiplicación: a * b
    /   División (resultado float): a / b
    //  División entera (sin decimales): a // b
    %   Módulo (resto de la división): a % b
    **  Exponente o potencia: a ** b
    -x  Negación (cambia el signo del número)
    +x  Positivo (no cambia el valor)
"""

numero1 = 24
numero2 = 12

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
divi2 = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2
negacion = -numero1
positivo = +negacion

print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} x {numero2} = {multi}")
print(f"{numero1} / {numero2} = {divi}")
print(f"{numero1} // {numero2} = {divi2}")
print(f"{numero1} % {numero2} = {modulo}")
print(f"{numero1} ** {numero2} = {potencia}")
print(f"Negación de {numero1} = {negacion}")
print(f"Positivo de {negacion} = {positivo}")