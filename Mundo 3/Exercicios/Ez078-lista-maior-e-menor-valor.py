
maior = 0
menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um numero na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Esses foram os valores digitados {valores}')
print(f'O maior valor digitado foi {maior} e esta na posição ', end='')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}...', end='')
print(f'\nO menor valor foi {menor} que esta na posição ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}...', end='')