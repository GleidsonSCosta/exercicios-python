reta1 = int(input('Informe o valor da primeira reta: '))
reta2 = int(input('Informe o valor da segunda reta: '))
reta3 = int(input('Informe o valor da terceira reta: '))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('É possével formar um trinagulo')
else:
    print('Não é possível formar triâ2ngulo')
