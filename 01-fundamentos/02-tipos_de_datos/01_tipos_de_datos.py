print("--- 1. Tipos Numéricos (int, float, complex) ---")

# Entero (int): Números sin decimales
edad = 35
print(f"1. Entero (int): {edad}, Tipo: {type(edad)}")

# Flotante (float): Números con decimales
altura = 1.78
print(f"2. Flotante (float): {altura}, Tipo: {type(altura)}")

# Complejo (complex): Parte real (5) e imaginaria (3j)
numero_complejo = 5 + 3j
print(f"3. Complejo (complex): {numero_complejo}, Tipo: {type(numero_complejo)}")

print("\n--- 2. Tipo de Secuencia de Texto (str) ---")

# Cadena de Texto (str): Secuencia de caracteres
nombre_curso = "Curso de Python Básico"
print(f"4. Cadena (str): {nombre_curso}, Tipo: {type(nombre_curso)}")

print("\n--- 3. Tipo Booleano (bool) ---")

# Booleano (bool): Solo True o False
es_activo = True
es_nulo = False
print(f"5. Booleano (True): {es_activo}, Tipo: {type(es_activo)}")
print(f"6. Booleano (False): {es_nulo}, Tipo: {type(es_nulo)}")

print("\n--- 4. Tipos de Secuencia (list, tuple) ---")

# Lista (list): Colección ordenada, MUTABLE (se puede modificar)
habilidades = ["Python", "Git", "SQL"]
habilidades.append("HTML")
print(f"7. Lista (list): {habilidades}, Tipo: {type(habilidades)}")

# Tupla (tuple): Colección ordenada, INMUTABLE (no se puede modificar)
coordenadas = (40.71, -74.00)
print(f"8. Tupla (tuple): {coordenadas}, Tipo: {type(coordenadas)}")

print("\n--- 5. Tipos de Mapeo y Conjunto (dict, set) ---")

# Diccionario (dict): Pares clave-valor, NO ordenado, mutable
perfil = {"nombre": "Juan", "edad": 35, "ciudad": "Valencia"}
print(f"9. Diccionario (dict): {perfil}, Tipo: {type(perfil)}")

# Conjunto (set): Colección NO ordenada, solo elementos ÚNICOS
etiquetas = {"Avanzado", "Python", "Básico", "Avanzado"} # 'Avanzado' solo aparece una vez
print(f"10. Conjunto (set): {etiquetas}, Tipo: {type(etiquetas)}")

print("\n--- 6. Tipo 'Ninguno' (NoneType) ---")

# NoneType: Representa la ausencia de valor
valor_nulo = None
print(f"11. NoneType (None): {valor_nulo}, Tipo: {type(valor_nulo)}")