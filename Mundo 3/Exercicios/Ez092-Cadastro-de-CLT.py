pessoa = dict()

print('_' * 30)
print(f'{"SAIBA QUANDO VAI SE APOSENTAR":^30}')
print('_' * 30)

pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['ano'] = int(input('Digite seu ano de nascimento: '))
pessoa['sexo'] = str(input('Qual o seu sexo? [M/F]: '))
idade = 2024 - pessoa['ano']


ctps = str(input('Você possui carteira de trabalho? [S/N]: '))
if ctps in 'Ss':
    pessoa['anocont'] = int(input('Em que ano você foi contratado?: '))
    pessoa['salario'] = float(input('Qual o seu salario?: '))
    aposentah = pessoa['anocont'] + 35
    aposentam = pessoa['anocont'] + 30

    if pessoa['sexo'] in 'Mm':
        print('-=' * 20)
        print(f'{pessoa["nome"].capitalize()} você irá se aposentar em {aposentah}!')
        print('-=' * 20)
        print(f'Nome: {pessoa["nome"]}\n'
              f'Idade: {idade}\n'
              f'Sexo: {pessoa["sexo"]}asculino\n'
              f'Salario: {pessoa["salario"]:0.2f}R$\n'
              f'Aposentadoria: {aposentah}')
        print('-=' * 20)
    else:
        print('-=' * 20)
        print(f'{pessoa["nome"].capitalize()} você irá se aposentar em {aposentam}!')
        print('-=' * 20)
        print(f'Nome: {pessoa["nome"]}\n'
              f'Idade: {idade}\n'
              f'Sexo: {pessoa["sexo"]}eminino\n'
              f'Salario: {pessoa["salario"]:0.2f}R$\n'
              f'Aposentadoria: {aposentam}')
        print('-=' * 20)
else:
    print('Para que você se aposente é necessario ter uma carteira de trabalho!')
    print('-=' * 20)
    print(f'Nome: {pessoa["nome"]}\n'
          f'Idade: {idade}\n'
          f'Sexo: {pessoa["sexo"]}')
    print('-=' * 20)

