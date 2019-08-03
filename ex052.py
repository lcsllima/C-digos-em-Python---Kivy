n = int(input('Digit o numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[0;34m', end=' ')
        cont += 1
    else:
        print('\033[0;31m', end=' ')
    print('{}'.format(c), end=' ')
if cont == 2:
    print('\n\033[mO numero foi divisível {}, então é primo'.format(cont))
else:
    print('\n\033[mO numero foi divisível {}, então não é primo'.format(cont))
