#  En este ejercicio vamos a realizar una calculadora que realice las operaciones básicas de suma, resta, multiplicación y división.
# Utilizando los conocimientos adquiridoas hasta el momento 

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir entre 0"
    return num1 / num2

def calculator():
    operations = {
        "suma", "resta", "multiplicacion", "division"
    }
    
    print("Operaciones disponibles: ", operations)

    operation = input("Introduce la operación que deseas realizar: ")
    
    if operation not in operations:
        print("Operación no válida")
        return

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operation == "suma":
        print(suma(num1, num2))
    elif operation == "resta":
        print(resta(num1, num2))
    elif operation == "multiplicacion":
        print(multiplicacion(num1, num2))
    elif operation == "division":
        print(division(num1, num2))


calculator()

