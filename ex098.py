from time import sleep
def linha():
    print('-=-'*12)


def contagem(i, f, c):
    '''
    atual = i
    while atual != f:
        print(atual, end=' ')
        if i < f:
            atual += c
        elif i > f:
            atual -= c
        elif c < 0:
            atual += c
    '''
    atual = 'inicio'
    while True:
        if atual == 'inicio':
            if c == 0:
                print('O contador não pode ser 0!')
                break
            atual = i
            print(f'{atual} → ', end='')
            sleep(0.2)
        if c >= 1 and i < f:
            atual += c
            if atual > f:
                break
        elif c >= 1 and i > f:
            atual -= c
            if atual < f:
                break
        else:
            atual += c
            if i > f:
                if atual < f:
                    break
            elif i < f:
                if atual > f:
                    break
        print(f'{atual} → ', end='')
        sleep(0.4)
        if atual == f:
            break
    print('FIM')


#  codigo
linha()
contagem(1, 10, 1)
linha()
contagem(10, 0, 2)
linha()
print('Agora é sua vez')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
con = int(input('Contagem: '))
linha()
contagem(ini, fim, con)
linha()