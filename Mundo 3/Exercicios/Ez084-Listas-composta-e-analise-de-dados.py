pessoas = list()
dados = list()
print('-=' * 30)
print('Cadastre seu nome e peso.')
print('-=' * 30)
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    print('-=' * 30)
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar ?[S/N]: '))
    if continuar in 'Nn':
        break

print(f'\nForam cadastradas {len(pessoas)} pessoas\n')
print('-=' * 30)
print('Essas são as pessoas cadastradas mais pesadas:')
print('-=' * 30)
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]} pesando {p[1]}Kg')
print('-=' * 30)
print('Essas são as pessoas mais leves cadastradas:')
print('-=' * 30)
for c in pessoas:
    if c[1] < 100:
        print(f'{c[0]} pesando {c[1]}Kg')