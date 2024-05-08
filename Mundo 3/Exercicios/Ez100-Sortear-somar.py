from random import randint

numeros = list()


def sorteia():

    for c in range(0, 5):
        numeros.append(randint(0, 100))
    print(f'Os valores sorteados foram: {numeros}')


def somaPar():
    somapar = 0
    for valor in numeros:
        if valor % 2 == 0:
            somapar += valor
    print(f'A soma dos valores pares foi {somapar}')


sorteia()
somaPar()


