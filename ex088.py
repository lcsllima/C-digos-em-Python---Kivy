from random import randint
from time import sleep
lista = []
v = 6
jogo = 0
jogos = int(input('Quantos jogos você quer? '))
print(('-='*3),f'Sorteando {jogos}',('=-'*3))
while jogos > 0:
    jogo += 1
    while len(lista) < v:
        num = randint(1, 99)
        if num not in lista:
            lista.append(num)
    sleep(0.9)
    lista.sort()
    print(f'Jogos {jogo}:{lista}')
    lista.clear()
    jogos -= 1
