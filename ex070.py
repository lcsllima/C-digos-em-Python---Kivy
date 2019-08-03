tot = cont = var = 0

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    var += 1
#   if tot == 0:
    if var == 1 or preco < menorv:
        menorv = preco
        menor = produto
#    else:
#        if preco < menorv:
#            menorv = preco
#            menor = produto
    tot += preco
    if preco > 1000:
        cont += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Quer continuar? [S/N] '))
    if c in 'Nn':
        break
print(f'O mais barato foi: {menor} | custando: R${menorv:.2f}'
      f'\nO total gasto foi R${tot:.2f} e {cont} produtos custaram mais de R$1000')
