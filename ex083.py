fechou = abriu = 0
funcao = str(input('Digite a função: '))
funcao.split()
lista = funcao
for n in lista:
    if n == '(':
        abriu += 1
    elif n == ')':
        fechou += 1
    if fechou > abriu:
        print('Você fechou os parenteses antes de abrir')
        break
print(f'Abriu {abriu} e fechou {fechou}')
if abriu == fechou:
    print('Abriu e fechou corretamente os parenteses')
else:
    print('Expressão incorreta')



