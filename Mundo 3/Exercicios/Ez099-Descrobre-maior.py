from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando valores...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'O maior valor digitado foi {maior}')
    print('-=' * 30)

maior(1, 3, 4, 5, 6, 8)
maior(8, 10, 3, 1, 0)