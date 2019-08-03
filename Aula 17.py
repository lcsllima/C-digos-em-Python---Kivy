a = [1,2,3,4]
b = a #  para copiar devemos fazer o seguinte >>>> b = a[:], pois assim COPIAMOS todos os valores de A para B.
b[1] = 9874
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#  a lista A mudou, mesmo tendo alterado apenas a lista B, portanto, associar uma lista com a outra, liga as duas para qualquer alteração.
'''
valores = []
valores.append(4)
valores.append(5)
valores.append(8)
print(valores)
for posição,valo in enumerate(valores):
    print(f'Na posição {posição} encontrei o valor {valo}!')
print('Cheguei ao final da lista')
'''
'''
num = [2,5,9,1]
num[2] = 3
num.append(7)
a = int(input(f'Digite um valor para inserir na lista {num}:'))
b = int(input('Agora digite a posição: '))
num.insert(b, a)
print(num)
if 95 in num:
    num.remove(95)
else:
    print('Não existe numero 95 na lista.')
print(num)
# num.remove(4)
#  num.sort()
print(num)
print(f'Esta lista tem {len(num)} elementos')
'''