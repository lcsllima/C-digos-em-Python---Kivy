cont = soma = núm = 0
núm = int(input('Digite um numero [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um numero [999 para parar]: '))

print(cont,soma)