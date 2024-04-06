frase = str(input('Digite uma frase. ')).strip().upper()
palavras = frase.split()

juntaPalavras = ''.join(palavras)

# Método usando fatiamento de palavras
inverso = juntaPalavras[::-1]

# Método usando o FOR

'''
inverso = ''

for c in range(len(juntaPalavras) -1, -1, -1):
    inverso += juntaPalavras[c]
'''

print('Frase digitada: {}'. format(juntaPalavras))
print('Inverso da frase:  {}'.format(inverso))

if inverso == juntaPalavras:
    print('A frase digitada é um palindromo.')
else:
    print('A frase não é um palindromo.')

