palavras = ('comida', 'palmeiras', 'musica', 'janeiro', 'fevereiro')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()} ', end='')

