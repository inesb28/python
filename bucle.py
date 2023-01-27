#while
num1=4

num2 = int(input("dime un número "))

while num1 != num2:
    if num1 < num2:
        print("el número que tienes que adivinar es menor")
    else:
        print("el número que tienes que adivinar es mayor")
    num2 = int(input("dime un número "))

print("¡enhorabuena!")