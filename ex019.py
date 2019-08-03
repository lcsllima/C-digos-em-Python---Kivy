import random
a = str(input("Diga o nome do 1º aluno: "))
b = str(input("Diga o nome do 2º aluno: "))
c = str(input("Diga o nome do 3º aluno: "))
d = str(input("Diga o nome do 4º aluno: "))
alunos = [a, b, c, d]
sorteio = random.choice(alunos)
print("O aluno sorteado é {}".format(sorteio))
'''
import random
a = input("Diga o nome do 1º aluno: ")
b = input("Diga o nome do 2º aluno: ")
c = input("Diga o nome do 3º aluno: ")
d = input("Diga o nome do 4º aluno: ")
r = random.randint(1,4)

if r == 1:
    print(a)
if r == 2:
    print(b)
if r == 3:
    print(c)
if r == 4:
    print(d)
    '''


