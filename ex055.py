peso = 0
menor = 0
for c in range(1,6):
    pesoa = float(input('Digite o peso da {} ª pessoa: '.format(c)))
    if c == 1:
        peso = pesoa
        menor = pesoa
    else:
        if pesoa > peso:
            peso = pesoa
        if pesoa < menor:
            menor = pesoa
print('O mais pesado, pesava {} kg'.format(peso))
print('o mais leve pesava {} kg'.format(menor))
