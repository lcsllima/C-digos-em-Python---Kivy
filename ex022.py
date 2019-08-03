nome = str(input('Diga seu nome completo: '))

print(nome.upper())
print(nome.lower())
print('O nome completo tem a seguinte quantidade de letras: ',len(nome.replace(" ","")))
nom = nome.split()
print('Lucas tem a seguinte quantidade de letras: ',len(nom[0]))