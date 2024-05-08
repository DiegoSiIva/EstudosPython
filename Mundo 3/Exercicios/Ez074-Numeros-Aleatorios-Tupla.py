from random import randrange

tupla = (randrange(0, 10),
        randrange(0, 10),
        randrange(0, 10),
        randrange(0, 10),
        randrange(0, 10))


print(tupla)

tupla = sorted(tupla)

print(f'O maior valor é {tupla[4]}')
print(f'O menor valor é {tupla[0]}')
