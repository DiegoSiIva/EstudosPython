jogador = dict()
gols = list()
totgol = 0
print('-' * 30)
print(f'{"VEJA SEU APROVEITAMENTO":^30}')
print('-' * 30)

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantos jogos você jogou?: '))

for c in range(0, jogador['partidas']):
    gl = int(input(f'Quantos gols você fez na {c+1}° partida: '))
    gols.append(gl)
    totgol += gl

jogador['gols'] = gols
jogador['totgol'] = totgol

print('-=' * 30)
print(f'{"ESTATISTICAS DO JOGADOR":^30}')
print('-=' * 30)
print()
print(f'Nome: {jogador['nome']}\n'
      f'Partidas jogadas: {jogador['partidas']}\n'
      f'Total de gols: {jogador['totgol']}')
print()
print('GOLS POR PARTIDA')
print()
for i, o in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {o} gols')
print('-=' * 30)