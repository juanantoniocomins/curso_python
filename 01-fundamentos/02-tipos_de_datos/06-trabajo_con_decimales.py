# ---------------------------------- Declaración básica

altura = 1.75
pi = 3.14159

# ---------------------------------- Suma, Resta, Multiplicación, División, Potencía

a = 10.5
b = 2.0

suma = a + b        # 12.5
resta = a - b       # 8.5
producto = a * b    # 21.0
cociente = a / b    # 5.25
potencia = a ** 2   # 110.25


# ---------------------------------- Conversion de tipos

entero = 5
cadena = "2.5"

f1 = float(entero) # 5.0
f2 = float(cadena) # 2.5

# ---------------------------------- Redondeo con round(): permite redondear un número al número de decimales que especifiques.

num_largo = 3.14159265

redondeo_a_2 = round(num_largo, 2)  # Redondear a 2 decimales
print(redondeo_a_2)                 # 3.14


# ---------------------------------- Formateo en la Impresión (F-strings): Se usa la sintaxis {variable:.Nf}, donde N es el número de decimales:

precio = 19.99876
impuesto = 0.21

total = precio * (1 + impuesto)     # 24.19840996

# Imprimir con 2 decimales
print(f"Total: ${total:.2f}")       # Total: $24.20 (¡fíjate que redondea!)

