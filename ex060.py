num = int(input('Informe um número para saber seu fatorial: '))
fator = 1
cont = num

print('Calculando {}! : '.format(num), end= '')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = {}'.format(fator), end='')

    fator *= cont

    cont -= 1

print('\nFatorial de {} é igual a {}'.format(num, fator))






