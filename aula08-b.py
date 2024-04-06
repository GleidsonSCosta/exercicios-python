# Desafio 16
# Arrendondar o número para mais e para menos.
import random
import math
from math import ceil, floor, hypot
num = float(input('Digite um número real: '))

arrMais = ceil(num)
arrMenos = floor(num)

print('Arredondando para o número {} para mais = {}'.format(num, arrMais))
print('Arredondando para o número {} para menos = {}'.format(num, arrMenos))

print('=' * 15)

# Desafio 17
# Calcular a hipontenusa de um triângulo retângulo.

catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(catA, catO)

print('O valor da Hipotenusa é igual a : {}'.format(hipotenusa))

print('=' * 15)

# Desafio 18
#Calcular seno, coseno e tangente de ângulo.

angulo = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {:.0f}° é igual a {:.2f}'.format(angulo, seno))
print('O coseno de {:.0f}° é igual a {:.2f}'.format(angulo, coseno))
print('A tangente de {:.0f}° é igual a {:.2f}'.format(angulo, tangente))

print('=' * 15)

# Desafio 19
# Sortear entre quatro nomes  de aulo e imprimir o nome sorteado.

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do teceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

alunoSorteado = random.choice(lista)

print('O aluno sorteado(a) é {}'.format(alunoSorteado))

print('=' * 15)













