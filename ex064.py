num = int(input('Digite um número: \nPara sair digite 999 '))
qtd = 0
soma = 0

while num != 999:
    qtd += 1
    soma += num
    num = int(input('Digite um número: \nPara sair digite 999 '))

print('Foram informados {} números'.format(qtd))
if qtd >= 1:
    print('A soma deles é {}'.format(soma))
