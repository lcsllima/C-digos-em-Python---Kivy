# Leia int, tem que funcionar igual o input, mas só com 1 numero.
def leiaInt(frase):
    while True:
        valor = input(f'{frase}')
        if valor.isnumeric():
            return valor
            break
        else:
            print('\033[1;31mERRO, DIGITE UM NUMERO INTEIRO\033[m')


a = leiaInt('Digite o numero: ')
print(f'O numero digitado foi {a}')
