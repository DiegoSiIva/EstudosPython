def notas(*num, sit=False):
    soma = 0
    valores = dict()
    valores['maior'] = 0
    valores['menor'] = 0

    for valor in num:
        if valores['maior'] and valores['menor'] == 0:
            valores['maior'] = valor
            valores['menor'] = valor
        if valor > valores['maior']:
            valores['maior'] = valor
        if valor < valores['menor']:
            valores['menor'] = valor
        soma += valor
    valores['media'] = soma/len(num)

    if valores['media'] > 7:
        situação = '\033[0;32mAPROVADOS\033[m'
    else:
        situação = '\033[0;31mREPROVADOS\033[m'
    valores['total'] = len(num)
    print(valores)
    print(f'Foram lidas {valores['total']} nota(s)\n'
          f'A maior nota: {valores['maior']}\n'
          f'A menor nota: {valores['menor']}\n'
          f'A média da turma: {valores['media']:0.1f}')
    if sit:
        print(f'Situação da turma: {situação}')


notas(9.5, 8.2, 3, 10, 2, 4, 7, 1, sit=True)


#while True:
#   nota = int(input('Digite a nota do aluno: '))
#    while True:
#        cont = str(input('Deseja cadastrar outra nota?[S/N]: ')).upper()
#        if cont in 'SN':
#            break
#        print('\033[0;31mERRO! Digite um valor valido!\033[m')
#    if cont in 'N':
#        break

