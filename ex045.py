import random
import emoji
from time import sleep
elementos = ['PEDRA', 'PAPEL', 'TESOURA']

player = str(input('''Digite o nome do elemento entre:
PEDRA
PAPEL
TESOURA
''')).strip().upper()

print('=' * 20)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('=' * 20)

if player in elementos:
    cpu = random.choice(elementos)

    if player == cpu:
        print(emoji.emojize('EMPATE :cross_mark:'))
        print('CPU = {}'.format(cpu))
    elif player == 'PEDRA' and cpu == 'TESOURA':
        print('Você Ganhou!!')
        print(emoji.emojize('CPU = {} :victory_hand:'.format(cpu)))
    elif player == 'PEDRA' and cpu == 'PAPEL':
        print('DERROTA!!')
        print(emoji.emojize('CPU = {} :hand_with_fingers_splayed:'.format(cpu)))
    elif player == 'PAPEL' and cpu == 'PEDRA':
        print('Você Ganhou!!')
        print(emoji.emojize('CPU = {} :oncoming_fist:'.format(cpu)))
    elif player == 'PAPEL' and cpu == 'TESOURA':
        print('DERROTA!!')
        print(emoji.emojize('CPU = {} :victory_hand:'.format(cpu)))
    elif player == 'TESOURA' and cpu == 'PAPEL':
        print('Você Ganhou!!')
        print(emoji.emojize('CPU = {} :hand_with_fingers_splayed:'.format(cpu)))
    elif player == 'TESOURA' and cpu == 'PEDRA':
        print('DERROTA!!')
        print(emoji.emojize('CPU = {} :oncoming_fist:'.format(cpu)))
else:
    print('Elemento inválido!!!')






