ficha = list()
contador = 0
print('-=' * 4,f'CADASTRO DE ALUNOS', '-=' * 4)
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    contador += 1
    ficha.append([nome, [nota1, nota2], media])
    cont = str(input('Deseja cadastrar mais algum aluno?[S/N]: '))
    if cont in 'Nn':
        break
print('-=' * 4, 'ALUNOS CADASTRADOS', '-=' * 4)
print()
for c in range(0, contador):
    print('-=' * 30)
    print(f'Aluno: {ficha[c][0]}')
    print(f'Nota 1: {ficha[c][1][0]}')
    print(f'Nota 2: {ficha[c][1][1]}')
print('-=' * 30)

print('-=' * 4, 'BOLETINHO', '-=' * 4)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')

