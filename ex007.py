opcao = float(input("Quantas notas você quer somar? "))

if opcao == 2:
    n1 = float(input("Diga a nota 1: "))
    n2 = float(input("Diga a nota 2: "))
    result = (n1 + n2) / opcao
    print("A média de {:.2f} + {:.2f} é {:.2f}".format(n1, n2, result))

if opcao == 3:
    n1 = float(input("Diga a nota 1: "))
    n2 = float(input("Diga a nota 2: "))
    n3 = float(input("Diga a nota 3: "))
    result = (n1 + n2 + n3) / opcao
    print("A média de {:.2f} + {:.2f} + {:.2f} é {:.2f}".format(n1,n2,n3,result))
if opcao == 4:
    n1 = float(input("Diga a nota 1: "))
    n2 = float(input("Diga a nota 2: "))
    n3 = float(input("Diga a nota 3: "))
    n4 = float(input("Diga a nota 4: "))
    result = (n1 + n2 + n3 + n4) / opcao
    print("A média de {:.2f} + {:.2f} + {:.2f} + {:.2f} é {:.2f}".format(n1,n2,n3,n4,result))



