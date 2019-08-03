from datetime import date
info = {}
data = date.today().year
info['nome'] = str(input('Digite seu nome: '))
info['ano'] = data - (int(input('Em que ano você nasceu?')))
info['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if info['CTPS'] > 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = int(input('Qual o seu primeiro salário: '))
    info['Aposentadoria'] = 35 - (data - (info['contratação'])) + info['ano']
print('-=-'*30)
print(info)
for k, v in info.items():
    print(f'  - {k} tem o valor {v}')
