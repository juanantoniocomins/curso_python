# Es el proceso de cambiar el tipo de dato de una variable (ej., de texto a número)
# para que pueda usarse en una operación específica (ej., una suma matemática).

## 1. Conversión de CADENA (str) a NÚMEROS (int y float)
# Esto es vital para procesar la entrada del usuario (la función input() siempre devuelve texto).

entrada_usuario_edad = "25"
entrada_usuario_altura = "1.75"

# Conversión a Entero (int) para operaciones de conteo o edad:
edad_entero = int(entrada_usuario_edad)
print(f"1. Edad como entero: {edad_entero}, Tipo: {type(edad_entero)}")

# Conversión a Flotante (float) para números decimales:
altura_float = float(entrada_usuario_altura)
print(f"2. Altura como float: {altura_float}, Tipo: {type(altura_float)}")

# Demostración: Sumar con el tipo correcto
print(f"3. Suma de edades (25 + 10): {edad_entero + 10}") 
print("-" * 30)


## 2. Conversión de NÚMEROS a CADENA (str)
# Necesario para concatenar números con cadenas de texto o para escribir datos en archivos.

valor_int = 150
valor_float = 9.99

# Conversión a Cadena (str)
cadena_int = str(valor_int)
cadena_float = str(valor_float)

print(f"4. Valor int como str: '{cadena_int}', Tipo: {type(cadena_int)}")

# Demostración: Concatenación (unir texto)
print(f"5. Concatenación: 'El precio es $' + {cadena_float}")
print("-" * 30)


## 3. Conversión a Booleano (bool)
# Cualquier valor se puede convertir a True o False. Solo algunos valores específicos son False.

# Los valores que son considerados False (Falsy):
falso_cero = bool(0)
falso_vacio_str = bool("")
falso_vacio_lista = bool([])
falso_none = bool(None)

print(f"6. 0 es False: {falso_cero}")
print(f"7. La cadena vacía ('') es False: {falso_vacio_str}")

# El resto de valores (cualquier número diferente de 0, cualquier cadena con contenido) son True (Truthy):
verdadero_num = bool(100)
verdadero_str = bool("Hola")

print(f"8. Cualquier número diferente de 0 es True: {verdadero_num}")
print("-" * 30)


## ⚠️ Manejo de Errores al Convertir
# Python lanza un error si intentas convertir una cadena que NO tiene formato numérico.

cadena_mala = "Hola123"

try:
    int(cadena_mala)
except ValueError as e:
    print(f"9. ¡ERROR al intentar convertir 'Hola123' a int! Mensaje: {e}")