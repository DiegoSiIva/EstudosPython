print('Descubra qual a sua categoria na natação de acordo com sua idade\n')

ano = int(input('Digite seu ano de nascimento: '))

idade = 2024 - ano

if idade <= 9:
    print('Você esta na categoria mirim!')
elif 10 <= idade <= 14:
    print('Você esta na categoria infantil!')
elif 15 <= idade <= 19:
    print('Voce esta na categoria junior!')
elif idade == 20:
    print('Você esta na categoria senior!')
else:
    print('Você esta na categoria master!')