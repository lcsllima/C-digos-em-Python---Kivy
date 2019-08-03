def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
soma(2, 3, 6)
soma(1, 2, 5, 1)
'''
numeros = (2,3,4)
resultado = 0
for numero in numeros:
    print(numero)
print(resultado)
'''