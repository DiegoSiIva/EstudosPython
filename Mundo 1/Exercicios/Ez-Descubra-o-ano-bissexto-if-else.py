
ano = int(input('Digite o ano que você nasceu: '))

bissexto = ano % 4

if bissexto == 0:
    print('Você nasceu no ano bissexto!!')
else:
    print('Você não nasceu no ano bissexto!')
