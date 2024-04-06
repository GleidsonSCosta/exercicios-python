# Caluculo de IMC

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

print('=' * 25)

imc = peso / (altura * altura)

print('IMC = {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobre peso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
