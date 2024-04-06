while True:
    print('-' * 40)
    num = int(input('Quer ver a tudbuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        print('Programa encerrado. Volte Sempre')
        break
    for cont in range(1, 11):
        calc = num * cont
        print(f'{num} X {cont} = {calc}')
