# Emprétimo bancario
from math import ceil

valorCasa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe seu salário: '))
anos = int(input('Informe em quantos parceles pretende financiar: '))

qtdParcelas = anos * 12
print('=' * 20)

valorParcela = valorCasa / qtdParcelas

limite = salario * (30 / 100)

if valorParcela > limite:
    print('NEGADO!! O valor da parcela excede o máximo de 30% do salário.')
    print('Sua parcela mensal pode ser até R$ {:.2f}.'.format(limite))

    print('=' * 20)
    print('Oferta do Banco')

    qtdParcelaProposta = ceil(valorCasa / limite)
    parcelaProposta = valorCasa / qtdParcelaProposta
    print('Proposta : {} x de R$ {:.2f}'.format(qtdParcelaProposta, parcelaProposta))
elif valorParcela <= limite:
    print('APROVADO!! Valor da Parcela R${:.2f}'.format(valorParcela))



