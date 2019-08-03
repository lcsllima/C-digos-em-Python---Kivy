idade = int(input('Insira a idade do participante: '))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')