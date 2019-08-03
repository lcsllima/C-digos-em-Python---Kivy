def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print('Na função teste, x vale {x}')
    global a
    a = 9
    print(a)

def teste2(b=0, c=0):
    a = 7
    print(a)
#  Programa Principal

n = 2
print(f'No Programa principal, n vale {n}')
teste()
#  print(f'No programa principal, x vale {x}')
#  se você declarar a variavel no DEF, ela sera local
#  se você declarar fora da DEF, ela sera global

a = 8
print(a)
teste2()
