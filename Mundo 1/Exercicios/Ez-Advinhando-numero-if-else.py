import random

n = random.randrange(6)

m = int(input('Tente adivinhar um numero de 0 a 5 que o computador escolheu: '))

if m == n:
    print('Você acertou parabens!!')
else:
    print('O computador venceu!!')
print('O numero era: {}'.format(n))