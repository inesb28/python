word = ("azul")

letras_check = []
letras_not = []

while True:

    for letra in word:
        if letra in letras_check:
            print(letra,end=" ")
        else:
            print("_",end=" ")

    letra_ask = input("\ndime una letra: \n")

    print(letra_ask in word)
    if letra_ask in word:
        letras_check.append(letra_ask)
    else:
        letras_not.append(letra_ask)

    print("correctas: ",letras_check)
    print("incorrectas: ",letras_not)