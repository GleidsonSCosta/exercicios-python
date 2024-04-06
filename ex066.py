soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar: ) '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'Foram digitado {cont} números, e soma é igual a {soma}')