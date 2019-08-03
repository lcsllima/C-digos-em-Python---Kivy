list = []
menor = maior = 0
for c in range(0,5):
    if len(list) >= 2:
        meio = list[1]
    if len(list) == 3:
        meio2 = list[2]
    valor = int(input('Qual variavel você quer?'))
    if c == 0:
        list.append(valor)
        meio = valor
    if min(list) > valor:
        list.insert(0,valor)
        menor = valor
        if c == 0:
            maior = meio
    elif max(list) < valor:
        list.insert(max(list),valor)
        maior = valor
        if c == 0:
            menor = meio
    if c > 1:
        if meio > valor > menor and max(list) > valor:
            list.insert(list.index(meio),valor)
        elif meio < valor > menor and max(list) > valor and valor < list[2]:
            list.insert(list.index(meio) +1,valor)
        elif meio < valor > menor and max(list) > valor and valor > list[2]:
            list.insert(list.index(meio2),valor)
print(f'Sua lista ordenada é {list}')
'''
list = []
menor = maior = 0
for c in range(0,5):
    if len(list) >= 2:
        meio = list[1]
    if len(list) == 3:
        meio2 = list[2]
    valor = int(input('Qual variavel você quer?'))
    print(valor)
    if c == 0:
        list.append(valor)
        meio = valor
    if min(list) > valor:
        list.insert(0,valor)
        menor = valor
        if c == 0:
            maior = meio
    elif max(list) < valor:
        list.insert(max(list),valor)
        maior = valor
        if c == 0:
            menor = meio
    if c > 1:
        if meio > valor > menor and max(list) > valor:
            list.insert(list.index(meio),valor)
        elif meio < valor > menor and max(list) > valor and valor < list[2]:
            list.insert(list.index(meio) +1,valor)
        elif meio < valor > menor and max(list) > valor and valor > list[2]:
            list.insert(list.index(meio2),valor)
    print(f'MENOR: {menor}')
    print(f'MAIOR: {maior}')
    print(f'MEIO: {meio}')
    print(c)
    print(list)
print(list)
'''