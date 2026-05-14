# Tipos comunes de excepciones

print("=" * 50)
print("EJEMPLO 1: ZeroDivisionError")
print("=" * 50)

try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("No es posible dividir entre cero")

print()

print("=" * 50)
print("EJEMPLO 2: OverflowError")
print("=" * 50)

try:
    resultado = 10.0 ** 1000000
except OverflowError:
    print("El número es demasiado grande para ser representado")

print()

# Excepciones relacionadas con tipos de datos

print("=" * 50)
print("EJEMPLO 3: TypeError")
print("=" * 50)

try:
    resultado = "42" + 10
except TypeError:
    print("No se pueden sumar tipos diferentes")

print()

print("=" * 50)
print("EJEMPLO 4: ValueError")
print("=" * 50)

try:
    numero = int("abc")
except ValueError:
    print("La cadena no representa un número válido")

print()

# Excepciones relacionadas con indices y claves

print("=" * 50)
print("EJEMPLO 5: IndexError")
print("=" * 50)

try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError:
    print("El índice está fuera del rango de la lista")

print()

print("=" * 50)
print("EJEMPLO 6: KeyError")
print("=" * 50)

try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")

print()

# Excepciones relacionadas con archivos

print("=" * 50)
print("EJEMPLO 7: FileNotFoundError")
print("=" * 50)

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")

print()

print("=" * 50)
print("EJEMPLO 8: PermissionError")
print("=" * 50)

try:
    with open("/etc/passwd", "w") as archivo:
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")

print()

# Excepciones relacionadas con atributos y nombres

print("=" * 50)
print("EJEMPLO 9: AttributeError")
print("=" * 50)

try:
    texto = "Hola"
    longitud = texto.size
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")

print()

print("=" * 50)
print("EJEMPLO 10: NameError")
print("=" * 50)

try:
    print(variable_no_definida)
except NameError:
    print("La variable no está definida")

print()

# Excepciones relacionadas con importaciones

print("=" * 50)
print("EJEMPLO 11: ImportError")
print("=" * 50)

try:
    import biblioteca_inexistente
except ImportError:
    print("No se pudo importar el módulo")

print()

print("=" * 50)
print("EJEMPLO 12: ModuleNotFoundError")
print("=" * 50)

try:
    import modulo_que_no_existe
except ModuleNotFoundError:
    print("El módulo no existe")

print()

# Jerarquia de excepciones

print("=" * 50)
print("EJEMPLO 13: Jerarquia con Exception")
print("=" * 50)

try:
    resultado = int("abc") / 0
except Exception as e:
    print(f"Se produjo un error:{type(e).__name__}")
    print(f"Descripción:{e}")

print()

# Identificando el tipo de excepcion

print("=" * 50)
print("EJEMPLO 14: Identificando el tipo de excepcion")
print("=" * 50)

try:
    resultado = eval(input("Introduce una expresión: "))
except Exception as e:
    print(f"Error de tipo:{type(e).__name__}")
    print(f"Descripción:{e}")

print()

# Excepciones en bibliotecas externas

print("=" * 50)
print("EJEMPLO 15: Excepciones en bibliotecas externas")
print("=" * 50)

import requests

try:
    respuesta = requests.get("https://api.ejemplo.com/datos", timeout=1)
    respuesta.raise_for_status()
except requests.exceptions.ConnectionError:
    print("No se pudo conectar al servidor")
except requests.exceptions.Timeout:
    print("La solicitud excedió el tiempo de espera")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP:{e}")