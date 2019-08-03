menor = maior = media = c = 0
opcao = 'S'
lopcao = ['S','N']
while opcao == 'S':
    n = int(input('Digite um numero: '))
    c +=1
    if c == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    media += n
    opcao = str(input('Gostaria de continuar? [S/N]')).upper().strip()
    while opcao not in lopcao:
        opcao = str(input('Digite novamente se gostaria de continuar com S ou N:')).upper().strip()
    if opcao == 'N':
        break

media = media / c
print('A media dos {} numeros é {}'.format(c,media))
print('O {} é o maior numero e o menor é {}'.format(maior,menor))