#def soma(a, b):
    #s = a + b
    #print(f'O resultado da soma foi {s}')


#soma(1, 2)
#soma(4, 8)
#soma(2, 5)


def contador(*num):
    tam = len(num)
    for valor in num:
        print(f'{valor}', end=' ')
    print(f' Foram recebidos {tam} valores')

contador(7,4,3,2,0)