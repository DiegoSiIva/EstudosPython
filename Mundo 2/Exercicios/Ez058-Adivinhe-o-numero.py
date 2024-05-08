import random

computador = random.randrange(11)
pessoa = 0
tentativas = 0
print('\033[7m Tente adivinhar o numero que o computador escolheu!\033[m\n')

while pessoa != computador:
    pessoa = int(input('Digite um numero de 0 a 10: '))
    tentativas += 1

print('\nVocê acertou!! O computador tbm escolheu {}'.format(computador))
print('Voê fez {} tetativas'.format(tentativas))

