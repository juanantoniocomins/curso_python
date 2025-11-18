# print() – Imprimir en consola
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# *objects: uno o varios valores a imprimir.
# sep=' ' → separador entre los valores (por defecto un espacio).
# end='\n' → qué poner al final (por defecto un salto de línea).
# file=sys.stdout → salida (puede ser un archivo en vez de la consola).
# flush=False → fuerza la impresión inmediata si es True.

print("Hola, mundo")                    # Texto simple
print("Nombre:", "Juanan")              # Múltiples valores
print("Suma:", 3 + 5)                   # Expresión
print("Hola", "Mundo", sep="-")         # Hola-Mundo
print("Hola\nMundo")                    # Salto de línea
print("A\tB\tC")                        # Tabulación
print("Texto", end=" ")                 # Sin salto final

"""
print() es una función incorporada en Python que muestra información por pantalla. 
En Python 3 siempre debe usarse con paréntesis, por ejemplo print("Hola"). 
Al ejecutarla, los valores pasados se convierten a texto legible y se envían a la salida estándar (la pantalla)

La función print() acepta varios argumentos separados por comas.

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
        ===================================================================================================================================================================================================================
        Parámetro	Descripción	                                                                                                                                Valor por Defecto
===================================================================================================================================================================================================================        
        *objects	Los valores (variables, expresiones, cadenas, etc.) a imprimir. Es el único argumento que se debe proporcionar al menos con un valor.	        — (No tiene; es la información obligatoria)
        sep	        La cadena de texto que se insertará entre los objetos si se proporcionan múltiples argumentos (separados por comas).	                        ' ' (Un espacio en blanco)
        end	        La cadena de texto que se agregará al final de la salida. Controla qué ocurre después de que se ha impreso todo el contenido.	                '\n' (Un salto de línea)
        file	    El objeto de archivo o stream (flujo de datos) donde se enviará la salida.	                                                                        sys.stdout (La consola o terminal)
        flush	    Un valor booleano que indica si la salida del stream (como la consola) debe vaciarse forzadamente (escribirse inmediatamente).	                False (El sistema operativo optimiza cuándo escribir la salida)

"""

print("hola mundo1!!!")
print('hola mundo2!!!')

cad1 = "Hola"
cad2 = " Mundo3"
cad3 = "!!!"

print(cad1 + cad2 + cad3)

cad4 = "hola"
cad5 = "mundo4"
cad6 = "!!!"

print(cad4 , cad5 , cad6)

# se puede usuar como salto de linea
print("")
