import random

casillas = [" "," "," "," "," "," "," "," "," ",]
casillas_libres = [0,1,2,3,4,5,6,7,8]

you = input("Quieres ser cara o cruz? ")
if you == "x":
    pc = "o"
if you == "o":
    pc = "x"

final = False

while not final:

    if casillas_libres == []:
        print("Empate!")
        final = True

    posicion = int(input("Elige una casilla del 0 al 8: "))
    casillas[posicion] = you
    casillas_libres.remove(posicion)

    if casillas[0] == casillas [1] == casillas [2] == you:
        print("has ganado!")
        final = True
    if casillas[3] == casillas [4] == casillas [5] == you:
        print("has ganado!")
        final = True
    if casillas[6] == casillas [7] == casillas [8] == you:
        print("has ganado!")
        final = True
    if casillas[0] == casillas [3] == casillas [6] == you:
        print("has ganado!")
        final = True
    if casillas[1] == casillas [4] == casillas [7] == you:
        print("has ganado!")
        final = True
    if casillas[2] == casillas [5] == casillas [8] == you:
        print("has ganado!")
        final = True
    if casillas[0] == casillas [4] == casillas [8] == you:
        print("has ganado!")
        final = True
    if casillas[2] == casillas [4] == casillas [6] == you:
        print("has ganado!")
        final = True

    if not casillas_libres == []:
        posicion = random.choice(casillas_libres)
        casillas[posicion] = pc
        casillas_libres.remove(posicion)

    if casillas[0] == casillas [1] == casillas [2] == pc:
        print("has perdido!")
        final= True
    if casillas[3] == casillas [4] == casillas [5] == pc:
        print("has perdido!")
        final = True
    if casillas[6] == casillas [7] == casillas [8] == pc:
        print("has perdido!")
        final = True
    if casillas[0] == casillas [3] == casillas [6] == pc:
        print("has perdido!")
        final = True
    if casillas[1] == casillas [4] == casillas [7] == pc:
        print("has perdido!")
        final = True
    if casillas[2] == casillas [5] == casillas [8] == pc:
        print("has perdido!")
        final = True
    if casillas[0] == casillas [4] == casillas [8] == pc:
        print("has perdido!")
        final = True
    if casillas[2] == casillas [4] == casillas [6] == pc:
        print("has perdido!")
        final = True

    print("| "+casillas[0]+" | "+casillas[1]+" | "+casillas[2]+" |")
    print("| "+casillas[3]+" | "+casillas[4]+" | "+casillas[5]+" |")
    print("| "+casillas[6]+" | "+casillas[7]+" | "+casillas[8]+" |")
