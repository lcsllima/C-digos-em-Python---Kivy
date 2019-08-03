import random
from time import sleep
nome = input('Insira seu nome: ')
lista = ['pedra','papel','tesoura']
pj = 0
pc = 0
while pj < 3 and pc < 3:
    computador = random.choice(lista)
    jogador = (input('Pedra, papel ou tesoura?')).lower()
    print('='*20)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('=' * 20)
    print('{}: {} x PC: {}'.format(nome, jogador, computador))
    if computador == 'pedra' and jogador == 'tesoura':
        pc += 1
        print('PC VENCEU {} {} x PC {}'.format(nome,pj,pc))
        print('='*20)
    elif computador == 'tesoura' and jogador == 'papel':
        pc += 1
        print('PC VENCEU {} {} x PC {}'.format(nome,pj,pc))

    elif computador == 'papel' and jogador == 'pedra':
        pc += 1
        print('PC VENCEU {} {} x PC {}'.format(nome,pj,pc))

    elif computador == jogador or jogador == computador:
        print('Empate')
    else:
        pj += 1
        print('{} VENCEU J {} x PC {}'.format(nome,pj,pc))
if pc == 3:
    print('PC venceu o jogo')

else:
    print('{} venceu o jogo'.format(nome))