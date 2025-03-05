# lambda es una palabra clave en Python que se utiliza para definir funciones anónimas.
# Las funciones anónimas son funciones que no tienen un nombre.
# Por lo general, se utilizan en un lugar donde no se necesita una función normal.
# Las funciones anónimas se definen utilizando la palabra clave lambda seguida de los argumentos de la función.

# Función anónima que suma dos números
add = lambda a, b: a + b
print(add(2, 5))

# Función anónima que multiplica dos números
multiply = lambda a, b: a * b
print(multiply(2, 5))

#  map() aplica una función a todos los elementos de una lista
numbers = range(11)
squared_numbers = list(map(lambda x : x**2, numbers))
print(squared_numbers)

# filter() crea una lista de elementos para los cuales una función devuelve True
# vamos a mostrar los números pares de una lista
numbers = range(11)
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)
