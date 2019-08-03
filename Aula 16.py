pessoa = ('Lucas', 20, 'M', 95)
print(pessoa)
'''
a = (3, 2, 1)
b = (7, 6, 5, 4)
c = b + a  # Se colocar a + b ficaria (3, 2, 1, 7, 6, 5, 4)
print(c)
print(c.count(2))  # conta quantas vezes tem o valor
print(c.index(5))  # Em que posição esta o valor, colocar >> , << depois do 5 ali, pode deslocar a buscar para uma posição
'''
'''
# () Tupla
# [] Lista
# {} Dicionario
#Tuplas são imutaveis, portando se colocar Lanche[1] = 'Refrigerante' Não vai acontecer nada
lanche = ['Hambúrguer','Suco','Pizza','Pudim']
Lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata frita')  #Hambúrguer é o elemento 0, e o Pudim o 3.
print(Lanche[-4])
print(Lanche[:2])
print(Lanche[:4])#Escrevi 4, temos apenas 4 elementos, sendo o 0,1,2,3.
# O Lanche[-4] é o hambúrguer e o -1 é o Pudim
print(Lanche[2:4])
print(Lanche[-2:])
print(Lanche[-4:])
print(lanche[1]) #é uma lista
lanche[1] = 'Refrigerante'
print(lanche[1]) #é uma lista, a lista é mútavel
print(f'=-='*40)
for comida in Lanche:
    print(f'Eu vou comer {comida}!')
print('Comi pra caramba')
print('=-='*40)
for comida in range(0,len(Lanche)): # SEMPRE COM ATENÇÂO, o LANCHE É COM L MAIUSCULO
    print(f'Eu vou comer{Lanche[comida]}! Na posição {comida}')  #O indice de Lanche é o comida, que esta contando do 0 ao tamanho do Lanche (0 ao 4)
print('Comi pra caramba')
print(f'=-='*40)
for pos,comida in enumerate(Lanche):
    print(f'Eu vou comer {comida}! Na posição {pos}, usando enumerate')

print(sorted(Lanche))
'''