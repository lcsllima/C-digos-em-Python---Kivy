frase = input('Digite uma frase para ver se é um palíndromo: ').replace(' ','')
com = len(frase)
inc = 0
for c in range (0,com):
    inc += 1
    pos1 = frase[-1+(inc)]
    pos2 = frase[com+1-(1+inc)]
    #print(pos1,pos2)
    if pos1 == pos2:
        continue
    else:
        print('Não é palíndromo')
        break
if inc == com:
    print('é palíndromo')


