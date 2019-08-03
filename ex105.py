def notas(*valores, sit=False):
    med = sum(valores) / len(valores)
    profi = {'nota': valores, 'maior':max(valores), 'menor': min(valores),
             'média':med, 'situação': 'Boa' if med >= 6 else 'Ruim'}

    print(f'{profi}')


notas(6, 2, 8, 10)