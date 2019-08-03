termo = int(input('Digite qual sera o termo da PA: '))
razao = int(input('Digite qual sera a razão: '))
cont = 0
v = 1
max = 11
resp = 1
while resp > 0:
    while cont <= max and v > 0:
        print('{} →'.format(termo),end=' ')
        #print('Pausa' if cont == (max - 2) else '→', end=' ')
        termo += razao
        cont += 1
        if cont == max -1:
            resp = int(input('Pausa\nDigite mais quantos termos gostaria de ver. Caso não queira, digite 0: '))
            if resp > 0:
                cont == 0
                max += resp
            else:
                break
print('Fim')
