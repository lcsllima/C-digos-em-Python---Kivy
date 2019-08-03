print('='*10,'Loja do melbin','='*10)
preco = float(input('Digite o preço do produto: R$'))
fpag = float(input('Qual sera a forma de pagamento? Digite o numero correspondente'
                 '\n1- à vista no dinheiro (-10%)'
                 '\n2- à vista no cartão (-5%)'
                 '\n3- até 2x no cartão (normal)'
                 '\n4- 3x ou mais no cartão (+20%)'
                 '\nForma de pagamento:'))
if fpag == 1:
    pag = preco * 0.9
    print('O total a se pagar é R${:.2f} à vista no dinheiro, com 10% de desconto'.format(pag))
elif fpag == 2:
    pag = preco * 0.95
    print('O total a se pagar é R${:.2f} à vista no cartão, com 5% de desconto'.format(pag))
elif fpag == 3:
    parc = int(input('Será em 1x ou 2x no cartão de crédito?'))
    pag = preco / parc
    print('O pagamento sera feito em:'
          '\n{}x de R${}, sem juros'.format(parc,pag))
elif fpag == 4:
    parc = int(input('Gostaria de parcelar em quantas vezes?'))
    if parc >= 3:
        pag = preco * 1.2 / parc
        print('O pagamento sera feito em:\n{}x de R${:.2f}, o juros aplicado é de 20% no valor total(R${:.2f})!'.format(parc,pag,preco))
    elif parc == 1 or 2:
        pag = preco / parc
        print('O pagamento sera feito em:'
              '\n{}x de R${}, sem juros'.format(parc, pag))
else:
    print('Digite uma opção valida')
