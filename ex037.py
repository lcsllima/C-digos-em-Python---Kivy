valor = int(input('Digite um numero inteiro: '))
opcao = int(input('''Em qual o valor que você gostaria de converter?
[ 1 ]Binário
[ 2 ].Octal
[ 3 ].Hexadecimal
Escolha: '''))
if opcao == 1:
    print('O numero {} em binario é {}'.format(valor,bin(valor)[2:]))
elif opcao == 2:
    print('O numero {} em octal é {}'.format(valor,oct(valor)[2:]))
elif opcao == 3:
    print('O numero {} em hexadecimal é {}'.format(valor,hex(valor)[2:]))
else:
    print('Invalido, tente novamente')