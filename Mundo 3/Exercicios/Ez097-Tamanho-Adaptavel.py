def escreva(text):
    tam = len(text) + 4
    print('~' * tam)
    print(f'  {text}')
    print('~' * tam)


escreva('Ola mundo!')