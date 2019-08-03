lista = []
nome = []
nota = []
aluno = 0
while True:
    nome.append(str(input('Digite o nome do aluno: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    lista.append(nome[:])
    lista[aluno].append(nota[:])
    nome.clear()
    nota.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
    aluno += 1
print('No. NOME     Média')
for numaluno, nomealuno in enumerate(lista):
    print(numaluno, end=' ')
    print(lista[numaluno][0], end='     ')
    print((sum(lista[numaluno][1]))/2)
print(lista)
while True:
    a = int(input('Quer ver a nota de qual aluno? '))
    print(f'As notas do aluno são {lista[a][1]}')
    if a == 999:
        break

