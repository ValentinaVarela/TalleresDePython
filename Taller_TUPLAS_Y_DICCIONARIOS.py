#Crear una tupla con números que usted desee, crear dos tuplas vacías llamadas par y la otra impar. A través de un ciclo for recorrer la tupla numérica si el numero evaluado es para ingresar el valor a la tupla par, de lo contrario insertar a la tupla impar.

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = ()
impares = ()

for numero in numeros:
    if numero % 2 == 0:
        pares += (numero,)
    else:
        impares += (numero,)

print("Tupla de números pares:", pares)
print("Tupla de números impares:", impares)

#Crear una tupla con diferentes valores numéricos o cadenas de texto, crear un programa que muestre el elemento mayor y menor de la tupla usando la función correspondiente.

tupla = (3, 8, 1, 5, 2, 9, 7, 4)
mayor = max(tupla)
menor = min(tupla)

print("El elemento mayor de la tupla es:", mayor)
print("El elemento menor de la tupla es:", menor)

#Crea una tupla numérica, pide al usuario que ingrese un número y crea un programa que cuente cuantas veces está el numero ingresado en la tupla, de lo contrario muestre que el número no se encuentra.

tupla_numerica = (1, 3, 5, 2, 4, 6, 8, 3, 7, 9, 3, 5)
numero = int(input("Ingrese un número: "))
contador = 0

for n in tupla_numerica:
    if n == numero:
        contador += 1
if contador > 0:
    print(f"El número {numero} aparece {contador} veces en la tupla.")
else:
    print(f"El número {numero} no se encuentra en la tupla.")

#Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono. Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. No se podrán meter nombres repetidos. Debe imprimir el diccionario creado.

agenda = {}
while True:
    nombre = input("Ingrese el nombre del contacto (o 'no' para salir): ")
    if nombre == 'no':
        break
    if nombre in agenda:
        print("El nombre ya existe en la agenda. Por favor ingrese otro nombre.")
        continue
    telefono = input("Ingrese el teléfono del contacto: ")
    agenda[nombre] = telefono
    
print("Agenda telefónica:")
print(agenda)

#Teniendo en cuenta el punto anterior, crea un programa que solicite al usuario la clave(usuario) y muestre el teléfono correspondiente

nombre = input("Ingrese el nombre del contacto: ")

if nombre in agenda:
    print(f"El teléfono de {nombre} es {agenda[nombre]}.")
else:
    print(f"{nombre} no se encuentra en la agenda.")

#Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indice = int(input("Ingrese un índice entre 0 y 9: "))

if indice < 0 or indice > 9:
    print("El índice ingresado no es válido")
else:
    print(f"Los valores en la posición {indice} son {tupla[indice]}")

#Encuentra los errores en los siguientes ejemplos de lista:                          lista_colores ["rojo", "azul", "verde", 'amarillo']

"""El error que esta demostrando esta lista es que hace falta el signo de igualdad para asignar los valores a la variable "lista_colores", Además, el valor 'amarillo' está utilizando comillas simples en lugar de comillas dobles, lo que no es un error en sí mismo, pero puede causar problemas de estilo y legibilidad en el código."""
"""Asi sería la forma correcta de declarar la lista"""
lista_colores = ["rojo", "azul", "verde", "amarillo"]

#Encuentra los errores en los siguientes ejemplos de lista:                          lista_colores = ["rojo", "azul", "verde", "amarillo"]                                        print(lista_colores(0))

"""El error en el código presentado es que se está intentando acceder al primer elemento de la lista utilizando la sintaxis de una función en lugar de la sintaxis de indexación. La sintaxis correcta para acceder al primer elemento de una lista es utilizando corchetes, de la siguiente manera"""
lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[0])

#Encuentra los errores en los siguientes ejemplos de lista                           lista_colores = ["rojo", "azul", "verde"]                                                        print(lista_colores[-0])                                                                     print(lista_colores[-4])

"""En el código presentado no hay errores de sintaxis, pero hay un error lógico en la línea print(lista_colores[-0]). El índice '-0' es equivalente al índice '0', por lo que se estaría intentando acceder al primer elemento de la lista, lo que no es un problema en sí mismo, pero utilizar '-0' puede causar confusión y es innecesario.

En la línea print(lista_colores[-4]) se está intentando acceder a un elemento fuera del rango de la lista. El índice '-4' corresponde al cuarto elemento contando desde el final de la lista, pero la lista lista_colores solo tiene tres elementos. Por lo tanto, este código producirá un error de índice fuera de rango. El índice válido más bajo para esta lista sería '-3', que corresponde al primer elemento contando desde el final de la lista."""