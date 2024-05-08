def ficha(nome='', gols=0):
    if nome == '':
        nome = '<jogador desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')


n = input('Digite o nome do jogador: ')

g = input('Quantos gols o jogador fez: ')

ficha(n, g)