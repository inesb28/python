import random

words = ["poema","software","contento","hierva","periscopio","cenizas","azul","castigado","sentir","fotocopia","esqueleto","robot","esternocleidomastoideo","murcielago","tomate","jirafa",]

word = random.choice(words)

letras_check = []
letras_not = []

play = True

while play:

    for letra in word:
        if letra in letras_check:
            print(letra,end="")
        else:
            print("_ ",end="")

    letra_ask = input("\ndime una letra: \n")
    
    print(letra_ask in word)

    if letra_ask in word:
        letras_check.append(letra_ask)
    else:
        letras_not.append(letra_ask)

    print("correctas: ",letras_check)
    print("incorrectas: ",letras_not)
    if len(letras_not) == 1:
        print("o")
    if len(letras_not) == 2:
        print("o")
        print("|")
    if len(letras_not) == 3:
        print(" o")
        print("[|")
    if len(letras_not) == 4:
        print(" o")
        print("[|]")
    if len(letras_not) == 5:
        print(" o")
        print("[|]")
        print("|")
    if len(letras_not) == 6:
        print(" o")
        print("[|]")
        print("| |")
    if len(letras_not) == 7:
        print("_____")
        print("|  o")
        print("| [|]")
        print("| | |")
    
    if set(letras_check) == set(word):
        play = False
        print("you win!")
    if len(letras_not) == 7:
        play = False
        print("has perdido!")
        print("la palabra secreta era ",word)