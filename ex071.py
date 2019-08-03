valor = int(input('Quanto você gostaria de sacar? '))


c50 = valor // 50
resto = valor - c50 * 50

c20 = resto // 20
resto = resto - c20 * 20

c10 = resto // 10
resto = resto - c10 * 10

c1 = resto
resto = resto - c1

print(f'Cedulas de 50: {c50}\nCedulas de 20: {c20}\nCedulas de 10: {c10}\nCedulas de 1: {c1}\n')