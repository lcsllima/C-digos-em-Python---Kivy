import pygame
print('\033[1;35m0.Legends Never Die\n1.Thomas e Seus amigos\n2.REPROVADO\n3.TES V Skyrim Soundtrack - The Streets of Whiterun\033[m')
opcao = int(input('Qual musica você gostaria de ouvir?: '))
while opcao == 0 or opcao == 1 or opcao == 2 or opcao == 3 :
    if opcao == 0:
        print('\033[0;34mVocê esta ouvindo agora: Legends never die\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('legendsneverdie.mp3')
        pygame.mixer.music.play()
        opcao = int(input('Qual musica você gostaria de ouvir?: '))
    if opcao == 1:
        print('\033[0;34mVocê esta ouvindo agora: Thomas e seus amigos\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('TTTS.mp3')
        pygame.mixer.music.play()
        opcao = int(input('Qual musica você gostaria de ouvir?: '))
    if opcao == 2:
        print('\033[0;34mVocê esta ouvindo agora: REPROVADO\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('Reprovado.mp3')
        pygame.mixer.music.play()
        opcao = int(input('Qual musica você gostaria de ouvir?: '))
    if opcao == 3:
        print('\033[0;34mVocê esta ouvindo agora: TES V Skyrim Soundtrack - The Streets of Whiterun\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('TESV.mp3')
        pygame.mixer.music.play()
        opcao = int(input('Qual musica você gostaria de ouvir?:'))


