"""
input() es una función incorporada en Python que lee datos introducidos por el usuario desde la entrada estándar (teclado).
El flujo del programa se detiene hasta que el usuario ingresa datos y presiona Enter.

La función input() acepta un argumento opcional:

input(prompt='')
===================================================================================================================================================================================================================
        Parámetro	Descripción	                                                                                                                                Valor por Defecto
===================================================================================================================================================================================================================        
        prompt	    Cadena de texto que se muestra al usuario antes de leer la entrada. Es opcional pero muy recomendado para indicar qué dato se espera.	    '' (Cadena vacía - no muestra nada)

IMPORTANTE: input() SIEMPRE devuelve una cadena de texto (str), sin importar qué escriba el usuario.
Para trabajar con números u otros tipos, es necesario realizar conversión de tipos (casting).
"""

print("--- 1. Argumento prompt (Mensaje al Usuario) ---")

# Sin prompt - No se muestra ningún mensaje, solo el cursor parpadeando
print("Entrada sin prompt (escribe algo y presiona Enter):")
dato_sin_prompt = input()
print(f"Recibido: '{dato_sin_prompt}'")
print("-" * 40)

# Con prompt - Muestra un mensaje descriptivo al usuario
nombre = input("Introduce tu nombre: ")
print(f"¡Hola, {nombre}!")
print("-" * 40)


print("--- 2. Tipo de Dato Devuelto (Siempre str) ---")

# Aunque el usuario escriba un número, input() devuelve una cadena
dato = input("Escribe el número 42: ")
print(f"Tipo de dato recibido: {type(dato)}")  # <class 'str'>
print(f"Valor: '{dato}'")
print(f"¿Es una cadena? {isinstance(dato, str)}")  # True
print("-" * 40)


print("--- 3. Conversión de Tipos (Casting) ---")

# Convertir a entero (int)
edad_str = input("¿Cuántos años tienes? ")
edad_int = int(edad_str)  # Conversión explícita
print(f"El próximo año tendrás {edad_int + 1} años.")
print(f"Tipo: {type(edad_int)}")

# Conversión directa en una línea (más común)
altura = float(input("¿Cuál es tu altura en metros? "))
print(f"Tu altura es {altura} m, tipo: {type(altura)}")
print("-" * 40)


print("--- 4. Validación y Manejo de Errores ---")

# Sin validación, si el usuario escribe texto en lugar de número, el programa crashea
print("Validación con try-except:")
try:
    numero = int(input("Introduce un número entero: "))
    print(f"Has introducido: {numero}")
except ValueError:
    print("❌ Error: No has introducido un número válido.")

# Validación con bucle (repite hasta obtener dato válido)
print("\nValidación con bucle (no aceptará texto):")
while True:
    try:
        numero_valido = int(input("Introduce un número entero válido: "))
        print(f"✅ Número válido recibido: {numero_valido}")
        break  # Sale del bucle si la conversión fue exitosa
    except ValueError:
        print("❌ Dato inválido. Intenta de nuevo.")
print("-" * 40)


print("--- 5. Entrada Múltiple en una Línea ---")

# Leer varios datos separados por espacios
print("Introduce tres números separados por espacios (ej: 10 20 30):")
linea = input()
numeros = linea.split()  # Divide la cadena en una lista
print(f"Has introducido: {numeros}")
print(f"Tipo de cada elemento: {[type(n) for n in numeros]}")  # Todos son str

# Convertir todos a enteros
numeros_int = [int(n) for n in numeros]
print(f"Convertidos a int: {numeros_int}")
print(f"Suma total: {sum(numeros_int)}")
print("-" * 40)


print("--- 6. Entrada con Valores por Defecto ---")

# Simulando un valor por defecto si el usuario no introduce nada
ciudad = input("¿En qué ciudad vives? (presiona Enter para 'Desconocida'): ")
if ciudad == "":  # Si el usuario solo presiona Enter sin escribir nada
    ciudad = "Desconocida"
print(f"Ciudad: {ciudad}")

# Usando 'or' para valor por defecto (método más pythónico)
pais = input("¿País? (presiona Enter para 'España'): ") or "España"
print(f"País: {pais}")
print("-" * 40)


print("--- 7. Entrada Segura con strip() ---")

# Los usuarios pueden introducir espacios adicionales accidentalmente
# strip() elimina espacios en blanco al inicio y final
nombre_con_espacios = input("Introduce tu nombre (puedes añadir espacios): ")
print(f"Sin strip: '{nombre_con_espacios}'")
print(f"Con strip: '{nombre_con_espacios.strip()}'")
print("-" * 40)


print("--- 8. Entrada de Booleanos (Sí/No) ---")

# Convertir respuestas de usuario a booleanos
respuesta = input("¿Quieres continuar? (s/n): ").strip().lower()

if respuesta == 's' or respuesta == 'si' or respuesta == 'sí':
    continuar = True
elif respuesta == 'n' or respuesta == 'no':
    continuar = False
else:
    print("Respuesta no válida, se asume 'No'")
    continuar = False

print(f"Continuar: {continuar} (tipo: {type(continuar)})")
print("-" * 40)


print("--- 9. Lectura desde Archivo (Simulando input) ---")

# Aunque input() lee desde teclado (sys.stdin), puedes redirigir la entrada
# Esto es útil para testing automatizado
import sys
from io import StringIO

# Simulamos entrada de usuario sin necesidad de escribir manualmente
entrada_simulada = StringIO("Juan\n25\n")
sys.stdin = entrada_simulada

nombre_sim = input("Nombre: ")
edad_sim = int(input("Edad: "))

# Restauramos entrada estándar
sys.stdin = sys.__stdin__

print(f"Datos simulados: {nombre_sim}, {edad_sim} años")
print("(Útil para testing automatizado)")
print("-" * 40)


print("--- 10. Entrada Segura de Contraseñas (getpass) ---")

# Para datos sensibles, usa el módulo getpass (no muestra lo que se escribe)
import getpass

# Nota: getpass no funciona bien en algunos entornos (como Jupyter o algunos IDEs)
# pero funciona perfecto en terminal/consola normal
try:
    password = getpass.getpass("Introduce tu contraseña (no se verá): ")
    print(f"Contraseña recibida (longitud: {len(password)} caracteres)")
    print("✅ Contraseña oculta exitosamente")
except Exception:
    print("⚠️ getpass no disponible en este entorno, usa input() normal en su lugar")
