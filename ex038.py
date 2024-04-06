num = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num > num2:
    print('O número {} é maior que {}.'.format(num, num2))
elif num < num2:
    print('O número {} é maior que {}'.format(num2, num))
else:
    print('Os números são iguais.')
