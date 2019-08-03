import pygame
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
nf = (n1 + n2)/2
if nf < 5:
    print('\033[0;31mReprovado! Sua nota foi {}\033[m'.format(nf))
    pygame.mixer.init()
    pygame.mixer.music.load('Reprovado.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
elif nf >= 5 and nf <= 6.9: # 7 > média >= 5 também funciona no python
    print('Você esta de recuperação! Estude para a prova.\nSua nota foi {}'.format(nf))
elif nf == 7.0:
    print('Olha, passou raspando em\nTUTS TUTS QUERO VER!')
    pygame.mixer.init()
    pygame.mixer.music.load('tutstuts.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('Parabéns, você foi aprovado sua nota é',nf)