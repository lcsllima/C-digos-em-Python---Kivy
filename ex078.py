lista = []
for i in range(0,5):
    lista.append(int(input('Digite um numero para guardar na lista: ')))
    print(f'Lista atual: {lista} <<<<')
print('\033[0;34m=-=\033[m'*30)
print(f'O numero {max(lista)} é o MAIOR! Ele esta na posição: {lista.index(max(lista))}')
print(f'O numero {min(lista)} é o MENOR! Ele esta na posição: {lista.index(min(lista))}')
print('\033[0;34m=-=\033[m'*30)

