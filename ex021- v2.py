import pygame


def play(opcao):
    pygame.mixer.init()
    pygame.mixer.music.load(lista[opcao])
    pygame.mixer.music.play()


musicas = (0,1,2,3)
lista = ['legendsneverdie.mp3','TTTS.mp3','Reprovado.mp3','TESV.mp3']
print('\033[1;35m0.Legends Never Die\n1.Thomas e Seus amigos\n2.REPROVADO\n3.TES V Skyrim Soundtrack - The Streets of Whiterun\033[m')
while True:
    opcao = int(input('Qual musica você gostaria de ouvir?: '))
    if opcao in musicas:
        print(f'\033[0;34mVocê esta ouvindo agora: {lista[opcao]}\033[m')
        play(opcao)
    else:
        print('Você precisa escolher uma musica da lista')
