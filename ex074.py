from random import randint
lista = []
cont = 0
while cont < 5:
    n = randint(1,10)
    lista.append(n)
    cont +=1
print(f'A lista gerada foi {lista}')
a = (lista)
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
print('=-='*30)
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')