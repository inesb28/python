import math

a = 3
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)

a = int(input("dime un número: "))
b = int(input("dime otro: "))
print("suma: ")
print(a+b)
print("resta: ")
print(a-b)
print("multiplicación: ")
print(a*b)
print("potencia: ")
print(a**b)
print("división: ")
print(a/b)

a = int(input("x^2: "))
b = int(input("x: "))
c = int(input("1: "))

print((-b+math.sqrt(b**(2)-4*a*c))/(2*a))
print((-b-math.sqrt(b**(2)-4*a*c))/(2*a))