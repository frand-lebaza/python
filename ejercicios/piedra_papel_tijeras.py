# Voy a crear un juego de piedra, papel o tijeras.
#  Necesito que hayan dos usuarios, que ingresen su elección y que el programa determine quién ganó.

print("Juego de piedra, papel o tijeras")
options = ["piedra", "papel", "tijeras"]
print("Las opciones son: ", options)

for option in options:
    user_1 = input("User1 Ingrese su elección: ")
    
    if user_1 != option:
        print("Opción inválida")
        break
    
    if user_1 == option:
        user_2 = input("User2 Ingrese su elección: ")
    
    if user_2 != option:
        print("Opción inválida")
        break


if user_1 == user_2:
    print("Empate")
elif user_1 == options[0] and user_2 == options[2]:
    print("Gana user1")
elif user_1 == options[1] and user_2 == options[0]:
    print("Gana user1")
elif user_1 == options[2] and user_2 == options[0]:
    print("Gana user1")
else:
    print("Gana user2") 