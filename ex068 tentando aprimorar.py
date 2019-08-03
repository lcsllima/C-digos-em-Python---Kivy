from random import randint
acerto = 0
while True:
    esc = str(input('Escolha [I/P]')).upper()
    j = int(input('Escolha o numero: '))
    pc = randint(0,10)
    res = (j + pc) % 2
    if res == 1:
        pori = 'IMPAR'
    elif res == 0:
        pori = 'PAR'
    if esc == 'P' and pori == 'IMPAR' or esc == 'I' and pori =='PAR':
        print('VOCÊ PERDEU')
        print(f'Jogador escolheu {j} e o pc {pc}, portanto {j + pc} é {pori}')
        break
    else:
        print(f'Jogador escolheu {j} e o pc {pc}, portanto {j+pc} é {pori}')
        acerto +=1
print(f'O total de acertos foi {acerto}')