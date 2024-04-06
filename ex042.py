reta1 = int(input('Informe o valor da primeira reta: '))
reta2 = int(input('Informe o valor da segunda reta: '))
reta3 = int(input('Informe o valor da terceira reta: '))

print('=' * 20)

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('É possível formar um trinagulo.')
    if reta1 == reta2 and reta1 == reta3:
        print('Será formado um triângulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Será formado um triângulo Isósceles.')
    else:
        print('Será formado um triângulo Escaleno.')
else:
    print('Não é possível formar triângulo.')

