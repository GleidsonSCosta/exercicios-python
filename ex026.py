frase = str(input('Digite uma frase qualquer: ')).strip().upper()

print('A letra "A" aparece {} vezes nessa frase'.format(frase.count('A')))
print('A letra a aperece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('A letra a aparece pela última vez na posição {}'.format(frase.rfind('A') + 1))