valor = int(input('Digite quanto gostaria de sacar: '))
c50 = c20 = c10 = c1 = 0
resto = valor
while True:
    if resto >= 50:
        c50 +=1
        resto -=50
    elif 50 > resto > 20:
        resto -= 20
        c20 +=1
    elif 20 > resto > 10:
        resto -=10
        c10 +=1
    elif resto < 10:
        c1 = resto
        resto -= c1
    if resto == 0:
        break
print(f'Cedulas de 50: {c50}\nCedulas de 20: {c20}\nCedulas de 10: {c10}\nCedulas de 1: {c1}\n')
