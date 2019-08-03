lista = [[],[]]
for c in range(0,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares são: {lista[0]}')
print(f'Os numeros impares são: {lista[1]}')