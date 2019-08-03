numeros = 0
lista = []
listapar = []
listaimpar = []
while True:
    numeros += 1
    n = int(input(f'Digite o {numeros}º numero: '))
    lista.append(n)
    resp = str(input('Gostaria de continuar? [S/N]'))
    if resp in 'Nn':
        break
    while resp not in 'Ss':
        resp = str(input('Por favor, utilize apenas S,s OU N,n\nGostaria de continuar? [S/N]: '))
for atual in lista:
    if atual % 2 == 0:
        listapar.append(atual)
    elif atual % 2 == 1:
        listaimpar.append(atual)
lista.sort()
listaimpar.sort()
listapar.sort()
print(f'Lista normal >>> {lista}')
print(f'Lista par >>>> {listapar}')
print(f'Lista impar >>>> {listaimpar}')
