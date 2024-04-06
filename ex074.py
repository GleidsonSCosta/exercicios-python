from random import randint

num = (randint(0, 10), randint(0, 10),randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Números sorteados: ', end='')
for n in num:
    print(f'{n} ', end='')

print(f'\nO menor valor é : {min(num)}')
print(f'O maior valor é : {max(num)}')