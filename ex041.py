from datetime import date

anoAtual = date.today().year
anaNasc = int(input('digite o ano de nascimento: '))

idade = anoAtual - anaNasc

print('Idade: {}'.format(idade))

if idade >= 21:
    print('Categoria: MASTER')
elif idade >= 19 or idade == 20:
    print('Categoria: SÊNIOR')
elif idade > 14 and idade <= 18:
    print('Categoria: JUNIOR')
elif idade >= 10 and idade <= 14:
    print('Categoria: INFANTIL')
else:
    print('Categoria: MIRIM')
