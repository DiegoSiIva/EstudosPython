def pyhelp(msg):
        print('\033[0;46m~' * 35, '\033[m')
        print(f'\033[0;46mAcessando o manual do comando {msg} \033[m')
        print('\033[0;46m~' * 35, '\033[m')
        print(f'{help(msg)}')


while True:
    print('\033[0;44m~' * 27, '\033[m')
    print('\033[0;44m  SISTEMA DE AJUDA PyHelp   \033[m')
    print('\033[0;44m~' * 27, '\033[m')

    h = str(input('Função ou Biblioteca > '))
    pyhelp(h)
    if h == 'fim':
        break

