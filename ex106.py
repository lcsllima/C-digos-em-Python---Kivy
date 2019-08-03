def linha(texto):
    linhas = (4 + len(texto))
    print('\033[0;32;44m-'*linhas)
    print(texto)
    print('-'*linhas)
    print('\033[m')


def fh(funcao):
    linha(f'Acessando o manual do comando {funcao}')
    print('\033[m')
    print('\033[0;30;46m')
    return help(funcao)


# Programa principal
while True:
    print('\033[m')
    a = str(input('Função ou Biblioteca >'))
    if a in ('fim', 'FIM'):
        break
    print(fh(a))
    linha('Fechando o menu')


