termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite qual sera a razão da PA: '))
cont = 1
while cont <= 10:
    print(termo, end=' → ')
    termo += razao
    cont += 1
print(' Fim')

#print('→ Fim' if cont == 10 else '→', end=' ')