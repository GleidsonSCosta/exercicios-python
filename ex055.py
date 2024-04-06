menorPeso = 0
maiorPeso = 0
for c in range(1, 6):
    peso = float(input('Digite o peso: '))

    if menorPeso == 0:
        menorPeso = peso

    if menorPeso > peso:
        menorPeso = peso

    if maiorPeso < peso:
        maiorPeso = peso

print('Menor peso informado {} Kg'.format(menorPeso))
print('Maior peso informado {} Kg'.format(maiorPeso))
