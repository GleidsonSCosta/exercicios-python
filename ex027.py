nome = str(input('Digite seu nome: ')).strip().upper()

arrayDoNome = nome.split()
primeiroNome = arrayDoNome[0]
ultimoNome = arrayDoNome[len(arrayDoNome) -1]

print('Primeiro: {}'.format(primeiroNome))
print('Último: {}'.format(ultimoNome))
