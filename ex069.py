pessoa = idq = miq = hq = 0
lista = ['Inicio']
while True:
    print('=-='*20)
    pessoa += 1
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {pessoa}ª pessoa [M/F]: ')).upper()
    while sexo not in 'MmFf':
        sexo = str(input(f'Digite novamente o sexo da {pessoa}ª pessoa, \033[1;031mutilize M/m ou F/f como resposta\033[m: ')).upper()
    print('=-=' * 20)
    if idade >= 18:
        idq +=1
    elif sexo == 'M':
        hq +=1
    if sexo == 'F' and idade < 20:
        miq += 1
    c = ' '
    while c not in 'SN':
        c = input('Gostaria de continuar? [S/N] ').upper()
    if c == 'N':
        break
print('=-=' * 20)
print(f'O total de pessoas com 18 anos ou mais é {idq}\nTemos {hq} pessoas do sexo masculino cadastrados'
      f'\nE {miq} mulhere(s) com menos de 20 anos')
