cont = nove = 0
pares = []
i = 0
n1 = int(input(f'Digite o numero: '))
n2 = int(input(f'Digite mais um numero: '))
n3 = int(input(f'Digite outro numero: '))
n4 = int(input(f'Digite mais um numero: '))
a = (n1,n2,n3,n4)
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