from random import randrange

print('\033[7mBem vindo ao par ou impar simulator\033[m\n')
count = 0
while True:
    escolha = str(input('Escolha oque quer jogar: ')).lower()
    jogador = int(input('Agora escolha um numero: '))
    computador = randrange(11)
    numero = jogador + computador



    if escolha == 'par':
        if numero % 2 == 0:
            print(f'Vitoria! O computador jogou \033[32m{computador}\033[m e você \033[34m{jogador}\033[m')
            count += 1
        else:
            print(f'Derrota!O computador jogou \033[32m{computador}\033[m e você \033[34m{jogador}\033[m')
            print(f'Seu total de vitoria consecutivas foi {count}')
            break
    if escolha == 'impar':
        if numero % 2 == 0:
            print(f'Derrota!O computador jogou \033[32m{computador}\033[m e você \033[34m{jogador}\033[m')
            print(f'Seu total de vitoria consecutivas foi {count}')
            break
        else:
            print(f'Vitoria!O computador jogou \033[32m{computador}\033[m e você \033[34m{jogador}\033[m')
            count += 1
