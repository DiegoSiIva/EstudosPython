produtos = ('macarrao', 7.50, 'peixe', 18.90, 'arroz', 5.30, 'feijao', 8.90, 'carne', 22.00)

print('_' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('_' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]: >5.2f}')

print('_' * 40)