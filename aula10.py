import emoji
# idade =  int(input('Digite sua idade: '))
#
# if idade >= 18:
#     print(emoji.emojize('Pode entrar na festa! :full_moon_face:'))
# else:
#     print(emoji.emojize('Proíbido para menores de 18 anos. :crying_face:'))
#
# nome = str(input('Digite seu nome: ')).strip().upper()
# if nome == 'GLEIDSON':
#     print(emoji.emojize('Que nome lindo! :face_blowing_a_kiss:'))
# else:
#     print(emoji.emojize('Seu nome é comum. :expressionless_face:'))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(emoji.emojize('Parabéns! Você foi Aprovado. :call_me_hand:'))
else:
    print(emoji.emojize('Que pena! Tente novamente. :crying_face:'))







