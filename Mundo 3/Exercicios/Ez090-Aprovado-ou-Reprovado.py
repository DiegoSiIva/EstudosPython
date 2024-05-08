aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
print(f'O aluno {aluno["Nome"]} está {aluno["Situação"]} pois a média dele foi {aluno["Média"]}')