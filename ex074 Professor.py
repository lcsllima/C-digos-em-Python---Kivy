from random import randint
a = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('A lista sorteada foi:', end=' ')
for n in a:
    print(n, end=' ')
print('\nO maior numero foi', (max(a)))
print('O menor numero foi', (min(a)))