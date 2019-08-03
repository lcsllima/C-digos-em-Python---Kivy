galera = list()
dado = list()
totmen = totmai = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # se não colocar [:], ele associa e na linha 7 apaga as duas
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45 ]]
#  print(galera[3][1]) # [3] é a posição da GALERA, [1] ali é idade dentro de cada pessoa
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''
'''
teste = list()
teste.append('Lucas')
teste.append(20)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
'''
'''
#  Aprender dicionarios (dictionary)
https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
pessoas = []
d1 = ['João', 21]
d2 = ['Pedro', 35]
d3 = ['Ana', 40]
d4 = ['Carla', 23]
print(pessoas)
pessoas.append(d1)
print(pessoas)
pessoas.append(d2)
print(pessoas)
pessoas.append(d3)
print(pessoas)
pessoas.append(d4)
print(pessoas)
'''