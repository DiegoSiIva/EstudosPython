lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')