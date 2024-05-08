matriz = [[], [], []]
valor = 0
par = 0
soma = 0
maior = 0
for linha in range(0, 3):

    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para a posição [{linha}, {coluna}]'))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            par += valor
        if coluna == 2:
            soma += valor
        if linha == 1 and valor > maior:
            maior = valor

print('-=' * 30)
for l in range(0, 3):

    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()
print('-=' * 30)
print(f'A soma dos números pares digitados foi: {par}')
print(f'A soma dos valores da terceira coluna foi: {soma}')
print(f'O maior valor da segunda linha foi {maior}')