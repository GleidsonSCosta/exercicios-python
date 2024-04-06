totalIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
qtdMulherMenor = 0
qtdHomem = 0
qtdMulher = 0
sexo = ''

for pessoa in range(1, 5):
    print('------- {}ª Pessoa -------'.format(pessoa))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Valor inválido! Digite novamente: \nSexo: [M/F] maria')).strip().upper()

    if sexo == 'M':
        qtdHomem += 1
        if idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeHomemMaisVelho = nome
    else:
        qtdMulher += 1
        if idade < 20:
            qtdMulherMenor += 1

    totalIdade += idade

mediaIdade = totalIdade / 4

if qtdHomem == 0:
    print('A média de idade é igual a {}'.format(mediaIdade))
    print('Não foram informados dados de homens.')
    print('A quantidade de mulheres menor de 20 anos é de {}.'.format(qtdMulherMenor))
elif qtdMulher == 0:
    print('A média de idade é igual a {}'.format(mediaIdade))
    print('O homem mais velho é {} e sua idade é de {} anos.'.format(nomeHomemMaisVelho, maiorIdadeHomem))
    print('Não foi informados dados de mulheres.')
else:
    print('A média de idade é igual a {}'.format(mediaIdade))
    print('O homem mais velho é {} e sua idade é de {} anos.'.format(nomeHomemMaisVelho, maiorIdadeHomem))
    print('A quantidade de mulheres menor de 20 anos é de {}.'.format(qtdMulherMenor))
