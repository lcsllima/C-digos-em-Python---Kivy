cont = nove = 0
lista = []
pares = []
while True:
    if cont == 4:
        break
    cont +=1
    n = int(input(f'Digite o {cont}º numero: '))
    lista.append(n)
a = lista
for valor in a:
    if valor == 9:
        nove +=1
    if valor % 2 == 0:
        pares.append(valor)
print(f'A lista digitada foi {a}')
print(f'O 9 foi digitado {nove} vez(es)')
if 3 in a:
    print(f'O 3 foi digitado pela primeira vez na posição: {a.index(3)+1}')
else:
    print('Não temos o 3 na lista')
print(f'Os valores pares foram: {pares}')