#o programa ira ler varios numeros, ao digitar 999 ele para. Preciso dizer a soma e quantos valores
valor = atual = cont = 0
#cont = 0
#valor = 0
#atual = 0
while valor != 999:
    valor = int(input('Digite um valor: '))
    if valor !=999:
        atual +=valor
        cont+=1
print('Foram somados {} numeros, e o total da soma é: {}'.format(cont,atual))
