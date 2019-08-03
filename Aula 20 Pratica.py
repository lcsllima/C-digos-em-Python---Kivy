def soma(a, b):
    print(f' A = {a} e B = {b}')
    c = a + b
    print(f' A + B = {c}')
    print('-' * 15)


def contador(*núm):  # * → desempacotamento
    tam = len(núm)
    print(f'recebi os valores {núm} e são ao todo {tam} números')


# Programa Principal
#  soma(4, 5)
#  soma(8, 9)
#  soma(2, 1)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
