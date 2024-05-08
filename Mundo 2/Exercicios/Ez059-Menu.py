n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
controle = 0
while controle != 5:
    controle = int(input(
                         '\n[1] \033[33mSOMAR\033[m\n'
                         '[2] \033[33mMULTIPLICAR\033[m\n'
                         '[3] \033[33mMAIOR\033[m\n'
                         '[4] \033[33mNOVOS NUMEROS\033[m\n'
                         '[5] \033[33mSAIR DO PROGRAMA\033[m\n'
                         'ECOLHA UMA OPÇÃO: '))
    if controle == 1:
        print('\nA soma de {} + {} = {}\n'.format(n1, n2, n1+n2))
    elif controle == 2:
        print('\nA multiplicação de {} * {} = {}'.format(n1, n2, n1*n2))
    elif controle == 3:
        if n1 > n2:
            print('\n{} é o maior'.format(n1))
        else:
            print('\n{} é o maior'.format(n2))
    elif controle == 4:
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('Digite outro número: '))

print('FIM')