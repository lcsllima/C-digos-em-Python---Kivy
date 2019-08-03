'''sexo = False
sexouser = input('Digite seu sexo\n[M] Masculino\n[F]Feminino\nResposta: ').strip().upper()
erro = 0
while sexo == False:
    if erro >=1:
        sexouser = input('\033[1;31mDigite seu sexo, mas dessa vez utilize M ou F\033[m\n[M] Masculino\n[F]Feminino: ').strip().upper()
    if sexouser == 'M':
        sexo = True
        print('Você é Homem')
    elif sexouser == 'F':
        sexo = True
        print('Você é Mulher')
    erro += 1
'''
sexo = str(input('Digite seu sexo: [M/F]')).upper().strip()
while sexo not in 'FfMm':
    sexo = str(input('Erro. Digite seu novamente seu sexo: [M/F]')).upper().strip()
print('Dado cadastrado como {}'.format(sexo))
