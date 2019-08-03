print('\033[1;033mOlá, digite dois valores para descobrir qual é o maior!\033[m')
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

if v1 > v2:
    print('\033[0;34mO 1º Valor é maior\033[m')
elif v1 < v2:
    print('\033[0;34mO 2º Valor é maior\033[m')
else:
    print('Não existe valor maior, Ambos são iguais.')
