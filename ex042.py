a = float(input('Informe o primeiro lado: '))
b = float(input('Informe o segundo lado: '))
c = float(input('Informe o terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo')
    if a == b == c:
        print('\033[0;32m-=\033[m'*81)
        print('O triângulo é equilatero!')
        print('\033[0;32m-=\033[m' * 81)
    elif a == b or a == c or c == b:
        print('\033[0;31m-=\033[m'*81)
        print('O triângulo é Isósceles')
        print('\033[0;31m-=\033[m'*81)
    else: # a != b != c
        print('\033[0;34m-=\033[m'*81)
        print('O triângulo é Escaleno')
        print('\033[0;34m-=\033[m'*81)
else:
    print('Os segmentos acima não podem formar um triângulo')