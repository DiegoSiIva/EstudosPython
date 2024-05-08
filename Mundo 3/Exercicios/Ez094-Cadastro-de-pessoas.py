lista = list()
mulher = list()
homem = list()
pessoa = dict()
cont = 0
totidade = 0
print('-=' * 20)
print(f'{"CADASTRO DE PESSOAS":^40}')
print('-=' * 20)
print()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F!')
    if pessoa['sexo'] in 'M':
        homem.append(pessoa.copy())
    elif pessoa['sexo'] in 'F':
        mulher.append(pessoa.copy())
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    totidade += pessoa['idade']

    while True:
        continua = str(input('Deseja cadastrar outra pessoa?[S/N]: ')).upper()
        if continua in 'NS':
            break
        print('Digite um valor valido [S/N]')
    if continua in 'N':
        print('Cadastro realizado com sucesso!')
        break
media = totidade / len(lista)
print('-=' * 30)
print()
print('\033[7mPESSOAS CADASTRADAS\033[m')
print()
print(f'Pessoas cadastradas: {len(lista)}\n'
      f'Media de idade: {media:5.2f}\n'
      f'Mulheres cadastradas:', end='')
for c in mulher:
    print(f' {c["nome"]}', end=' ')
print(f'\nEssas são as pessoas que estão a cima da média de idade:')
for c in lista:
    if c['idade'] >= media:
        print('    ')
        for i, o in c.items():
            print(f'{i} = {o}; ', end='')
        print()



