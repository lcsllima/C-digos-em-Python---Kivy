salario = float(input('Qual é o salário atual? '))

if salario > 1250:
    sup = salario * 1.1
    print('O novo salario sera de: R${}'.format(sup))
else:
    sup = salario * 1.15
    print('O novo salario sera de: R${}'.format(sup))