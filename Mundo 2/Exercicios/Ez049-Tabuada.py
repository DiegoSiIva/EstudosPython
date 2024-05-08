print('\033[1;7m Veja aqui a tabuada de um numero\033[m\n')

v = int(input('Digite um valor: '))
s = 0
print('Soma\n')
for c in range(1,11):
    x = c
    print('{} + {} = {}'.format(x, v, x + v))
print('\n')
print('Subtração\n')
for c in range(1,11):
    x = c
    print('{} - {} = {}'.format(x, v, v - x))

print('\n')
print('Divisão\n')
for c in range(1,31):
    x = c
    d = v / x
    if d%2 == 0:
        print('{} / {} = {}'.format(v, x, d))

print('\n')
print('Multiplicação\n')
for c in range(1,11):
    x = c
    print('{} * {} = {}'.format(x, v, v * x))