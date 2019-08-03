'''
for c in range (1,10):
    print(c)
print('Fim')
n % 2 == 0 PAR
n % 3 == 0 Impar
n % X == Divisivel, X usa varios numeros, por exemplo um range do for, (1,10), dividiria do 1 ao 10
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} numeros pares e {} numeros impares'.format(par,impar))