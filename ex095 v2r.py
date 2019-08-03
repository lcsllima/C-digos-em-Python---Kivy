jogadores = []
status = dict()
gol = []
total = anterior = opc = 0
while True:
    status.clear()
    gol.clear()
    status['Nome'] = str(input('Digite o nome do jogador: '))
    for c in range(0,int(input('Quantos jogos ele fez? '))):
        gol.append(int(input(f'Quantos gols ele fez no {c+1}º jogo?')))
        total += 1
    status['gols'] = gol.copy()
    status['total'] = total
    jogadores.append(status.copy())
    resp = str(input('Gostaria de continuar? '))
    print('-=' * 30)
    if resp in 'Nn':
        break
print('od nome      gols        total')
for k, v in enumerate(jogadores):
    if k == 0:
        anterior = k
    if k > anterior:
        print()
    print(f'{k}', end=' ')
    for keys, valores in v.items():
        print(f'{valores}', end='   ')
print()
while True:
    opc = 0
    opc = int(input('Qual jogador você gostaria de ver? (998 para  parar) '))
    print('-=' * 30)
    if opc == 998:
        break
    for k, v in jogadores[opc].items():
        if k == 'Nome':
            print(f'LEVANTAMENTO DO JOGADOR {v}')
            print('-=' * 30)
        if k == 'gols':
            for k, c in enumerate(v):
                print(f'    => No jogo {k+1} ele fez {c} gols')
print('Obrigado por usar nosso software')
