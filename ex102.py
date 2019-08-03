def fatorial(n, show=False):
    """
    :param n: Valor a ser fatorado n!
    :param show: True/False mostra ou não a fatoração ex: N! = n X n X n
    :return: Retorna o resultado.
    Ex de uso → print(fatorial(4, True))
    Resultado → 4 X 3 X 2 X 1 = 24
    """
    res = 1
    for fator in range(n, 0, -1):
        res *= fator
        if show is True:
            if fator == 1:
                a = '='
            else:
                a = 'X'
            print(f'{fator}', end=f' {a} ')
    return res
    #  res = res *fator


print(fatorial(4, True))
