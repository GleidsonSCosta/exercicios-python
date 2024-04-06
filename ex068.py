from random import randint

print('=-' * 15)
print('Vamos jogar PAR ou ÍMPAR')
print('=-' * 15)

vitorias = 0

while True:
    valor = int(input('Digite um valor de 1 até 10: '))

    while valor < 1 or valor > 10:
        valor = int(input('Valor inválido, Digite um valor de 1 até 10: '))

    opcaoJogador = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print('-' * 40)

    while opcaoJogador != 'I' and opcaoJogador != 'P':
        opcaoJogador = str(input('Opção inválida: PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
        print('-' * 40)

    maquina = randint(0, 10)

    resultado = valor + maquina

    print(f'Voce jogou {valor} e a máquina {maquina}. Total de {resultado} ', end='')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR')

    if resultado % 2 == 0 and opcaoJogador == 'P':
        vitorias += 1
        print('Você venceu!')
    elif resultado % 2 == 1 and opcaoJogador == 'I':
        vitorias += 1
        print('Você venceu!')
    else:
        print('Você Perdeu!')
        break

    print('-' * 40)
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {vitorias} vezes.')
