# Desafio 22
# Trabalhando com string

nome = str(input('Digite seu nome completo: ')).strip()

nomeUpper = nome.upper()
print('Nome Upper: ', nomeUpper)

nomeLower = nome.lower()
print('Nome Lower: ', nomeLower)

arrayDoNome = nome.split()
totalDeLetras = ''.join(arrayDoNome)

print('O total de letras sem espaço é : ', len(totalDeLetras))

print('-' * 15)

print('Total de Letras: {}'.format(len(nome) - nome.count(' ')))

print('A quantidade de letra no primeiro nome é :', len(arrayDoNome[0]))

print('-' * 15)

print('Total de letra do primeiro nome: {}'.format(nome.find(' ')))