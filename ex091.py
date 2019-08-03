from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for c in range(1,5):
    jogadores['jogador'+str(c)] = randint(1,6)
for k, v in jogadores.items():
    print(f'O {k} jogou {v}')
    sleep(0.7)
joglist = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(joglist):
    print(f'O {v[0]} ficou em {i+1}º com {v[1]} pontos')
    sleep(0.7)
print(jogadores)
print(joglist)
