#  Los iteradores son objetos que permiten recorrer uno a uno los elementos almacenados en una estructura de datos, y operar con ellos. 
# Los iteradores tienen que implementar un método next que debe devolver los elementos, de a uno por vez, comenzando por el primero. 
# Y al llegar al final de la estructura, debe levantar una excepción de tipo StopIteration.

# Ejemplo de iterador
list = [1, 2, 3, 4]
iterator = iter(list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# se puede iterar en cadenas de texto también
text = "Hola Frand"
iter_text = iter(text)

for char in iter_text:
    print(char)

# Crear un iterador para mostrar números impares

limite = 10
iter_impar = iter(range(1, limite + 1, 2))

for value in iter_impar:
    print(value)