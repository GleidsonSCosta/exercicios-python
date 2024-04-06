preco = float(input('Digite o preço do produto: '))

print('=' * 20)

aVistaOuCheque = preco - (preco * 10 / 100)

aVistaCartao = preco - (preco * 5 / 100)

parceladoEmDuas = preco

parceladoEmMais = preco + (preco * 20 / 100)

opcao = int(input('''Escolha a forma de pagamento:
Opções:
1- À Vista ou Cheque
2- À Vista no Cartão de Crédito
3- Parcelado em 2x no Cartão de Crédito
4- Parcelado em 3x ou mais no Cartão de Crédito
'''))

print('=' * 20)

if opcao < 1 or opcao > 4:
    print('Opção inválida')
elif opcao == 1:
    valorFinal = aVistaOuCheque
    print('O protudo teve um desconto de 10%, valor a ser pago: R$ {:.2f}'.format(valorFinal))
elif opcao == 2:
    valorFinal = aVistaCartao
    print('O protudo teve um desconto de 5%, valor a ser pago: R$ {:.2f}'.format(valorFinal))
elif opcao == 3:
    valorFinal = parceladoEmDuas
    print('Não tem desconto. Valor a ser pago: R$ {:.2f}'.format(valorFinal))

    valorParcela = valorFinal / 2

    print('Parceledo em 2x cada parcela será de R$ {:.2f}'.format(valorParcela))

elif opcao == 4:
    valorFinal = parceladoEmMais
    qtdParcelas = int(input('Digite a quantidade de parcelas que deseja, entre 3x e 12x '))

    if qtdParcelas < 3 or qtdParcelas > 12:
        print('Quantidade de parcelas inválida!')
    else:
        valorParcela = valorFinal / qtdParcelas

        print('Valor total a ser pago R$ {:.2f}'.format(valorFinal))
        print('Parceledo em {}x cada parcela será de R$ {:.2f}'.format(qtdParcelas, valorParcela))






