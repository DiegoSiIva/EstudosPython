print('Descubra qual é o maior rs!!\n')

n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))

if n1 > n2:
    print('{} é o maior valor'.format(n1))
elif n2 > n1:
    print('{} é o maior valor'.format(n2))
else:
    print('Os dois valores são iguais')