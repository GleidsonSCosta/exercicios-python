nome = str(input('Digite seu nome: ')).strip().upper()

if nome == 'GLEIDSON':
    print('Que nome bacana!')
elif nome in 'ANA MARIA JULIA':
    print('''Que nome bonito!
Tenha um bom dia !!''')
else:
    print('Bom dia {}'.format(nome))
