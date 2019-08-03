print('\033[7;33;44mOlá mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
nome = 'Lucas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'],nome,cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))






'''\033[0;33;44m
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''