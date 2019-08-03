from time import sleep


def maior(*valores):
    v = (valores)
    if len(v) == 0:
        x = t = m = 0
    else:
        x = (v)
        t = len(x)
        m = max(x)
    print('Analisando os valores passados', end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(0.4)
    print(f'\n{x} Foram informados {t} valores ao todo.'
          f'→{m}← foi o maior valor.')
    print('-=-' * 30)
'''
Gera uma analise para o usuário que diz quantos numeros a lista possui e qual é o maior.
'''


maior(2, 3, 5, 9, 1, -3)
maior(6, 7, 2, 10, 1, 0, -7)
maior(-3, -5, -1)
maior()
