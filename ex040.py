nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Média igual a {:.2f} ALUNO REPROVADO'.format(media))
elif media >= 5 and media <= 6.99:
    print('Média igual a {:.2f} ALUNO DE RECUPERAÇÃO'.format(media))
else:
    print('Média igual a {:.2f} ALUNO APROVADO. PARABÉNS!!!'.format(media))