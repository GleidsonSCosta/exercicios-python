num1 = int(input('Informe um número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('informe o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O número maior é {}'.format(num1))
elif num2 > num3:
    print('O número maior é {}'.format(num2))
else:
    print('O número maior é {}'. format(num3))

if num1 < num2 and num1 < num3:
    print('O número menor é {}'.format(num1))
elif num2 < num3:
    print('O número menor é {}'.format(num2))
else:
    print('O número menor é {}'. format(num3))

