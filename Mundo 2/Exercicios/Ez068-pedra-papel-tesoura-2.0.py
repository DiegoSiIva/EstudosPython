from random import choice

print('\033[7mBem vindo ao jokenpo simulator\033[m\n')

while True:
    escolha = str(input('Escolha oque quer jogar: ')).lower()
    count = 0
    n1 = 'pedra'
    n2 = 'papel'
    n3 = 'tesoura'

    lista = [n1, n2, n3]

    computador = choice(lista)

    if computador == n1:
        if escolha == n1:
            print('Empate!')
        elif escolha == n2:
            count += 1
            print('Vitoria')
        else:
            print('Derrota')
            print(f'Seu total de vitoria consecutivas foi {count}')
            break

    if computador == n2:
        if escolha == n1:
            print('Derrota')
            print(f'Seu total de vitoria consecutivas foi {count}')
            break
        elif escolha == n2:
            print('Empate!')
        else:
            print('Vitoria!')
            count += 1

    if computador == n3:
        if escolha == n1:
            print('Vitoria!')
            count += 1
        elif escolha == n2:
            print('Derrota!')
            print(f'Seu total de vitoria consecutivas foi {count}')
            break
        else:
            print('Empate!')