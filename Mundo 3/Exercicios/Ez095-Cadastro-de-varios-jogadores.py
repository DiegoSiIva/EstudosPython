jogador = dict()
jogadores = list()
gols = list()

print('-' * 30)
print(f'{"VEJA SEU APROVEITAMENTO":^30}')
print('-' * 30)

while True:
    totgol  = 0
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Quantos jogos você jogou?: '))

    for c in range(0, jogador['partidas']):
        gl = int(input(f'Quantos gols você fez na {c + 1}° partida: '))
        gols.append(gl)
        totgol += gl

    jogador['gols'] = gols[:]
    jogador['totgol'] = totgol
    jogadores.append(jogador.copy())


    while True:
        continuar = str(input('Deseja cadastrar outro jogador?[S/N]')).upper()
        if continuar in 'SN':
            break
        print('Digite um valor valido![S/N]')
    if continuar in 'N':
        break


print('-=' * 30)
print(f'{"cod nome":<4}{"partidas":>15}{"gols":>15}{"total":>15}')
print('_' * 41)
for c, o in enumerate(jogadores):
    print(f'\n{c:<3}', end='')
    for k in o.values():
        print(f'{str(k):<15}', end='')

while True:

    cod = int(input('Digite o codigo do jogador que deseja verificar: '))
    if cod >= len(jogadores):
        print(f'ERROR! NÃO EXISTE JOGADOR COM O CODIGO {cod}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"].upper()}')
        for c, o in enumerate(jogadores[cod]["gols"]):
            print(f'=> Na partida {c + 1}, fez {o} gols')
    while True:
        conti = str(input('Deseja buscar outro jogador?[S/N]')).upper()
        if conti in 'SN':
            break
        print('Digite um valor valido![S/N]')
    if conti in 'N':
        break
