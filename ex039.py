from datetime import date
anoNasc = int(input('Informe o ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 18:
    print('Você ainda não se alistou.')
    anosFaltantes = 18 - idade

    print('Faltam {} anos para seu alistamento.'.format(anosFaltantes))
elif idade == 18:
    print('Voce precisa se alistar esse ano.')
else:
    anosPassados = idade - 18
    print('Seu alistamento passou {} anos.'.format(anosPassados))

