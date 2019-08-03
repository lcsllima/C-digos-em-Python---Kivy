from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

a = (n1, n2, n3, n4, n5)
cont2 = 0
for tamanho in range(0,len(a)):
    if cont2 == 0:
        maior = a[0]
        menor = maior
    if maior < a[tamanho]:
        maior = a[tamanho]
    if menor > a[tamanho]:
        menor = a[tamanho]
    cont2 += 1
print(f'A lista foi {a}')
print('A lista sorteada foi:',end=' ')
sorteio = sorted(a)
print('')
print('=-='*30)
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')