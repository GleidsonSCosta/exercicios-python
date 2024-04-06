from time import sleep
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opcao = 0

while opcao != 5:
    opcao = int(input('''
O que desefa fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
'''))

    if opcao == 1:
        print('A soma do número {} mais {} é igual a {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação de {} por {} é igual a {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O número {} é maior que {}.'.format(num1, num2))
        else:
            print('O número {} é maior que {}.'.format(num2, num1))
    elif opcao == 4:
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        opcao = 0
        print('Opção inválida, digite novamente. ')
    sleep(1)

print('Fim do Programa. Até a próxima.')
















