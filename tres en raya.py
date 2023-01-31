casillas = ["","","","","","","","","",]

you = input("Quieres ser cara o cruz? ")
if you == "x":
    pc = "o"
if you == "o":
    pc = "x"

    while fin="no":

    posicion = int(input("Elige una casilla del 0 al 8: "))
    casillas[posicion] = you

    if casillas[0] == casillas [1] == casillas [2] == you:
        print("has ganado!")
    if casillas[3] == casillas [4] == casillas [5] == you:
        print("has ganado!")
    if casillas[6] == casillas [7] == casillas [8] == you:
        print("has ganado!")
    if casillas[0] == casillas [3] == casillas [6] == you:
        print("has ganado!")
    if casillas[1] == casillas [4] == casillas [7] == you:
        print("has ganado!")
    if casillas[2] == casillas [5] == casillas [8] == you:
        print("has ganado!")
    if casillas[0] == casillas [4] == casillas [8] == you:
        print("has ganado!")
    if casillas[2] == casillas [4] == casillas [6] == you:
        print("has ganado!")

    pc = ranom.randit(0,8)

    if casillas[0] == casillas [1] == casillas [2] == pc:
        print("has perdido!")
    if casillas[3] == casillas [4] == casillas [5] == pc:
        print("has perdido!")
    if casillas[6] == casillas [7] == casillas [8] == pc:
        print("has perdido!")
    if casillas[0] == casillas [3] == casillas [6] == pc:
        print("has perdido!")
    if casillas[1] == casillas [4] == casillas [7] == pc:
        print("has perdido!")
    if casillas[2] == casillas [5] == casillas [8] == pc:
        print("has perdido!")
    if casillas[0] == casillas [4] == casillas [8] == pc:
        print("has perdido!")
    if casillas[2] == casillas [4] == casillas [6] == pc:
        print("has perdido!")

    print("| "+casillas[0]+" | "+casillas[1]+" | "+casillas[2]+" |")
    print("| "+casillas[3]+" | "+casillas[4]+" | "+casillas[5]+" |")
    print("| "+casillas[6]+" | "+casillas[7]+" | "+casillas[8]+" |")

    fin = input("ha terminado la partida?")