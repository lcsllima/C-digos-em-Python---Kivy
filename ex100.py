from random import randint


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        lista.append(randint(1,9))
        print(f'{lista[c]}', end=' ')
    print(f'PRONTO!')

def soma(lis):
    pares = []
    for c in range(0, len(lis)):
        if lis[c] % 2 == 0:
            pares.append(lis[c])
    print(f'A soma dos numeros pares da lista {lis} o resultado é {sum(pares)}')


numeros = []
sorteio(numeros)
soma(numeros)
