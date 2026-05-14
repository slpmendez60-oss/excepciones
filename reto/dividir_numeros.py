# Reto - Manejo de excepciones

def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos numeros
        num1 = input("Ingresa el primer numero: ")
        num2 = input("Ingresa el segundo numero: ")

        # Convertir las entradas a numeros enteros
        num1 = int(num1)
        num2 = int(num2)

        # Realizar la division del primer numero entre el segundo
        resultado = num1 / num2

        # Devolver el resultado de la division
        print(f"Resultado: {num1} / {num2} = {resultado}")
        return resultado

    except ValueError:
        print("Error: Debes introducir un número válido")

    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")

    finally:
        print("Operación finalizada")


# Llamada a la funcion
dividir_numeros()