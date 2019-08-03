print("Maneira 1")
ca = float(input("Qual o valor do cateto adjascente? "))
co = float(input("Qual o valor do cateto oposto? "))
hi = (ca ** 2 + co ** 2) ** (1/2)
print("A hipotenusa é de {:.2f}".format(hi))
print("________________________________________________________________________________________")
print("Maneira 2")

from math import hypot
x = float(input("Diga o comprimento do cateto oposto: "))
y = float(input("Diga o comprimento do cateto adjascente: "))
h = hypot(x, y)
print("O valor da hipotenusa é {:.4f}".format(h))

print("Maneira 3")
print("________________________________________________________________________________________")


from math import sqrt
a = float(input("Qual é comprimento do cateto oposto? "))
b = float(input("Qual é o comprimento do cateto adjascente? "))
c1 = a**2 + b**2
c = sqrt(c1)
print("A hipotenusa é de {:.2f}".format(c))
