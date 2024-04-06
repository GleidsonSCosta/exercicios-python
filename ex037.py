#Converter número
from decimal import Decimal

num = int(input('Digite um número inteiro: '))
opcao = int(input('''Escolha uma das opções:
Digite
1 para Binário
2 para Octal
3 para Hexadecinal '''))

if opcao < 1 or opcao > 3:
    print('Opção inválida!')
elif opcao == 1:
    binario = bin(num)
    print('A conversão de {} em binário é {}'.format(num, binario[2:]))
elif opcao == 2:
    octal = oct(num)
    print('A conversão de {} em octal é {}.'.format(num, octal[2:]))
elif opcao == 3:
    hexadecimal = hex(num)
    print('A conversão de {} em hexadecimal é {}'.format(num, hexadecimal[2:]))
