# Lanzar excepciones con raise

print("=" * 50)
print("EJEMPLO 1: Usando raise")
print("=" * 50)

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Error:{e}")

print()

# Cuando lanzar excepciones

print("=" * 50)
print("EJEMPLO 2: Validacion de parametros")
print("=" * 50)

def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

try:
    print(calcular_raiz_cuadrada(16))
    print(calcular_raiz_cuadrada(-4))
except ValueError as e:
    print(f"Error:{e}")

print()

print("=" * 50)
print("EJEMPLO 3: Estados imposibles")
print("=" * 50)

def procesar_respuesta(respuesta):
    if respuesta["codigo"] == 200:
        return respuesta["datos"]
    elif respuesta["codigo"] == 404:
        return None
    else:
        raise RuntimeError(f"Código de respuesta no manejado:{respuesta['codigo']}")

try:
    print(procesar_respuesta({"codigo": 200, "datos": "OK"}))
    print(procesar_respuesta({"codigo": 500, "datos": ""}))
except RuntimeError as e:
    print(f"Error:{e}")

print()

print("=" * 50)
print("EJEMPLO 4: Precondiciones con raise")
print("=" * 50)

def retirar_dinero(cuenta, cantidad):
    if not cuenta["activa"]:
        raise ValueError("La cuenta no está activa")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if cantidad > cuenta["saldo"]:
        raise ValueError("Saldo insuficiente")
    cuenta["saldo"] -= cantidad
    return cuenta["saldo"]

cuenta = {"activa": True, "saldo": 500}

try:
    print(retirar_dinero(cuenta, 200))
    print(retirar_dinero(cuenta, 400))
except ValueError as e:
    print(f"Error:{e}")

print()

# Tipos de excepciones para lanzar

print("=" * 50)
print("EJEMPLO 5: ValueError y TypeError con raise")
print("=" * 50)

def establecer_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")
    return edad

for valor in ["veinte", -5, 200, 25]:
    try:
        edad = establecer_edad(valor)
        print(f"Edad válida: {edad}")
    except (TypeError, ValueError) as e:
        print(f"Error con '{valor}': {e}")

print()

print("=" * 50)
print("EJEMPLO 6: RuntimeError con raise")
print("=" * 50)

def hay_conexion_internet():
    return False

def conectar_a_servidor():
    if not hay_conexion_internet():
        raise RuntimeError("No hay conexión a Internet")

try:
    conectar_a_servidor()
except RuntimeError as e:
    print(f"Error:{e}")

print()

# Relanzando excepciones

print("=" * 50)
print("EJEMPLO 7: Relanzando excepciones")
print("=" * 50)

def procesar_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error:{e}")
        raise

try:
    contenido = procesar_archivo("no_existe.txt")
except FileNotFoundError:
    print("Error manejado en el nivel superior")

print()

# Excepciones personalizadas

print("=" * 50)
print("EJEMPLO 8: Excepciones personalizadas")
print("=" * 50)

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo
        mensaje = f"No hay suficiente saldo. Saldo:{saldo}, Cantidad solicitada:{cantidad}"
        super().__init__(mensaje)

def retirar(cuenta, cantidad):
    if cantidad > cuenta["saldo"]:
        raise SaldoInsuficienteError(cuenta["saldo"], cantidad)
    cuenta["saldo"] -= cantidad
    return cuenta["saldo"]

cuenta = {"titular": "Carlos", "saldo": 500}

try:
    print(retirar(cuenta, 200))
    print(retirar(cuenta, 400))
except SaldoInsuficienteError as e:
    print(f"Error:{e}")
    print(f"Déficit:{e.deficit}")

print()

# Buenas practicas

print("=" * 50)
print("EJEMPLO 9: Buenas practicas - mensajes claros")
print("=" * 50)

# Poco util
try:
    raise ValueError("Fecha inválida")
except ValueError as e:
    print(f"Poco util: {e}")

# Mejor
try:
    raise ValueError("La fecha '2023-13-45' no es válida. El formato debe ser YYYY-MM-DD")
except ValueError as e:
    print(f"Mejor: {e}")

print()

print("=" * 50)
print("EJEMPLO 10: Buenas practicas - excepciones especificas")
print("=" * 50)

import os

ruta = "archivo_que_no_existe.txt"

# Demasiado generico
try:
    if not os.path.exists(ruta):
        raise Exception("Problema con el archivo")
except Exception as e:
    print(f"Generico: {e}")

# Mejor
try:
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo:{ruta}")
except FileNotFoundError as e:
    print(f"Especifico: {e}")

print()

print("=" * 50)
print("EJEMPLO 11: Buenas practicas - validacion temprana")
print("=" * 50)

def procesar_datos(datos):
    if datos is None:
        raise ValueError("Los datos no pueden ser None")
    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")
    return datos

for entrada in [None, "texto", [], [1, 2, 3]]:
    try:
        resultado = procesar_datos(entrada)
        print(f"Datos validos: {resultado}")
    except (ValueError, TypeError) as e:
        print(f"Error con {entrada}: {e}")

print()

# Ejemplo practico validacion de entrada

print("=" * 50)
print("EJEMPLO 12: Validacion de entrada de usuario")
print("=" * 50)

def obtener_edad_validada():
    while True:
        try:
            entrada = input("Introduce tu edad: ")
            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")
            edad = int(entrada)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            if edad > 120:
                raise ValueError("La edad parece demasiado alta")
            return edad
        except ValueError as e:
            if str(e).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")
            else:
                print(f"Error:{e}")

try:
    edad_usuario = obtener_edad_validada()
    print(f"Tu edad es:{edad_usuario}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")