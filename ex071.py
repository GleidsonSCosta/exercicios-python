print('=' * 30)
print('{:^30}'.format('Banco'))
print('=' * 30)

valor = int(input('Qual o valor do saque? R$ '))
nota = 50
quantidadeDeNotas = 0

while True:
    if valor >= nota:
        valor -= nota
        quantidadeDeNotas += 1
    else:
        if quantidadeDeNotas > 0:
            print(f'Total de {quantidadeDeNotas} cédulas de R${nota} ')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        quantidadeDeNotas = 0

        if valor == 0:
            break

print('=' * 30)
