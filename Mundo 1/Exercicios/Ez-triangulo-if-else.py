n1 = int(input('Digite o valor da primeira reta: '))
n2 = int(input('Digite o valor da segunda reta: '))
n3 = int(input('Digite o valor da terceira reta: '))

if n1 == n2:
    if n1 == n3:
        print('Essas três retas podem formar um triangulo!')
    else:
        print('Essas retas não podem formar um trinagulo pois são diferentes')
else:
    print('Essas retas não podem ser um triangulo!')