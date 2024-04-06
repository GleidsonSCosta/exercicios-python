produtos = ('Banana', 10.5, 'Maçã', 7.25, 'Pera', 9.0, 'Limão', 3.5)

print('-' * 40)
print('{:^40}' .format('Lista de Preços'))
print('-' * 40)

for prod in range(0, len(produtos)):
    if prod % 2 == 0:
        print(f'{produtos[prod]:.<30} R$ {produtos[prod + 1]:.2f}')
