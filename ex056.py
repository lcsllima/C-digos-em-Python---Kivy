nshow = ''
media = 0
id = 0
menos20 = 0
p = int(input('Quantidade de pessoas: '))
for c in range(1,p+1):
    print('==='*20)
    print('{}ª Pessoa'.format(c))
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo:\n[M].Masculino\n[F]Feminino ').lower()
    print('===' * 20)
    media += idade
    if sexo == 'f' and idade < 21:
        menos20 +=1
    if sexo == 'm' and idade > id:
        id = idade
        nshow = nome
        ns = True
    else:
        continue
mediaf = media / p
if ns == True:
    print('O homem mais velho se chama {}'.format(nshow))
print('A media da idade do grupo é {:.2f}\n{} mulheres tem menos de 21 anos'.format(mediaf,menos20))

