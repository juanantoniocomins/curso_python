"""
Cómo manejar números (int y float) en print(), cubriendo los tres métodos principales:

1. 🔢 Impresión Directa y con Comas (Método Pythonic Básico)
        Cuando pasas números (o cualquier tipo de dato no str) a print() separados por comas, Python realiza automáticamente la conversión necesaria.

        Comportamiento Clave
        Conversión Implícita: Python convierte internamente el número (o cualquier tipo, como int, float, bool) a una cadena de texto (str) antes de imprimirlo. Esto se hace de forma segura y automática.

        Separador por Defecto: Utiliza el argumento sep=' ' (un espacio) para separar los números y cualquier otra cadena de texto en la salida.

2. 🔗 Concatenación de Cadenas (+) (Método Explícito)
        Si intentas unir números directamente con cadenas de texto utilizando el operador de concatenación (+), Python te obligará a hacer el Casting Explícito.

        Comportamiento Clave
        Error de Tipo: El operador + solo permite unir objetos del mismo tipo de dato (solo cadenas con cadenas, o números con números).

        Necesidad de str(): Para unir una cadena y un número, debes convertir manualmente el número a cadena usando la función str().
        Nota: Este método es menos flexible que las f-strings y requiere más código (str()), por lo que se usa menos.

3. 🖼️ Cadenas Formateadas (F-strings) (Método Avanzado y Moderno)

        Las f-strings son la forma más poderosa y flexible para incluir y formatear números dentro de una cadena de texto.

        Comportamiento Clave
        Conversión Implícita y Lectura: El número se inserta directamente dentro de las llaves ({}) y se convierte a str de manera limpia.

        Formato de Decimales: Permite controlar la cantidad de decimales, el relleno, separadores de miles y más.

        Formato de Decimales
        La sintaxis clave para los números flotantes es {variable:.Nf}, donde N es el número de decimales que deseas mostrar (y redondear).

        ==========================================================================
        Sintaxis	    Uso	Ejemplo	Salida
        ==========================================================================        
        :.2f	        Limita a dos decimales.	f"{98.96:.2f}"	98.96
        :.0f	        Muestra el entero redondeado.	f"{98.96:.0f}"	99
        :,	            Agrega separadores de miles.	f"{1234567:,}"	1,234,567
"""

####################################### 1 ########################################

edad = 33
altura = 1.75
es_estudiante = True

# Python imprime los valores de las variables, separándolos con un espacio.
print("La edad es", edad, "y la altura es", altura, "Estudiante:", es_estudiante)


####################################### 2 ########################################

# Error si no se convierte: print("Tengo " + edad + " años.")
# Solución:
print("Tengo " + str(edad) + " años.")


####################################### 3 ########################################

precio = 1999.9987
iva = 0.21

# Formateo combinado
print(f"El precio base es ${precio:,.2f} y el IVA es {iva:.0%}.")