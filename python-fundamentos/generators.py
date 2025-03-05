# los generadores son una forma sencilla de crear iteradores.
# Para crear un generador, se utiliza una función que contiene una o más sentencias yield.
# son útiles para recorrer grandes cantidades de datos, ya que no es necesario cargarlos todos en memoria.

# Ejemplo de generador
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value) 

# Fibonacci

def fibonacci(limit):
    a, b = 5, 6
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(20):
    print("fibonacci: ", num)

# Generador de números impares
def impar(limit):
    x = 0
    while x < limit:
        if x % 2 == 1:
            yield x
        x = x + 1

for num in impar(20):
    print("impar: ", num)