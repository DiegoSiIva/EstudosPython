print('\033[7mEscreva valores de 0 até 999 e veja a soma entre eles\033[m')

n = 0
soma = 0
cont = 0
while True:

    n = int(input('Digite valores até 999: '))
    if n < 999:
        soma += n
        cont += 1
    elif n == 999:
        break

print('Você digitou {} valores, e o resultado da soma entre eles foi {}'.format(cont, soma))