import random
from time import sleep

palpites = []

print('_' * 20)
print(f'{"JOGO DA MEGA SENA":^20}')
print('_' * 20)

qtdjogos = int(input('Quantos jogos você quer sortear?: '))

print()
print('-=' * 3, f'GERANDO {qtdjogos} JOGOS', '-=' * 3)
print()

for c in range(0, qtdjogos):
    palpites.append([])
    for num in range(0, 6):
        palpites[c].append(random.randrange(1, 60))

for count in range(0, qtdjogos):
    print(f'Jogo {count+1}:', palpites[count])
    sleep(1)

print()
print('-=' * 4, 'BOA SORTE!', '-=' * 4)

