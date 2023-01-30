import random

juego = input("Quieres jugar? ")

while juego == "si":

    usuario = input("¿Pierda, Papel o Tijeras? ")
    ordenador = random.randint(1,3)

    if usuario == "Piedra":
        usuario = 1

    if usuario == "Papel":
        usuario = 2
        
    if usuario == "Tijeras":
        usuario = 3

    if usuario == ordenador:
        print("¡Empate!")

    # Cuando tú sacas piedra
    if usuario == 1 and ordenador == 2:
        print("¡Has perdido!")

    if usuario == 1 and ordenador == 3:
        print("¡Has ganado!")

    #Cuando tú sacas papel
    if usuario == 2 and ordenador == 3:
        print("¡Has perdido!")

    if usuario == 2 and ordenador == 1:
        print("¡Has ganado!")

    #Cuando tú sacas piedra
    if usuario == 3 and ordenador == 1:
        print("¡Has perdido!")

    if usuario == 3 and ordenador == 2:
        print("¡Has ganado!")


    if ordenador == 1:
        ordenador = "Piedra"

    if ordenador == 2:
        ordenador = "Papel"
        
    if ordenador == 3:
        ordenador = "Tijeras"

    print("El ordenador había elegido "+ordenador)

    juego = input("Quieres volver a jugar? ")
    
if juego == "no":
    print("adiós :D")