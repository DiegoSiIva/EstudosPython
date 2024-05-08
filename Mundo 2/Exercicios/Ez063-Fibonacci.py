print('\033[7mSequência de Fibonacci\033[m\n')

n = int(input('Digite quantos termos deseja ver: '))
n1 = 0
n2 = 1
cont = 0

print('\n {} -> {}'.format(n1, n2), end='')

while cont < n - 2:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1

