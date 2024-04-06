maiorDeIdade = homens = mulherMenorDeVinte = 0

while True:
    print('-' * 25)
    print('CADASTRAR DADOS')
    print('-' * 25)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida! Sexo [M/F] ')).strip().upper()[0]

    if idade >= 18:
        maiorDeIdade += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulherMenorDeVinte += 1

    continuar = str(input('Continuar ? [S/N] ')).strip().upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida! Continuar ? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        print('======= FIM do Programa =======')
        break

print(f'Total de pessoas com mais de 18 anos: {maiorDeIdade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulherMenorDeVinte}')
