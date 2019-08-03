a = (int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')))
print(f'Lista digitada {a}')
print(f'O numero 9 foi digitado {a.count(9)} vezes')
if 3 in a:
    print(f'O numero 3 apareceu pela primeira vez na posição {a.index(3)+1}')
else:
    print('Não tem numero 3')
print('Os numeros pares são: ', end='')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')