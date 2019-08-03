a = str(input('Gostaria de verificar? (sim/não) ')).strip().lower()
while a == 'sim':
    n = int(input('Diga um numero, iremos verificar se é par ou impar '))
    nr = (n % 2)
    if nr == True:
        print('O numero é impar')
        a = str(input('Gostaria de verificar novamente? (sim/não) ')).strip().lower()
    if nr == False:
        print('O numero é par')
        a = str(input('Gostaria de verificar novamente? (sim/não) ')).strip().lower()
else:
    print('Tenha um bom dia')