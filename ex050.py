soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        print('Opa, número PAR : {}'.format(num))
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
