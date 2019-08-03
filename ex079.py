lvalor = []
while True:
    parar = str(input('Quer continuar?[S/N]'))
    if parar in 'Nn':
        break
    valor = int(input('Digite um novo valor para adicionar: '))
    if valor in lvalor:
        print('Valor duplicado, não vou adicionar...')
        print(lvalor)
    else:
        print('Valor novo, nova lista: ')
        lvalor.append(valor)
        print(lvalor)
lvalor.sort()
print(f'A lista final foi {lvalor}')

