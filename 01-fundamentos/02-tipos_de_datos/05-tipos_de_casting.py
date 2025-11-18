# --- PARTE 1: CASTING IMPLÍCITO (Conversión Automática) ---

# Python realiza automáticamente el casting implícito cuando opera con tipos
# que tienen una jerarquía clara (ej., int a float) para evitar pérdida de datos.

print("--- 1. Casting Implícito (Automático) ---")

# Variables iniciales: Entero (int) y Flotante (float)
entero_a = 10     # int
float_b = 5.5     # float

# Operación: Sumar un int con un float
resultado_suma = entero_a + float_b

print(f"1. Operación: {entero_a} (int) + {float_b} (float)")
print(f"   Resultado: {resultado_suma}")
print(f"   Tipo del Resultado (automático): {type(resultado_suma)}") 
# Resultado: float. Python promovió el int a float antes de sumar.

print("-" * 40)

# --- PARTE 2: CASTING EXPLÍCITO (Conversión Manual) ---

# El programador debe usar funciones de casting (int(), float(), str(), etc.)
# para forzar una conversión, a menudo para evitar errores o manipular la salida.

print("--- 2. Casting Explícito (Manual) ---")

# Ejemplo A: Flotante a Entero (Pérdida de Información)
numero_decimal = 9.99
numero_entero_forzado = int(numero_decimal) # Forzamos la conversión a int

print(f"2A. Flotante original: {numero_decimal}")
print(f"    Conversión a int (pierde decimal): {numero_entero_forzado}")
print(f"    Tipo: {type(numero_entero_forzado)}")

# Ejemplo B: Cadena a Número (Necesario para Matemáticas)
precio_str = "45.50"
cantidad_str = "2"

# Sin casting, daría un error al multiplicar.
precio_float = float(precio_str)
cantidad_int = int(cantidad_str)

total = precio_float * cantidad_int

print(f"\n2B. Total calculado con casting:")
print(f"    Precio (str -> float): {precio_float}")
print(f"    Cantidad (str -> int): {cantidad_int}")
print(f"    Total: {total}")

print("-" * 40)

# Ejemplo C: Número a Cadena (Necesario para Concatenación)
inventario = 15
mensaje = "Quedan " + str(inventario) + " unidades." # Forzamos la conversión a str

print(f"2C. Mensaje: {mensaje}")
print("   (La función str() fue usada manualmente para unir el texto y el número)")