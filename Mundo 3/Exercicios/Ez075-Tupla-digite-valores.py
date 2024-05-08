tupla = (
    int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')))

if 9 in tupla:
    print(f'O numero 9 apareceu {tupla.count(9)} vez(es)\n')
else:
    print('O valor 9 não foi digitado em nenhuma vez')


if 3 in tupla:
    print(f'O numero 3 apareceu na posição {tupla.index(3)+1}\n')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')


