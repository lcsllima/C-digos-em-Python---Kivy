a = float(input('Digite o lado a: '))
b = float(input('Digite o lado b: '))
c = float(input('Digite o lado c: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
    '''
a = float(input('Digite o lado a: '))
b = float(input('Digite o lado b: '))
c = float(input('Digite o lado c: '))
a1 = (b - c < a < b < c)
a2 = (a - b < c < a + b)
a3 = (a - c < b < a + c)

if a1 + a2 + a3 == True :
    print('Não se pode formar um triangulo')
else:
    print('É um triangulo')'''