from datetime import date

ano = date.today().year
qtdMaior = 0
qtdMenor = 0
for c in range(1, 8):
    anonasc = int(input('Informe o ano de nascimento: '))

    print('Idade = {}'.format(ano - anonasc))

    if ano - anonasc >= 18:
        qtdMaior += 1
    else:
        qtdMenor += 1


if qtdMaior > 1:
    print('Das 7 datas {} são maiores de idade.'.format(qtdMaior))
    print('E {} são menores de idade.'. format(qtdMenor))
else:
    print('Das 7 datas apenas {} é maior de idade.'.format(qtdMaior))
    print('E {} são menores de idade.'.format(qtdMenor))
