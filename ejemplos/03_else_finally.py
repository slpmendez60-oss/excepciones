# Clausula else y finally

print("=" * 50)
print("EJEMPLO 1: Clausula else")
print("=" * 50)

try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es:{resultado}")

print()

# Casos de uso practicos para else

print("=" * 50)
print("EJEMPLO 2: Casos de uso para else con archivos")
print("=" * 50)

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    print("Archivo leído correctamente.")
    archivo.close()

print()

print("=" * 50)
print("EJEMPLO 3: Else con operaciones relacionadas")
print("=" * 50)

def obtener_datos_de_api():
    raise ConnectionError("Sin conexion")

def validar_formato(datos):
    pass

def procesar_datos(datos):
    return datos

def guardar_resultados(resultados):
    pass

try:
    datos = obtener_datos_de_api()
    validar_formato(datos)
except ConnectionError:
    print("No se pudo conectar con el servidor.")
except Exception:
    print("Los datos recibidos tienen un formato incorrecto.")
else:
    resultados = procesar_datos(datos)
    guardar_resultados(resultados)

print()

# Clausula finally

print("=" * 50)
print("EJEMPLO 4: Clausula finally con archivo")
print("=" * 50)

import os

try:
    archivo = open("registro.txt", "w")
    archivo.write("Operación iniciada\n")
    resultado = 10 / int(input("Introduce un número: "))
    archivo.write(f"Resultado:{resultado}\n")
except ZeroDivisionError:
    archivo.write("Error: División por cero\n")
except ValueError:
    archivo.write("Error: Valor no válido\n")
finally:
    archivo.write("Operación finalizada\n")
    archivo.close()
    print("Proceso completado")

if os.path.exists("registro.txt"):
    os.remove("registro.txt")

print()

# Casos de uso practicos para finally

print("=" * 50)
print("EJEMPLO 5: Finally - liberar recursos")
print("=" * 50)

def conectar_a_base_de_datos():
    raise Exception("Sin conexion a base de datos")

conexion = None
try:
    conexion = conectar_a_base_de_datos()
except Exception:
    print("Error al conectar con la base de datos")
finally:
    if conexion:
        print("Conexion cerrada")
    else:
        print("No habia conexion que cerrar")

print()

print("=" * 50)
print("EJEMPLO 6: Finally - registrar finalizacion")
print("=" * 50)

def registrar_inicio(tarea):
    print(f"Iniciando:{tarea}")

def ejecutar_tarea_diaria():
    raise Exception("Error en la tarea")

def registrar_error(tarea, error):
    print(f"Error en {tarea}:{error}")

def registrar_finalizacion(tarea):
    print(f"Finalizado:{tarea}")

try:
    registrar_inicio("tarea_diaria")
    ejecutar_tarea_diaria()
except Exception as e:
    registrar_error("tarea_diaria", str(e))
finally:
    registrar_finalizacion("tarea_diaria")

print()

# Combinando else y finally

print("=" * 50)
print("EJEMPLO 7: Combinando else y finally")
print("=" * 50)

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automáticamente")
else:
    print(f"Contenido leído:{contenido}")
finally:
    print("Operación de archivo completada.")
    archivo.close()

if os.path.exists("datos.txt"):
    os.remove("datos.txt")

print()

# Orden de ejecucion

print("=" * 50)
print("EJEMPLO 8: Orden de ejecucion")
print("=" * 50)

def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")
    print("5. Continuando después del bloque try")

demostrar_orden()

print()

# Consideraciones importantes

print("=" * 50)
print("EJEMPLO 9: Return en bloques try finally")
print("=" * 50)

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    finally:
        print("División finalizada")

print(dividir(10, 2))
print(dividir(10, 0))

print()

print("=" * 50)
print("EJEMPLO 10: Excepciones en finally")
print("=" * 50)

try:
    1 / 0
except ZeroDivisionError:
    print("Capturada división por cero")
finally:
    print("Bloque finally ejecutado")