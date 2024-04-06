from random import randint
from time import sleep
from emoji import emojize

tentativas = 1
numInt = randint(1, 10)
num = int(input('Escolha um número entre 1 e 10: '))

while num < 1 or num > 10:
    num = int(input(emojize('Valor inválido! \nEscolha um número entre 1 e 10: :anger_symbol:')))
    tentativas += 1

print('Carregando...')
sleep(2)

while num != numInt:
    tentativas += 1
    num = int(input('Tente novamente. \nEscolha um número entre 1 e 10: '))

print(emojize('Parabéns você acertou o númeoro. :check_mark:'))
print('O número sorteado foi: {}.'.format(numInt))

print('Total de tentativas: {}'.format(tentativas))
