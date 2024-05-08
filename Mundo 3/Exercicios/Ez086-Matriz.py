matriz = [[], [], []]
valor = 0
for linha in range(0, 3):

    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para a posição [{linha}, {coluna}]'))
        matriz[linha].append(valor)
print('-=' * 30)
for l in range(0, 3):

    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()