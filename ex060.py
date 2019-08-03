#faça um programa que leia um numero e dê sua fatorial, ex 5!= 5x4x3x2x1 = 120
n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c #f = f * c
    c -= 1
print('{}'.format(f))

'''
n = int(input('Digite um numero: '))
fatorial = n - 1
n1 = n
while fatorial >= 1:
    if n == n1:
        print('Calculando {}! = {}'.format(n,n),end=' ')
    print('X {}'.format(fatorial), end=' ')
    res = n1 * fatorial
    n1 = res
    fatorial -= 1
print('=',res,end=' ')

'''
'''
n = int(input('Digite um numero: '))
fator = n - 1
while fator >= 1:
    res = fator * n
    n = res
    fator -=1
print('{}'.format(res))
'''
