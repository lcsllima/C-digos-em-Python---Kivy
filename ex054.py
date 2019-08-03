from datetime import date
d = date.today().year
print(d)
q = 0
for c in range(1,8):
    data = int(input('Digite a data de nascimento da {}ª pessoa: '.format(c)))
    idade = d - data
    if idade >= 21:
        q +=1
    else:
        continue
n = 7 - q
print('{} não atingiram a maioridade, e {} atingiram.'.format(n,q))

