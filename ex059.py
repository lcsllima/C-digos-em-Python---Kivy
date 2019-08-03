sair = 5
valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))
op = int(input(('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Digitar novos valores\n[5]Sair\nResposta:')))
print('===='*30)
while op != sair:
    print('====' * 30)
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Digitar novos valores\n[5]Sair')
    op = int(input('Operação: '))
    print('===='*30)
    if op == 1:
        soma = valor1 + valor2
        print('Aqui esta: {} + {} = {}'.format(valor1,valor2,soma))
    elif op == 2:
        mult = valor1 * valor2
        print('{} X {} = {}'.format(valor1,valor2,mult))
    elif op == 3:
        if valor1 > valor2:
            print('{} > {}'.format(valor1,valor2))
        else:
            print('{} < {}'.format(valor1,valor2)) # poderia colocar if valor1 > valor 2: maior = valor1 else: maior = valor2
    elif op == 4:
        valor1 = int(input('Digite o valor 1: '))
        valor2 = int(input('Digite o valor 2: '))
    else:
        print('Digite uma opção valida!')
        op = 0
print('Obrigado por usar nossos serviços.')
