from random import randint
import pygame
from time import sleep
d = 'S'
tentativa = 0
while d == 'S':
    valor = randint(0,10)
    print('\033[1;33m-=-\033[m' * 20)
    print('Vou pensar em um numero de 0 a 5')
    print('\033[1;33m-=-\033[m' * 20)
    resposta = int(input('Adivinhe em qual numero estou pensando: '))
    print('PROCESSANDO...')
    sleep(3)
    if resposta == valor:
        print('\033[1;34mParabéns você acertou\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('certa.mp3')
        pygame.mixer.music.play()
        print('Você venceu com {} erro(s)'.format(tentativa))
        d = input('Gostaria de jogar novamente? [S]Sim ou [N]Não?').upper()
        tentativa = 0
    else:
        print('\033[1;31mERROUUUU\033[m, o numero que pensei foi {}'.format(valor))
        pygame.mixer.init()
        pygame.mixer.music.load('errou.mp3')
        pygame.mixer.music.play()
        d = 'S'
        tentativa += 1
else:
    print('Era pra ser um laço while, mas ta ok então')
