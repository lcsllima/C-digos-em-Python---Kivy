from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
ranking = list() # antes usamos como dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #  'jogador1' é a pos 0, e randint(1,6) é a posição 1. Logo, ele traz o valor da pos 1 como ITEM PEGO e o key pos 0
print('-=-'*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
