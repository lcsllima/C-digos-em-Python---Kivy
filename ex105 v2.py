def notas(*valores, sit=False):
    """
    :param valores: Define notas do Aluno
    :param sit: Define se será mostrado o status atual do aluno
    :return: retorna o dicionário
    EX: print(notas(x, x, x, sit=True) → x são as notas, e sit=True mostra a 'situação'.
    """
    med = sum(valores) / len(valores)
    s = 'Boa' if med >= 6 else 'Ruim'
    profi = {}
    profi['nota'] = valores
    profi['maior'] = max(valores)
    profi['menor'] = min(valores)
    profi['média'] = med
    if sit:
        profi['situação'] = s
    return f'{profi}'


print(notas(6, 2, 8, 10, sit=True))
help(notas)