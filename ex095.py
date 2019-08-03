jogadores = []
jogador = {}
gol = []
partidas = 0
while True:
    jogador.clear()
    gol.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for gols in range(0,partidas):
        gol.append(int(input(f'Quantos gols ele fez na {gols+1}ª partida? ')))
    jogador['gols'] = gol.copy()
    jogador['total'] = partidas
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar?'))
    if resp in 'Nn':
        break
print('od nome      gols        total')
for k, v in enumerate(jogadores):
    print(f'{k} {v}', end=' ')
    print()
while True:
    opc = int(input('Gostaria de ver qual jogador? '))
    if opc == 999:
        break
    if opc != 999:
        for chave, valor in jogadores[opc].items():
            if chave == gol:
                for key, value in jogador['gol']:
                    print(f' No jogo {key} o jogador fez {value}')

print(gol)
print(jogadores)