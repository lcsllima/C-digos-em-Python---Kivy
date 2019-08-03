matriz = [[],[],[]]
somp = col3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um numero para a posição ({l},{c}): ')))
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somp += matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] == matriz[l][2]:
            col3 += matriz[l][2]
    print()
#  for l in range(0,3):
#       col3 += matriz[l][2] # poderia substituir a linha 11

print(f'A soma dos valores pares na matriz é {somp}.')
print(f'A soma dos valores da terceira coluna é {col3}.') #  sum(matriz[2]) achei que era LINHA 2
print(f'O maior valor da segunda linha é {max(matriz[1])}')