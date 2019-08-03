#Soma de todos numeros impares do 1 ao 500, sendo multiplos de 3
valor = 0
vezes = 0
for impar in range(0,500,3):
    if impar % 2 == 1: #impar % 3 == 0:
        valor +=impar
        vezes += 1
print('A soma dos {} numeros é {}'.format(vezes,valor))
