pos = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
       'Atlético', 'Athletico - PR', 'Cruzeiro', 'Botafogo','Santos','Bahia',
       'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama',
       'Sport Recife', 'América - MG', 'EC Vitória', 'Paraná')
#  print('{:^30}'.format('Olá'))
print('=-='*20)
print(f'Lista de times do brasileirão: {pos}')
print('=-='*20)
print(f'Os 5 primeiros: {pos[0:5]}')
print('=-='*20)
print(f'Os 4 ultimos: {pos[-4:20]}')
print('=-='*20)
print(f'Em ordem alfabética: {sorted(pos)}')
print('=-='*20)
escolha = str(input('Qual time você gostaria de ver? '))
for posi,time in enumerate(pos):
    if time == escolha:
        print(f'O {time} esta na {posi+1}ª posição')
#{pos.index('Chapecoense')}