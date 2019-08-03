lista = []
while True:
    n = int(input(f'Gostaria de colocar um numero na lista?\nNumeros atuais >>{lista}<<\nDigite aqui: '))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        print('Tente novamente')
        resp = str(input('Quer continuar? [S/N]'))
lista.sort(reverse=True)
if 5 in lista:
    print(f'O numero 5 esta na lista, ele aparece pela primeira vez na posição {lista.index(5)+1}')
else:
    print("Não temos o numero 5 na lista :'( ")
print(lista)
print(f'Esta lista possui {len(lista)} numeros')