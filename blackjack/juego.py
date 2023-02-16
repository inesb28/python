from baraja import Baraja
from mano import Mano

mibaraja = Baraja()
mano1 = Mano()
mibaraja.mezclar()

print("buenos días, vamos a jugar al 21, empezarmos con dos cartas")

print("tus dos primeras cartas son:")

carta_cogida = mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)
carta_cogida = mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)
mano1.mostrar_mano()

mano1.calcular_valor()

juego = True

if mano1.valor == 21:
    print("Enhorabuena, has ganado!!")
    juego = False

while juego == True:
    print("tu puntuación es de ",mano1.valor,)
    ok = input("seguimos jugando? ")
    
    if not ok == "ok":
        print("ok,bye!")
        juego = False

    if ok == "ok":
        carta_cogida = mibaraja.coger_carta()
        mano1.añadir_carta(carta_cogida)
        mano1.mostrar_mano()

        mano1.calcular_valor()

        juego = True
    
    if mano1.valor > 21:
        print("oh, no! te has pasado")
        juego = False