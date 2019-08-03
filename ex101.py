#  16 - 18 e 65+ é opcional
#  Código adaptado, no inicio havia declarado a variavel ANO como global
# os RETURNS estavam como print, e a função voto() na linha 19, não tinha o V dentro obviamente.


def voto(ano):
    from datetime import date
    idade = int(date.today().year) - ano
    if idade < 16:
        return f'idade {idade}: VOTO NEGADO!'
    elif idade in (16,17) or idade > 65:
        return f'idade {idade}: VOTO OPCIONAL!'
    elif 65 > idade > 18:
        return f'idade {idade}: VOTO OBRIGATÓRIO!'


while True:
    v = int(input('Digite seu ano de nascimento: '))
    print(voto(v))
    c = input('Quer continuar?[S/N]')
    if c in 'Nn':
        break
