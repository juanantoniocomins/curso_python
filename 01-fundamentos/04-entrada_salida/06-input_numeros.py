"""
Cómo manejar números (int y float) con input(), cubriendo los tres métodos principales de conversión y validación:

1. 🔢 Conversión Directa (Método Simple pero Riesgoso)
        Convertir directamente el resultado de input() usando int() o float() sin validación.
        
        Comportamiento Clave
        Conversión Explícita: input() SIEMPRE devuelve str, por lo que DEBES convertir manualmente a int o float.
        
        Riesgo de Error: Si el usuario introduce texto en lugar de número, el programa crashea con ValueError.

2. 🛡️ Conversión con Validación (Método Seguro y Recomendado)
        Usar try-except para capturar errores de conversión y manejarlos apropiadamente.
        
        Comportamiento Clave
        Prevención de Crashes: El programa no se detiene si el usuario introduce datos inválidos.
        
        Retroalimentación al Usuario: Permite informar al usuario del error y solicitar nuevo dato.
        
        Bucles de Validación: Se puede repetir la solicitud hasta obtener un dato válido.

3. 🎯 Conversión con Funciones de Validación (Método Profesional)
        Crear funciones reutilizables que validen y conviertan datos, permitiendo restricciones adicionales.
        
        Comportamiento Clave
        Reutilizable: Las funciones se pueden usar en múltiples lugares del programa.
        
        Validaciones Personalizadas: Puedes agregar restricciones (rangos, valores positivos, etc.).
        
        Código Limpio: Separa la lógica de validación del flujo principal del programa.
"""

####################################### 1. CONVERSIÓN DIRECTA (RIESGOSA) ########################################

print("=" * 80)
print("1. CONVERSIÓN DIRECTA - Método Simple pero Riesgoso")
print("=" * 80)

# Conversión directa a int
# ⚠️ CUIDADO: Si el usuario escribe "abc" en lugar de un número, el programa crashea
try:
    edad = int(input("¿Cuántos años tienes? "))
    print(f"Tienes {edad} años.")
    print(f"Tipo de dato: {type(edad)}")
except ValueError:
    print("❌ ERROR: No has introducido un número entero válido.")

print("-" * 80)

# Conversión directa a float
# ⚠️ CUIDADO: Acepta decimales con punto (.) pero no con coma (,)
try:
    peso = float(input("¿Cuál es tu peso en kg? (usa punto decimal, ej: 70.5): "))
    print(f"Tu peso es {peso} kg.")
    print(f"Tipo de dato: {type(peso)}")
except ValueError:
    print("❌ ERROR: No has introducido un número decimal válido.")

print("-" * 80)

# Operaciones aritméticas directas
try:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    # División requiere cuidado adicional (división por cero)
    if num2 != 0:
        division = num1 / num2
        print(f"\nResultados:")
        print(f"{num1} + {num2} = {suma}")
        print(f"{num1} - {num2} = {resta}")
        print(f"{num1} × {num2} = {multiplicacion}")
        print(f"{num1} ÷ {num2} = {division:.2f}")
    else:
        print("❌ No se puede dividir por cero.")
        
except ValueError:
    print("❌ ERROR: Debes introducir números válidos.")

print("\n")


####################################### 2. CONVERSIÓN CON VALIDACIÓN (SEGURO) ########################################

print("=" * 80)
print("2. CONVERSIÓN CON VALIDACIÓN - Método Seguro y Recomendado")
print("=" * 80)

# Validación con try-except simple
print("Introduce tu altura en metros:")
while True:
    try:
        altura = float(input("Altura: "))
        if altura > 0:  # Validación adicional: debe ser positivo
            print(f"✅ Altura válida: {altura} m")
            break
        else:
            print("❌ La altura debe ser un número positivo.")
    except ValueError:
        print("❌ Error: Introduce un número decimal válido (ej: 1.75)")

print("-" * 80)

# Validación con límites (rango)
print("Introduce tu edad (entre 0 y 120):")
edad_valida = False
while not edad_valida:
    try:
        edad = int(input("Edad: "))
        if 0 <= edad <= 120:
            print(f"✅ Edad válida: {edad} años")
            edad_valida = True
        else:
            print("❌ La edad debe estar entre 0 y 120.")
    except ValueError:
        print("❌ Error: Introduce un número entero válido.")

print("-" * 80)

# Validación con múltiples intentos
print("Introduce un número entre 1 y 10 (tienes 3 intentos):")
intentos = 3
numero_correcto = False

for intento in range(1, intentos + 1):
    try:
        numero = int(input(f"Intento {intento}/{intentos}: "))
        if 1 <= numero <= 10:
            print(f"✅ ¡Correcto! Has introducido: {numero}")
            numero_correcto = True
            break
        else:
            print(f"❌ El número debe estar entre 1 y 10. Te quedan {intentos - intento} intentos.")
    except ValueError:
        print(f"❌ No es un número válido. Te quedan {intentos - intento} intentos.")

if not numero_correcto:
    print("❌ Has agotado todos los intentos.")

print("-" * 80)

# Validación de múltiples números con split()
print("Introduce tres calificaciones separadas por espacios (ej: 8.5 9.0 7.5):")
while True:
    try:
        entrada = input("Calificaciones: ")
        calificaciones = [float(x) for x in entrada.split()]
        
        if len(calificaciones) != 3:
            print(f"❌ Necesitas introducir exactamente 3 números. Has introducido {len(calificaciones)}.")
            continue
        
        # Validar rango (0-10)
        if all(0 <= cal <= 10 for cal in calificaciones):
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"✅ Calificaciones: {calificaciones}")
            print(f"📊 Promedio: {promedio:.2f}")
            break
        else:
            print("❌ Todas las calificaciones deben estar entre 0 y 10.")
            
    except ValueError:
        print("❌ Error: Asegúrate de introducir solo números separados por espacios.")

print("\n")


####################################### 3. FUNCIONES DE VALIDACIÓN (PROFESIONAL) ########################################

print("=" * 80)
print("3. FUNCIONES DE VALIDACIÓN - Método Profesional y Reutilizable")
print("=" * 80)

# Función genérica para leer enteros con validación
def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Lee un número entero del usuario con validación opcional de rango.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (int): Valor mínimo permitido (opcional)
        maximo (int): Valor máximo permitido (opcional)
    
    Returns:
        int: Número entero validado
    """
    while True:
        try:
            numero = int(input(mensaje))
            
            # Validar rango si se especificó
            if minimo is not None and numero < minimo:
                print(f"❌ El número debe ser al menos {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"❌ El número debe ser como máximo {maximo}.")
                continue
            
            return numero
            
        except ValueError:
            print("❌ Error: Debes introducir un número entero válido.")


# Función genérica para leer flotantes con validación
def leer_float(mensaje, minimo=None, maximo=None, decimales=2):
    """
    Lee un número decimal del usuario con validación opcional de rango.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (float): Valor mínimo permitido (opcional)
        maximo (float): Valor máximo permitido (opcional)
        decimales (int): Número de decimales a mostrar en mensajes
    
    Returns:
        float: Número decimal validado
    """
    while True:
        try:
            numero = float(input(mensaje))
            
            # Validar rango si se especificó
            if minimo is not None and numero < minimo:
                print(f"❌ El número debe ser al menos {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"❌ El número debe ser como máximo {maximo}.")
                continue
            
            return round(numero, decimales)
            
        except ValueError:
            print("❌ Error: Debes introducir un número decimal válido.")


# Función para leer números positivos
def leer_positivo(mensaje, tipo='int'):
    """
    Lee un número positivo (mayor que 0).
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        tipo (str): 'int' o 'float'
    
    Returns:
        int o float: Número positivo validado
    """
    while True:
        try:
            if tipo == 'int':
                numero = int(input(mensaje))
            else:
                numero = float(input(mensaje))
            
            if numero > 0:
                return numero
            else:
                print("❌ El número debe ser positivo (mayor que 0).")
                
        except ValueError:
            print(f"❌ Error: Debes introducir un número {tipo} válido.")


# Ejemplos de uso de las funciones
print("Usando funciones de validación:\n")

# Leer edad (entre 0 y 120)
edad = leer_entero("Introduce tu edad (0-120): ", minimo=0, maximo=120)
print(f"✅ Edad registrada: {edad} años\n")

# Leer precio (positivo)
precio = leer_positivo("Introduce el precio del producto: $", tipo='float')
print(f"✅ Precio registrado: ${precio:.2f}\n")

# Leer temperatura (puede ser negativa)
temperatura = leer_float("Introduce la temperatura en °C (-50 a 50): ", minimo=-50, maximo=50)
print(f"✅ Temperatura registrada: {temperatura}°C\n")

# Leer cantidad (entero positivo)
cantidad = leer_positivo("Introduce la cantidad de productos: ", tipo='int')
print(f"✅ Cantidad registrada: {cantidad} unidades\n")

print("-" * 80)


####################################### CASOS PRÁCTICOS COMPLETOS ########################################

print("=" * 80)
print("CASOS PRÁCTICOS COMPLETOS")
print("=" * 80)

# Caso 1: Calculadora de IMC (Índice de Masa Corporal)
print("\n📊 CALCULADORA DE IMC")
print("-" * 40)

peso = leer_positivo("Introduce tu peso en kg: ", tipo='float')
altura = leer_positivo("Introduce tu altura en metros (ej: 1.75): ", tipo='float')

imc = peso / (altura ** 2)

print(f"\n📈 Resultados:")
print(f"   Peso: {peso} kg")
print(f"   Altura: {altura} m")
print(f"   IMC: {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"   Categoría: {categoria}")

print("-" * 80)

# Caso 2: Calculadora de Interés Compuesto
print("\n💰 CALCULADORA DE INTERÉS COMPUESTO")
print("-" * 40)

capital_inicial = leer_positivo("Capital inicial ($): ", tipo='float')
tasa_interes = leer_float("Tasa de interés anual (%, ej: 5.5): ", minimo=0, maximo=100)
años = leer_entero("Años de inversión: ", minimo=1, maximo=100)

# Fórmula: Monto Final = Capital * (1 + tasa/100)^años
monto_final = capital_inicial * ((1 + tasa_interes/100) ** años)
ganancia = monto_final - capital_inicial

print(f"\n📊 Proyección de Inversión:")
print(f"   Capital inicial: ${capital_inicial:,.2f}")
print(f"   Tasa de interés: {tasa_interes}% anual")
print(f"   Período: {años} años")
print(f"   Monto final: ${monto_final:,.2f}")
print(f"   Ganancia total: ${ganancia:,.2f}")
print(f"   Rentabilidad: {(ganancia/capital_inicial)*100:.2f}%")

print("-" * 80)

# Caso 3: Conversor de Monedas
print("\n💱 CONVERSOR DE MONEDAS")
print("-" * 40)

cantidad_euros = leer_positivo("Cantidad en Euros (€): ", tipo='float')
tasa_cambio = leer_positivo("Tasa de cambio EUR a USD (ej: 1.18): ", tipo='float')

cantidad_dolares = cantidad_euros * tasa_cambio

print(f"\n💵 Conversión:")
print(f"   {cantidad_euros:,.2f} € = {cantidad_dolares:,.2f} $")
print(f"   Tasa de cambio: 1 € = {tasa_cambio} $")

print("-" * 80)


####################################### COMPARATIVA DE MÉTODOS ########################################

print("\n")
print("=" * 80)
print("📋 COMPARATIVA DE MÉTODOS")
print("=" * 80)

comparativa = """
╔═══════════════════════╦═══════════════════╦═══════════════════╦═══════════════════╗
║ Aspecto               ║ Conversión Directa║ Con Validación    ║ Con Funciones     ║
╠═══════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║ Facilidad de uso      ║ ⭐⭐⭐            ║ ⭐⭐              ║ ⭐⭐⭐           ║
║ Seguridad             ║ ❌ Baja           ║ ✅ Alta           ║ ✅ Muy Alta      ║
║ Código requerido      ║ Mínimo            ║ Moderado          ║ Inicial alto      ║
║ Reutilizable          ║ ❌ No             ║ ⚠️ Limitado       ║ ✅ Sí            ║
║ Manejo de errores     ║ ❌ No             ║ ✅ Sí             ║ ✅ Sí            ║
║ Validación avanzada   ║ ❌ No             ║ ⚠️ Manual         ║ ✅ Automática    ║
║ Uso recomendado       ║ Scripts simples   ║ Programas medianos║ Proyectos grandes ║
╚═══════════════════════╩═══════════════════╩═══════════════════╩═══════════════════╝

🎯 RECOMENDACIÓN:
   • Para scripts de prueba: Conversión Directa
   • Para programas escolares: Con Validación
   • Para proyectos profesionales: Con Funciones
"""

print(comparativa)

print("=" * 80)
print("🎓 FIN DEL TUTORIAL - ¡Domina el manejo de números con input()!")
print("=" * 80)
