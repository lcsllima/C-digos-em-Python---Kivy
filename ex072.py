numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero: '))
    if num in range(0,20):
        print(f'Você digitou o numero {numeros[num]}')
        break
    print('Tente novamente. ', end='')
#   else:
#       num = int(input('Digite um numero, mas que seja entre 0 e 20: '))
