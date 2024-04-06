velocidade = int(input('Informe a velocidade em KM/h:'))

if velocidade > 80:
    print('Você foi multado!')
    valorMulta = (velocidade - 80) * 7
    print('Valor da multa : R$ {:.2f}'.format(valorMulta))
else:
    print('Velocidade OK !')