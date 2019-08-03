from math import cos,sin,tan,radians
ang = float(input("Diga o angulo: "))
c = cos(radians(ang))
s = sin(radians(ang))
t = tan(radians(ang))

print("o cosseno é {:.2f} \no seno é {:.2f} \na tangente é {:.2f}" .format(c,s,t))


