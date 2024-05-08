print('\033[1;7mVeja se você pode comprar sua casa conosco!!\033[m\n')

valor = float(input('Digite o valor da casa que você deseja comprar: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Em quantos anos pretende pagar as parcelas: '))

prestacao = valor / (anos*12)
limite = salario * 30/100

if prestacao > limite:
    print('O valor das prestações excederam o 30% do seu salarios e infelizmente o emprestimo foi negado!')
else:
    print('O emprestimo foi aprovado, e as prestações serão de {:.2f}R$ por mês.'.format(prestacao))

print(limite)