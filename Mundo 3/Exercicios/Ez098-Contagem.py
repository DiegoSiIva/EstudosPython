from time import sleep


def contagem(inicio, fim, passo):
    if inicio - fim < 0:
        if passo > 0:
            print('-=' * 30)
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            while inicio <= fim:
                print(inicio, end=' ')
                inicio += passo
                sleep(0.5)
            print('FIM!')
            print()
        if passo == 0:
            print('-=' * 30)
            print(f'Contagem de {inicio} até {fim} de 1 em 1')
            while inicio <= fim:
                print(inicio, end=' ')
                inicio += 1
                sleep(0.5)
            print('FIM!')
            print()
    else:
        if passo > 0:
            print('-=' * 30)
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            while inicio >= fim:
                print(inicio, end=' ')
                inicio -= passo
                sleep(0.5)
            print('FIM!')
            print()
            print('-=' * 30)
        if passo < 0:
            print('-=' * 30)
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            while inicio >= fim:
                print(inicio, end=' ')
                inicio += passo
                sleep(0.5)
            print('FIM!')
            print()
            print('-=' * 30)
        if passo == 0:
            print('-=' * 30)
            print(f'Contagem de {inicio} até {fim} de 1 em 1')
            while inicio >= fim:
                print(inicio, end=' ')
                inicio -= 1
                sleep(0.5)
            print('FIM!')
            print()
            print('-=' * 30)


contagem(0, 10, 1)
contagem(10, 0, 2)
print()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)