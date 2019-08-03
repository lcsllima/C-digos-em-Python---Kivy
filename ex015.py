dias = float(input('Quantos dias usou o carro? '))
km = float(input('Quantos Km foram utilizados? '))
diap = 60
kmp = 0.15
preço = (dias * diap) + (km * kmp)
print('Preço a pagar R${:.2f}'.format(preço))
