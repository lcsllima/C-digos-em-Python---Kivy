aluno = {}

n = str(input('Nome: '))
aluno['nome'] = n
me = float(input(f'Média do {aluno["nome"]}: '))
aluno['media'] = me
if me >= 6:
    aluno['status'] = 'Aprovado'
else:
    aluno['status'] = 'Reprovado'
#  print(aluno)
#  print(f'O aluno {aluno["nome"]} foi {aluno["status"]} com média {aluno["media"]}')
for i, v in aluno.items():
    print(f'{i} : {v}')
