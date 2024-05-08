from math import factorial

n = int(input('Digite um número: '))
p = 0
fatorial = factorial(n)
print('{}! = '.format(n), end='')
while p < n:
    p += 1
    if p < n:
        print('{}'.format(p), end='*')
    else:
        print(p, end='')
print(' = {}'.format(fatorial))