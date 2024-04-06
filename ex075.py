numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print('\nVocê digitou os números: ', end='')

for n in numeros:
    print(f'{n} ', end='')

if 9 in numeros:
    print(f'\nO números 9 foi digitado {numeros.count(9)} vezes.')
else:
    print('\nO número 9 não foi digitado')

if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3) + 1}ª posição.')
else:
    print('O números 3 não foi digitado.')

pares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1

if pares >= 1:
    print('Os números pares são: ', end='')
    for n in numeros:
        if n % 2 == 0:
            print(f'{n} ', end='')
else:
    print('Não foram digitados números pares.')