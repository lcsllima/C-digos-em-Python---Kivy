# primeum, primedois
# Visionum, visiondois
ge = {}
gc = {}
ge ['erge'] = float(input("Grau esférico → olho direito: "))
ge ['elge'] = float(input("Grau esférico → olho esquerdo: "))
gc ['ergc'] = float(input("Grau cilíndrico → olho direito: "))
gc ['elgc'] = float(input("Grau cilíndrico → olho esquerdo: "))

resultado = -0.25
ec = ee = eep= False
dc = de = dep = False

prime = -12
vision = -15
passo = -0.25
if ge ['erge'] < -15 or ge ['elge'] < -15:
    print('insira um valor entre 0 e 15 para grau esférico!')
if gc['ergc'] < -5 or gc ['elgc'] < -5:
    print('insira um valor entre 0 e 5 para grau cilíndrico!')

if -6 < gc['elgc'] < -2 or -6 < gc['ergc'] < -2 or ge['erge'] < -12.25 or ge['elge'] < -12.25:
    while True:
        if resultado == ge['erge'] <= vision:
            de = 1
        resultado += passo
        if resultado > vision:
            resultado = 0.25
            break
    while True:
        if resultado == ge['elge'] <= vision:
            ee = 1
        resultado += passo
        if resultado > vision:
            resultado = 0.25
            break
    if ee == 1 or de == 1:
        print('VOCÊ UTILIZARA LENTES VISION')

if gc['elgc'] > 0 or gc['ergc'] > 0:
    prime = 10
    while True:
        if resultado == ge['erge'] <= prime:
            dep = 1
        resultado += passo
        if resultado > prime:
            resultado = 0.25
            break

    while True:
        if resultado == ge['elge'] <= prime:
            eep = 1
        resultado += passo
        if resultado > prime:
            resultado = 0.25
            break
    if eep == 1 and dep == 1:
        print('VOCÊ UTILIZARA LENTES PRIME')
    elif eep == 1 or dep == 1 and prime <= 10:
        print('VOCÊ UTILIZARA LENTES PRIME')
