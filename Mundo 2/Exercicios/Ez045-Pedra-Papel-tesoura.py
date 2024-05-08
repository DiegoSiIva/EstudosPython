from random import choice

print('\033[1;7mVamos jogar pedra, papel e tesoura\033[m\n')

escolha = str(input('O que você escolhe: ')).lower()

n1 = 'pedra'
n2 = 'papel'
n3 = 'tesoura'

lista = [n1, n2, n3]
escolhido = choice(lista)



if escolha == 'pedra':
    if escolhido == 'papel':
        print('O computador ganhou! ele escolheu {}'.format(escolhido))
    elif escolhido== 'pedra':
        print('Ninguem ganhou! ele escolheu {}'.format(escolhido))
    else:
        print('Você ganhou! ele escolheu {}'.format(escolhido))
elif escolha == 'papel':
    if escolhido == 'papel':
        print('Ninguem ganhou! ele escolheu {}'.format(escolhido))
    elif escolhido == 'pedra':
        print('Você ganhou! ele escolheu {}'.format(escolhido))
    else:
        print('O computador ganhou! ele escolheu {}'.format(escolhido))
elif escolha == 'tesoura':
    if escolhido == 'pedra':
        print('Você perdeu! ele escolheu {}'.format(escolhido))
    elif escolhido == 'papel':
        print('Você ganhou! ele escolheu {}'.format(escolhido))
    else:
        print('Ninguem ganhou! ele escolheu {}'.format(escolhido))
else:
    print('Não existe esse obejto neste jogo!')