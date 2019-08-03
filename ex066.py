cont = soma = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Total de numeros digitados: {cont}\nE a soma dos valores: {soma}')
