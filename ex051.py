primeiro = int(input('Digite o primeiro termo da prograssão: '))
razao = int(input('Digite a razão da progressão: '))

decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ')
