num = int(input('Digite um numero para fazer a tabuada dele: '))
for tab in range(1,11):
    res = tab * num
    print('{} x {} = {}'.format(tab,num,res))

