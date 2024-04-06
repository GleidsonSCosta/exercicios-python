from time import sleep

num = int(input('Digite um número: '))
qtd = 1
soma = num
media = 0
resp = 'S'
maior = num
menor = num

while resp == 'S':
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()

    if resp == 'N':
        print('Calculando dados...')
        sleep(2)
    else:
        num = int(input('Digite um número: '))
        soma += num
        qtd += 1

        if maior < num:
            maior = num

        if menor > num:
            menor = num

media = soma / qtd

print('=' * 10)
print('Foram digitados {} números.'.format(qtd))
print('A soma de todos os números é {}.'.format(soma))
print('A média é {}.'.format(media))
print('O maior número digitado foi {}.'.format(maior))
print(f'O menor número digitado foi {menor}.')
