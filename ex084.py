lista = []
pessoa = []
cont = 0
mpesado = []
menpesado = []
media = 0
while True:
    cont += 1
    pessoa.append(str(input(f'Digite um nome da {cont}ª pessoa: ')))
    pessoa.append(int(input(f'Digite o peso da {cont}ª pessoa: ')))
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
for peso in lista:
    media += peso[1]
media = media / len(lista)
for c in lista:
    if c[1] > media + 10:
        mpesado.append(c[0])
    elif c[1] < media - 10:
        menpesado.append(c[0])
print(f'O peso médio utilizado foi {media}')
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Os mais pesados são {mpesado}')
print(f'Os mais leves são {menpesado}')
