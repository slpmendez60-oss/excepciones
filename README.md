Excepciones en Python

Que son las excepciones?
En Python, una excepcion es un error que ocurre durante la ejecucion
de un programa y que interrumpe su flujo normal. Con manejo de excepciones
podemos capturar ese error y decidir que hacer, permitiendo que el programa
continue de forma controlada.

Diferencia entre except, else y finally

except: Solo cuando ocurre una excepcion en el bloque try
else: Solo cuando NO ocurre ninguna excepcion en el bloque try
finally: Siempre se ejecuta, haya o no excepcion

Estructura del proyecto

excepciones/
    ejemplos/
        01_try_except.py
        02_tipos_comunes.py
        03_else_finally.py
        04_raise_personalizadas.py
    reto/
        dividir_numeros.py
    README.md

Descripcion de los archivos

01_try_except.py
Contiene los ejemplos basicos de try-except, captura de excepciones
especificas, acceso a la informacion de la excepcion, combinacion de
multiples excepciones y uso practico con validacion de datos.

02_tipos_comunes.py
Contiene ejemplos de los tipos de excepciones mas frecuentes en Python
como ZeroDivisionError, ValueError, TypeError, IndexError, KeyError,
FileNotFoundError, PermissionError, AttributeError, NameError,
ImportError y ModuleNotFoundError.

03_else_finally.py
Contiene ejemplos de las clausulas else y finally, casos de uso practicos,
combinacion de ambas clausulas, orden de ejecucion y consideraciones
importantes sobre return en bloques try.

04_raise_personalizadas.py
Contiene ejemplos de como lanzar excepciones con raise, cuando lanzar
excepciones, tipos de excepciones para lanzar, como relanzar excepciones,
creacion de excepciones personalizadas y buenas practicas.

dividir_numeros.py
Solucion del reto practico. Funcion que solicita dos numeros al usuario,
realiza la division y maneja correctamente ValueError y ZeroDivisionError,
mostrando siempre el mensaje de finalizacion con finally.

Reflexion
El manejo de excepciones es una de las habilidades mas importantes en
programacion porque en el mundo real los datos que recibimos rara vez son
perfectos. Sin excepciones, un solo error detiene todo el programa y deja
al usuario sin ninguna explicacion util. Con excepciones podemos anticipar
esos fallos, mostrar mensajes claros y permitir que el programa se recupere
o termine de forma ordenada. La clausula finally es especialmente valiosa
porque garantiza que siempre se ejecute el codigo de limpieza sin importar
si hubo error o no.