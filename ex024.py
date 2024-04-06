cidade = str(input('Informe o nome da sua cidade: ')).upper().strip()

arrayCidade = cidade.split()

primeiroNome = arrayCidade[0]

print('O nome da cidade começa com SANTO: {}'.format('SANTO' in primeiroNome))