sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido! \nInforme o sexo: [M/F] ')).strip().upper()
