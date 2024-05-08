nome = str(input('Qual seu nome?: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem pupolar no brasil')
else:
    print('Seu nome é bem normal {}!'.format(nome))
print('Tenha um bom dia')