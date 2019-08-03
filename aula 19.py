estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#  print(brasil[0])
print(brasil[0]['uf'])

'''
'''print(brasil)
print(estado1)
print(estado2)
'''
'''
pessoas = {'Nome':'Lucas','sexo': 'M','idade': 20}
#  del pessoas[sexo]
pessoas['Nome'] = 'Leandro'
pessoas['peso'] = 92.5
for k in pessoas.items():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
'''