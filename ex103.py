def ficha(nome="<desconhecido>", gols=0):
    """
    :param nome: Recebe o nome do jogador
    :param gols: Gols marcados pelo jogador
    :return: Retorna a ficha
    """
    return f'O jogador {nome}, fez {gols} gols(s) no campeonato.'


n = str(input('Nome do jogador: '))
g = str(input('Gols do jogador: '))

if n.strip != '':
    if g.isnumeric():
        g = int(g)
        if n.isnumeric():
            print(ficha(gols=g))
        else:
            print(ficha(n, g))
    elif n.isnumeric():
        print(ficha())
    else:
        print(ficha())
else:
    print(ficha())
