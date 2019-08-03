from datetime import date
data = date.today().year
nasc = int(input('Olá, digite a data de seu nascimento: '))
idade = data - nasc

if idade < 18:
    falta = 18 - idade
    print('Falta(m) {} ano(s) para você se alistar!'.format(falta))
    print('Seu alistamento sera em {}'.format(data + falta ))
    print('Quem nasceu em {}, faz {} anos em {}'.format(nasc, idade, data))

elif idade == 18:
    print('Esta na hora de se alistar!')
    print('Quem nasceu em {}, em {}, faz {}'.format(nasc, data, idade))
else:
    print('Já se passaram {} ano(s) desde sua data inicial para o alistamento.'.format(idade - 18))
    print('Quem nasceu em {}, em {}, faz {}'.format(nasc,data,idade))