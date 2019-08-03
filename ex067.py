c = 0
while True:
    print('=-='*25)
    n = int(input('Gostaria de ver a tabuada de qual valor? '))
    print('=-=' * 25)
    if n < 0:
        break
    #elif c == 10:
        #c = 0
    #while c < 10:
        #c += 1
        #print(f'{n} x {c:2} = {n*c}')

    for c in range (1,11):
        print(f'{n} x {c:2} = {c*n}')
print('Volte sempre')

# Em vez de c * n eu estava utilizando res = c*n e o res no print