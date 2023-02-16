from baraja import Baraja
from mano import Mano

mibaraja = Baraja()
mano1 = Mano()
mibaraja.mezclar()

input("buenos días, vamos a jugar al 21")

carta_cogida = mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)
carta_cogida = mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)
mano1.mostrar_mano()

mano1.calcular_valor()
print(mano1.valor)