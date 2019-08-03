tupla = ('Python','Abacate')
vogal = 'AaIiUuEeOo'
cont = 0
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aiueo':
            print(f'{letra}', end=' ')