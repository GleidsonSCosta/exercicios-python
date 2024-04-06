num = int(input('Digite um número entre 0 e 10: '))

nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while num < 0 or num > 10:
    num = int(input('Valor inválido. Digite um número entre 0 e 10: '))

print(f'Você digitou o número {nums[num]}')

