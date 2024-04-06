frase = '        Palmeiras Campeão Brasileiro 2023          '
print(frase)

print(frase[10:17])
print(frase[:9])

arrayDaFrase = frase.split()
time = arrayDaFrase[0]
print(time)

fraseSemEspaco = frase.strip()
print(fraseSemEspaco)
print(len(fraseSemEspaco))

print(frase.replace('2023', '2024'))

print('Palmeiras' in frase)

print(frase.find('Campeão'))

fraseUpper = frase.upper().replace('2023', '2024')
print(fraseUpper.strip())


