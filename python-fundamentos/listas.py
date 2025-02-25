# Es una estructura de daos que permite almacenar varios valores en una sola variable u objeto.
# Las listas se pueden crear utilizando corchetes [] y separando los valores con comas.
# Las listas pueden contener cualquier tipo de dato, incluso otras listas.
# Las listas son mutables, es decir, se pueden modificar después de haber sido creadas.

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas de texto
nombres = ["Ana", "Luis", "María"]

# Lista mixta (diferentes tipos de datos)
mixta = [10, "Hola", 3.14, True]

print(numeros)
print(nombres)
print(mixta)

# Acceder a los elementos de una lista
# Para acceder a los elementos de una lista se utiliza el índice del elemento entre corchetes [].
# El índice de los elementos de una lista empieza en 0.
# Si se utiliza un índice negativo, se empieza a contar desde el final de la lista.

print(numeros[3])  # 4
print(nombres[1])  # Luis
print(mixta[-1])  # True último elemento

# Modificar elementos de una lista

numeros[1] = 20
print(numeros)  # [1, 2, 10, 4, 5]

# Agregar elementos a una lista
# Para agregar elementos a una lista se utiliza el método append().
# Este método añade un elemento al final de la lista.

numeros.append(6)
print(numeros)  # [1, 2, 10, 4, 5, 6]

# con insert() se puede agregar un elemento en una posición específica de la lista.
numeros.insert(2, 3)
print(numeros)  # [1, 2, 3, 10, 4, 5, 6]

# extend() permite agregar varios elementos al final de la lista.
numeros.extend([7, 8, 9])
print(numeros)  # [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]

# Eliminar elementos de una lista
# Para eliminar elementos de una lista se utiliza el método remove().
# Este método recibe como argumento el valor del elemento a eliminar.

numeros.remove(8)
print(numeros)  

# Para eliminar un elemento por su índice se utiliza el método pop().
numeros.pop(2)
print(numeros)  

# Elimina el primer elemento de la lista
del numeros[0]
print(numeros)  

# Para eliminar todos los elementos de una lista se utiliza el método clear().
numeros.clear()
print(numeros)  # []


# Recorrer una lista
# Se puede recorrer una lista utilizando un ciclo for.

nombres = ["Ana", "Luis", "María", "Frand"]
for nombre in nombres:
    print(nombre)

# También podemos recorrer la lista usando enumerate() para obtener el índice de cada elemento.

for i, nombre in enumerate(nombres):
    print(f"índice {i}: {nombre}")

# len() permite obtener la longitud de una lista.
print(len(nombres))  # 4

# sorted() permite ordenar los elementos de una lista.
print(sorted(nombres))  # ['Ana', 'Frand', 'Luis', 'María']

# sort() permite ordenar los elementos de una lista directamente.
nombres.sort()
print(nombres)  # ['Ana', 'Frand', 'Luis', 'María']

# reverse() permite invertir el orden de los elementos de una lista.
nombres.reverse()
print(nombres)  # ['María', 'Luis', 'Frand', 'Ana']