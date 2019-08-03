d = str(input('o carro esta ligado? (s/n) '))
while d == 's':
    va = float(input('Qual a velocidade do carro? '))
    vm = 80
    if va > vm:
        multa = 7
        resultado = (va - 80) * multa
        print('Você foi multado!')
        print('A multa é de R${:.2f}'.format(resultado))
        d = str(input('Gostaria de continuar? '))
    else:
        print('Parabéns, continue dirigindo assim')
        d = str(input('Gostaria de continuar? '))
else:
    print('Encerrando o programa')



