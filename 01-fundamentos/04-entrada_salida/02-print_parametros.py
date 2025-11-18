import sys
import time

print("--- 1. Argumento *objects (Valores a imprimir) ---")

# El argumento principal: acepta múltiples valores de diferentes tipos separados por comas.
nombre = "Ana"
edad = 28
pi = 3.14159

print("Valores múltiples:", nombre, edad, pi, True) 
print("-" * 40)


print("--- 2. Argumento sep (Separador) ---")

# Por defecto, el separador es un espacio (' ').
# Lo cambiamos a un guión bajo ('_').
print("A", "B", "C", "D", sep='_') 

# Lo cambiamos a un salto de línea ('\n').
print("Línea", "Línea", "Línea", sep='\n')
print("-" * 40)


print("--- 3. Argumento end (Final de línea) ---")

# Por defecto, el final es un salto de línea ('\n').
# Lo cambiamos para que la siguiente impresión continúe en la misma línea.
print("Esto se queda en la misma línea", end=' -> ')
print("Continuación en la misma línea.")

# Sin end, se imprime normalmente (con salto de línea).
print("Línea final.")
print("-" * 40)


print("--- 4. Argumento file (Salida a Archivo) ---")

# En lugar de imprimir en la consola (sys.stdout), enviamos la salida a un archivo.
nombre_archivo = "salida_registro.txt"

# Usamos 'with open' para abrir el archivo en modo escritura ('w')
with open(nombre_archivo, 'w', encoding='utf-8') as archivo_salida:
    print("Este mensaje NO aparecerá en la consola.", file=archivo_salida)
    print("Se ha escrito el registro completo en:", nombre_archivo)
    
print("Revisa el archivo 'salida_registro.txt' que se acaba de crear.")
print("-" * 40)


print("--- 5. Argumento flush (Vaciar Buffer) ---")

# 'flush=True' obliga a la salida a escribirse inmediatamente, sin esperar al sistema.
# Esto es útil en bucles o cuando se imprime con delays.
print("Imprimiendo con flush=True...", end='', flush=True)

# Simulamos una tarea pesada o un delay (que es cuando el buffer podría fallar)
time.sleep(0.5) 

print(" ¡Hecho inmediatamente!")