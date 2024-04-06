soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma += c

print('A soma dos números impares divisiveis por 3 é igual a {}'.format(soma))
