times = ('Palmeiras', 'Santos', 'São Paulo', 'Bragantino',
         'Ponte Preta', 'Vasco', 'Flamengo', 'Fluminense',
         'Corinthians', 'Champecoense', 'Mirassol', 'Botafogo')

print(f'Os quatro primeiros: {times[0:4]}')
print(f'Os três últimos: {times[-3:]}')
print(f'Ordem Alfabetica -> {sorted(times)}')

for t in range(0, len(times)):
    if times[t] == 'Champecoense':
        print(f'Colocação da Chapecoense: {t + 1}°')


print(f'O Vasco esta na {times.index('Vasco') + 1}ª colocação.')

# for t in times:
#     if t == 'Champecoense':
#         print(f'Colocação da Chapecoense: {t}')

for pos, t in enumerate(times):
    print(f'{pos + 1}º {t}')
