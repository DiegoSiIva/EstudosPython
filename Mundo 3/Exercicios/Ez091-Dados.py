from random import randint
from time import sleep
from operator import itemgetter
valores = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}
ranking = dict()
print('-='*4, 'VALORES RANKEADOS', '-='*4)
for indice, objeto in valores.items():
    print(f'O {indice} tirou {objeto}')
    sleep(1)
print()
print('-='*4, 'RANKING', '-='*4)

ranking = sorted(valores.items(), key=itemgetter(1), reverse = True)
for indice, objeto in enumerate(ranking):
    print(f'O {objeto[0]} ficou em {indice+1}° e tirou {objeto[1]} no dado')
    sleep(1)