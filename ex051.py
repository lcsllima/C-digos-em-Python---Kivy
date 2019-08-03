print('=== Meu ===')
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
for pa in range(0,10):
    print('{}'.format(termo),end=' → ')
    termo += razao
print('Fim')
print('='*40)
print('=== Professor ===')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c),end=' → ')
print('Acabou')