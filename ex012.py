valor = float(input('Digite o valor da compra:R$'))
desconto = float(input('Digite a % do desconto: '))
descontoc = desconto / 100
result = valor - descontoc * valor
print('O valor com desconto de {}% é de R${:.2f}, sem o desconto seria R${:.2f}'.format(desconto,result,valor))

print('----------------------------------------------------')

#Forma adaptada com a formula do Guanabara

valor2 = float(input('Digite o valor da compra: '))
desconto2 = float(input('Digite a % do desconto: '))
result2 = valor2 - (desconto2 * valor2 / 100)
print('O valor com desconto de {}% é de R${:.2f}, sem o desconto seria R${:.2f}'.format(desconto2,result2,valor2))
