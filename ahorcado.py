import random

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
words = ["azul","gato","casa","lata",]
word = random.choice(words)
print(word)

if word == "azul":
    un = "a"
    dos = "z"
    tres = "u"
    cuatro = "l"
if word == "gato":
    un = "g"
    dos = "a"
    tres = "t"
    cuatro = "o"
if word == "casa":
    un = "c"
    dos = "a"
    tres = "s"
    cuatro = "a"
if word == "lata":
    un = "l"
    dos = "a"
    tres = "t"
    cuatro = "a"

print(un+dos+tres+cuatro)

while not letras == []:
    mine = input("dime una letra: ")
    letras.remove(mine)

    if mine == un:
        print(un+"_ _ _")
    if mine == dos:
        print("_"+dos+"_ _")
    if mine == tres:
        print("_ _"+tres+"_")
    if mine == cuatro:
        print("_ _ _"+cuatro)

