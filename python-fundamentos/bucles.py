# El bucle for me iterará sobre una lista de datos   y me imprimirá cada uno de ellos

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

names = ["Juan", "Pedro", "María", "Ana"] 
for name in names:
    print(name)

# también podemos utilizar el métopdo range() para generar una secuencia de números
# range(5) generará una secuencia de números desde 0 hasta 4
# range(1, 5) generará una secuencia de números desde 1 hasta 4

for number in range(5):
    print("range(5): ", number)

for number in range(1, 5):
    print("range(1, 5): ", number)

# El bucle while me permite ejecutar un bloque de código mientras una condición sea verdadera
# En este caso, el bucle se ejecutará mientras el número sea menor a 5

numbers = [1, 2, 3, 4, 5]

i = 0
while i < 5:
    print("i = ", i)
    i += 1

#  También podemos utilizar la palabra clave break para salir del bucle
# En este caso, el bucle se ejecutará mientras el número sea menor a 5, pero si el número es igual a 3, saldrá del bucle

x = 0

while x < 5:
    print("x= ", x)
    if x == 3:
        break
    x += 1

#  El método continue me permite saltar a la siguiente iteración del bucle

y = 0
while y < 8:
    y += 1
    if y == 5:
        continue
    print("continue: ", y)