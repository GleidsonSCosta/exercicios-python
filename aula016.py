# Tuplas

# Atenção tuplas são imutáveis

lanche = ('Pizza', 'Suco', 'Biscoito', 'Pudim')

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

print(len(lanche))


for c in lanche:
    print(f'Eu vou comer {c}')


print(sorted(lanche))

