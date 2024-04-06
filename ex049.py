num = int(input('Digite um número para calcularmos a tabuada. '))

for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num * c))
