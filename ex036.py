vc = float(input('Insira o valor da casa: '))
salario = float(input('Qual é o salário mensal do comprador? '))
anos = int(input('Em quantos anos gostaria de financiar? '))

mensalidade = vc / anos / 12 #Ou vc / (anos * 12)
condição = salario * 0.30

if condição < mensalidade:
    print('\033[0;31mEsse financiamento não pode ser feito, '
          'pois a mensalidade ultrapassa 30% do salário mensal, sendo ela R${:.2f}!\033[m'.format(mensalidade))
else:
    print('\033[0;34mCada mensalidade sera de R${:.2f},'
          ' durante os {} ano(s)\033[m'.format(mensalidade,anos))