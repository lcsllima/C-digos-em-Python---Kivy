import random
a = str(input("Nome do aluno 1: "))
b = str(input("Nome do aluno 2: "))
c = str(input("Nome do aluno 3: "))
d = str(input("Nome do aluno 4: "))
alunos = [a, b, c, d]
random.shuffle(alunos)
print("Os alunos apresentarão na seguinte ordem\n",alunos)