peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso, seu imc é: {:.2f}'.format(imc))
elif imc <=0:
    print('Reensira os dados corretamente!, seu imc é: {:.2f}'.format(imc))
elif imc < 25:
    print('Peso ideal, continue assim, seu imc é: {:.2f}'.format(imc))
elif imc <= 35:
    print('Sobrepeso, seu imc é: {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade, seu imc é: {:.2f}'.format(imc))
else:
    print('Obesidade mórbida, seu imc é: {:.2f}'.format(imc))

'''peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso, seu imc é: {:.2f}'.format(imc))
elif imc <=0:
    print('Reensira os dados corretamente!, seu imc é: {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal, continue assim, seu imc é: {:.2f}'.format(imc))
elif imc >= 25 and imc <= 35:
    print('Sobrepeso, seu imc é: {:.2f}'.format(imc))
elif imc >= 30 and imc <=40:
    print('Obesidade, seu imc é: {:.2f}'.format(imc))
else:
    print('Obesidade mórbida, seu imc é: {:.2f}'.format(imc)) '''
