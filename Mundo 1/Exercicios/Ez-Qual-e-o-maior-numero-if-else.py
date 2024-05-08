n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

if n1 > n2:
    if n1 > n3:
        print('O primeiro numero é o maior')
    else:
        print('O terceiro numero é o maior')
else:
    if n2 > n3:
        print('O segundo numero é o maior')
    else:
        print('O terceiro numero é o maior')