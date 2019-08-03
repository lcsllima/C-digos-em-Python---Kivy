from operator import itemgetter
cadastros = []
pessoa = {}
mulheres = []
pacima = []
media = 0
while True:
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    while True:
        pessoa['sexo'] = str(input('Digite o seu sexo [M/F]'))
        if pessoa['sexo'] in'MmFf':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = str(input('Digite sua idade: '))
    cadastros.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Foram cadastradas {len(cadastros)} pessoas')
for k, v in enumerate(cadastros):
    # print(f'{k} tem {v}')
    for key, valor in v.items():
        if key == 'sexo':
            if valor in 'Ff':
                mulheres.append(v['nome'])
        if key == 'idade':  #print(f'a {key} tem o valor: {valor}')
            media += int(valor)
            if int(valor) > int(media):
                pacima.append(v['nome'])
media = int(media/len(cadastros))
for k, v in enumerate(cadastros):
    for key, valor in  v.items():
        if key == "idade":
            if int(valor) > int(media):
                pacima.append(v['nome'])
print(f'A media das idades cadastradas é: {media}')
print(f'Em nosso cadastro possuimos {len(mulheres)} mulheres, que são: {mulheres}')
print(f'As pessoas acima da média são {pacima}')
print(cadastros)

