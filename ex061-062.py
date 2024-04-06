primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
qtdTermos = int(input('digite a quantidade de termos: '))
mostrarMais = 'S'
cont = 0
while mostrarMais == 'S':
    while cont != qtdTermos:
        cont += 1
        print('{}'.format(primeiro), end=' ')
        primeiro += razao

    mostrarMais = str(input('\nDeseja ver mais termos? [S/N] ')).strip().upper()
    cont = 0
    while mostrarMais != 'S' and mostrarMais != 'N':
        mostrarMais = str(input('Opção inválida! \nDeseja ver mais termos? [S/N] ')).strip().upper()

    if mostrarMais == 'S':
        qtdNovosTermos = int(input('Quantos novos termos deseja ver? '))

        while cont != qtdNovosTermos:
            cont += 1
            print('{}'.format(primeiro), end=' ')
            primeiro += razao
    else:
        print('-------- Saindo... --------')
print('Fim do programa.')


