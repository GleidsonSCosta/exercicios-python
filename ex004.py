palavra = input('Digite algo: ')

print('O o tipo da variável é {}'.format(type(palavra)))
print('Só tem espaços? {}'.format(palavra.isspace()))
print('É númeco? {}'.format(palavra.isnumeric()))
print('É alfabetico? {}'.format(palavra.isalpha()))
print('É alfanumérico? {}'.format(palavra.isalnum()))
print('Esta em maiúsculo? {}'.format(palavra.isupper()))
print('Esta em minúsculo? {}'.format(palavra.islower()))
print('Esta capitalizada? {}'.format(palavra.istitle()))