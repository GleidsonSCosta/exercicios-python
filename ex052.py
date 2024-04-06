num = int(input('Digite um número: '))
primo = 0
for c in range(1, num + 1):
    if num % c == 0:
        primo += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes.'.format(num, primo))

if primo == 2:
    print('\033[mSendo assim é um número primo.')
else:
    print('\033[mSendo assim NÃO é número primo.')
