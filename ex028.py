import random
import emoji
from time import sleep
numInt = random.randint(1, 5)
num = int(input('Escolha um número de 1 a 5: '))

print('Carregando...')
sleep(2)

if num < 1 or num > 5:
    print('Numero informado é inválido!')
elif num == numInt:
    print(emoji.emojize('Parabéms, você acertou o número escolhido. :check_mark:'))
    print('=' * 15)
    print('O número sorteado foi: {}.'.format(numInt))
    print('Você selecionou o número {}.'.format(num))
else:
    print(emoji.emojize('Não foi dessa vez.	:cross_mark:'))
    print('=' * 15)
    print('O número sorteado foi: {}.'.format(numInt))
    print('Você selecionou o número {}.'.format(num))



