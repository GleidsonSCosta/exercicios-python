salario = float(input('Informe o valor do seu salário: '))

if salario > 1250:
    salario = salario + (salario * 30 / 100)
    print('Seu aumentou é de 10%, seu novo salário é : R$ {:.2f}'.format(salario))
else:
    salario = salario + (salario * 15 / 100)
    print('Seu aumentou é de 15%, seu novo salário é : R$ {:.2f}'.format(salario))
