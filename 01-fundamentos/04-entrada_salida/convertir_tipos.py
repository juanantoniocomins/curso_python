# TIPOS MÁS COMUNES A CONVERTIR DESDE input()
# 
# Tipo	    Conversión	    Descripción	            Ejemplo entrada	    Resultado final
# 
# int	    int()	        Número entero	        42	                42 (int)
# float	    float()	        Número con decimales	3.14	            3.14 (float)
# bool	    bool()	        Lógico verdadero/falso 	True	            True (bool)
# str	    str()	        Texto 	                hola	            "hola" (str)
# list	    eval()	        Lista	                [1, 2, 3]	        [1, 2, 3] (list)
# tuple	    eval()	        Tupla	                (4, 5)	            (4, 5) (tuple)
# dict	    eval()	        Diccionario	            {"a": 1}	        {'a': 1} (dict)

print("\n=== EJEMPLOS PRÁCTICOS DE CASTING DESDE input() ===\n")

# --------------------------------------------------
# 1. int() → Enteros
# --------------------------------------------------
entrada_int = "42"
resultado_int = int(entrada_int)

print("1) int() → entero")
print(f"Entrada: {entrada_int}  (str)")
print(f"Resultado: {resultado_int}  (int)\n")


# --------------------------------------------------
# 2. float() → Decimales
# --------------------------------------------------
entrada_float = "3.14"
resultado_float = float(entrada_float)

print("2) float() → número decimal")
print(f"Entrada: {entrada_float}  (str)")
print(f"Resultado: {resultado_float}  (float)\n")


# --------------------------------------------------
# 3. bool() → Booleanos
# --------------------------------------------------
# IMPORTANTE: bool("False") → True, porque cualquier string NO vacío es True.
entrada_bool = "True"
resultado_bool = entrada_bool == "True"   # Forma correcta

print("3) bool() → booleano (método recomendado)")
print(f"Entrada: {entrada_bool}  (str)")
print(f"Resultado: {resultado_bool}  (bool)\n")


# --------------------------------------------------
# 4. str() → Texto
# --------------------------------------------------
entrada_str = 1234
resultado_str = str(entrada_str)

print("4) str() → texto")
print(f"Entrada: {entrada_str}  (int)")
print(f"Resultado: {resultado_str!r}  (str)\n")


# --------------------------------------------------
# 5. list() / tuple() / dict() → usando eval()
# --------------------------------------------------
# OJO: eval() ejecuta código. Solo usar en entornos controlados.
entrada_lista = "[1, 2, 3]"
entrada_tupla = "(4, 5)"
entrada_dict = '{"a": 1, "b": 2}'

resultado_lista = eval(entrada_lista)
resultado_tupla = eval(entrada_tupla)
resultado_dict = eval(entrada_dict)

print("5) eval() → estructuras de datos")
print(f"Entrada lista: {entrada_lista}  → {resultado_lista}  ({type(resultado_lista).__name__})")
print(f"Entrada tupla: {entrada_tupla}  → {resultado_tupla}  ({type(resultado_tupla).__name__})")
print(f"Entrada dict : {entrada_dict}  → {resultado_dict}  ({type(resultado_dict).__name__})\n")


print("=== Fin de ejemplos ===\n")


