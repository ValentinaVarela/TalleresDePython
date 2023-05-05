import math

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "No es posible dividir entre cero"
    else:
        return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

while True:
    print("\n** CALCULADORA **")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz cuadrada")
    print("8. Cambiar números")
    print("9. Salir")

    opcion = input("\nIngrese el número de la opción deseada: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == "5":
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
        resultado = potencia(num1, num2)
        print("El resultado de la potenciación es:", resultado)
    elif opcion == "6":
        num = int(input("Ingrese el número para calcular su factorial: "))
        resultado = factorial(num)
        print("El factorial de", num, "es:", resultado)
    elif opcion == "7":
        num = int(input("Ingrese el número para calcular su raíz cuadrada: "))
        if num < 0:
            print("El número debe ser positivo")
        else:
            resultado = math.sqrt(num)
            print("La raíz cuadrada de", num, "es:", resultado)
    elif opcion == "8":
        continue
    elif opcion == "9":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 9.")