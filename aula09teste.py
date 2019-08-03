frase = 'Curso em vídeo python'
print(len(frase))
print(frase[::2])
''' O resultado é zero pois não há a letra O maiuscula'''
print(frase.count("O"))
''' O resultado é 3 pois com o upper há a letra O maiuscula'''
print(frase.upper().count("O"))
''' O resultado é zero pois não há a letra O minuscula ao aplicar o upper'''
print(frase.upper().count("o"))

print('''OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo''')

print(frase.replace('Curso', 'Banana'))

'''frase.replace('Curso', 'Banana') não salva a variavel FRASE, para isso precisa se escrever da seguinte forma
frase = frase.replace('Curso','Banana') '''

dividido = frase.split()
print(dividido[2][1])