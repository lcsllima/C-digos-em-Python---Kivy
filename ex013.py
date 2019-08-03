SA = float(input('qual é o salário atual do funcionário? R$'))
aumento = float(input('qual sera o aumento em %? '))
SAA = SA + (aumento * SA / 100)
print('O salário era R${:.2f} e agora sera de R${:.2f} '.format(SA,SAA))