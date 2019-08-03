status = {}
gol = []
total = 0
status['Nome'] = str(input('Digite o nome do jogador: '))
for n in range(int(input('Quantas partidas ele jogou?'))): #for n in range(int(input('Quantas partidas ele jogou?'))): funciona  #range(status['total'])
    gol.append(int(input('Quantos gols ele fez na partida?')))
    total += 1
status['gols'] = gol.copy()
status['total'] = total
print('-='*30)
print(status)
print('-='*30)
for k,v in status.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
for k, v in enumerate(status['gols']):
    print(f'   =>Na partida {k+1}, fez {v}')
print(f'\nFoi um total de {sum(status["gols"])} gols')
print('-='*30)