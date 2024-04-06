# Desafio 20
# Sortear uma ordem entre quatro opções com nome de alunos

from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('Sequência sorteada:')
print(alunos)