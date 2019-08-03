res = 0
con = 0
for pars in range(0,6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        res += n
        con += 1
if con > 1:
    print('Resultado final dos {} numeros pares somados é: {}'.format(con,res))
elif con == 1:
    print('O numero par digitado é {} '.format(res))
else:
    print('não há numero par')