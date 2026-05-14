# Try - Except basico

print("=" * 50)
print("EJEMPLO 1: Try-Except basico")
print("=" * 50)

try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es:{resultado}")
except:
    print("¡Ups! No se puede dividir entre cero.")

print()

# Capturando excepciones especificas

print("=" * 50)
print("EJEMPLO 2: Capturando excepciones especificas")
print("=" * 50)

try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"100 dividido por{numero} es{resultado}")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")

print()

# Accediendo a la informacion de la excepcion

print("=" * 50)
print("EJEMPLO 3: Accediendo a la informacion de la excepcion")
print("=" * 50)

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    print(f"Error:{error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")

import os
if os.path.exists("archivo_inexistente.txt"):
    os.remove("archivo_inexistente.txt")

print()

# Combinando multiples excepciones

print("=" * 50)
print("EJEMPLO 4: Combinando multiples excepciones")
print("=" * 50)

try:
    archivo = open("datos.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error:{type(e).__name__}")
    print(f"Descripción:{e}")

print()

# Uso practico en aplicaciones reales

print("=" * 50)
print("EJEMPLO 5: Uso practico - validacion de edad")
print("=" * 50)

def obtener_edad():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Por favor, introduce un número entero.")

edad_usuario = obtener_edad()
print(f"Tu edad es:{edad_usuario}")