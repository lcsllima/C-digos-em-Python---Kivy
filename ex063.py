'''
anterior = 1
atual = 1
final = 2
while final < 2584:
    final = atual + anterior
    anterior = atual
    atual = final
    print(final)
cont = int(input('Quantos termos você quer mostrar?'))
anterior = 1
atual = 1
final = 2
print('0 → 1 → 1 → '.format(anterior),end=' ')
cont1 = 3
while cont1 < cont:
    final = atual + anterior
    anterior = atual
    atual = final
    print('{} →'.format(final), end=' ')
    cont1 += 1
print('Fim')
'''
atual = 1
anterior = 0
cont = int(input('Digite quantos termos você quer: '))
cont1 = 3
print('{} → {} '.format(anterior,atual),end='→ ')
while cont1 <= cont:
    print('{} '.format(atual), end='→ ')
    anterior = atual - anterior
    atual += anterior
    cont1 +=1
print('Fim')