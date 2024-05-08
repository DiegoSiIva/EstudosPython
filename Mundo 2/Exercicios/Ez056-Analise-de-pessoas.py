somaidade = 0
maioridadehomem = 0
nomevelho = ''
idademulher = 20
r = 0

for c in range(1, 5):
    print('{}° PESSOA'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).lower().strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < idademulher:
        r += 1


print('A media de idade é de {} anos'.format(somaidade / 4))
print('O nome do mais velho é {} e ele tem {} anos'.format(nomevelho, maioridadehomem))
print('Neste grupo {} mulheres tem menos de 20 anos'.format(r))
