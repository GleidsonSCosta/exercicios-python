total = maisDeMil = 0
precoMaisBarato = 0
contador = 0
produtoMaisBarato = ''

print('-' * 25)
print('Loja de Informática')
print('-' * 25)

while True:

    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: '))
    contador += 1

    if preco >= 1000.00:
        maisDeMil += 1

    total += preco

    if contador == 1 or preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = produto

    continuar = str(input('Continuar? [S/N]')).strip().upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida! Deseja continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maisDeMil} produtos custando R$1000.00 ou mais.')
print(f'O produto mais barato foi {produtoMaisBarato} custando R${precoMaisBarato:.2f}')