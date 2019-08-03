valor = int(input('Digite o valor que gostaria de sacar: '))
atual = valor
ced = 50
qced = 0

while True:
    if atual >= ced:
        atual -= ced
        qced += 1
    else:
        if qced > 0:
            print(f'{qced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qced = 0
        if atual == 0:
            break
