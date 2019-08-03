juro = float(input('Qual é o juro? '))
meses = int(input('Quantos meses ficara no investimento? '))
juroc = (juro/100)
qv = input('Você ira investir uma vez ou regularmente? Diga U para uma vez ou R para regularmente ')

if qv == "U":
    valor = float(input('Quanto sera o valor investido no primeiro mês? '))
    (resultado) = valor
    calc1 = resultado * (1 + juroc) ** meses

    print(calc1)
if qv == "R":
    valor2 = float(input('Quanto sera o valor regular? '))
    (resultado) = valor2*meses
    calc1 = resultado*(1 + juroc) ** meses

    print(calc1)
