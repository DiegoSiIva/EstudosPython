print('Veja aqui o quanto você gastou\n')
menorpreco = 0
nomemenor = ''
maismil = 0
precotudo = 0
count = 0
while True:

    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    precotudo += preco
    count += 1
    if count == 1:
        nomemenor = produto
        menorpreco = preco
    if preco < menorpreco:
        menorpreco = preco
        nomemenor = produto
    if preco >= 1000:
        maismil += 1
    continua = str(input('Deseja continuar ? [S/N]:  ')).upper()
    if continua == 'N':
        print(f'Você gastou um total de {precotudo:0.2f}R$\n'
              f'{maismil} produtos custaram mais de mil reais\n'
              f'{nomemenor} foi o produto mais barato e vc pagou {menorpreco:0.2f}R$ nele')
        break