viagem = float(input('Digite quantos KM possui a viagem: '))
if viagem <= 200:
   preco = viagem * 0.50
   print('Sua viagem custara R${}'.format(preco))
else:
    preco = viagem * 0.45
    print('Sua viagem custara R${}'.format(preco))