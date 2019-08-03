lista = ('Pão', 3,'Manteiga', 2,'Quiabo', 4,'Lapis',1.50,'Cachaça',20,'Caderno',15.40)
i = 1
print('-'*50)
print('{:^50}'.format('Listagem de preços'))
print('-'*50)
for v in range(0,len(lista),2):
    print(lista[v],end='.'*(42 - (len(lista[v]))))
    print(f'R${lista[v+i]:5.2f}')
