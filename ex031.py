distancia = int(input('Informe a distância da viagem: '))

if distancia <= 200:
    valorViagem = distancia * 0.50
    print('A passagem custa R$ {:.2f}'.format(valorViagem))
else:
    excedeKm = distancia - 200
    print("KM excendente : {}".format(excedeKm))

    valorviagem = (200 * 0.50) + (excedeKm * 0.45)

    print('A passagem custa R$ {:.2f}'.format(valorviagem))