time = ('Flamengo', 'Internacional', 'Juventude', 'Bragantino', 'Cruzeiro', 'Fortaleza', 'Athletico-PR', 'Grêmio', 'Vasco da Gama', 'Bahia', 'Botafogo', 'Palmeiras', 'Criciúma', 'Atlético-MG', 'Fluminense', 'Corithians', 'EC Vitória', 'São Paulo', 'Atlético-GO', 'Cuiabá')

print(f'\033[7mOs primeiros colocados são:\033[m\n'
      f'{time[:5]}\n')
print(f'\033[7mOs ultimos colocados sâo:\033[m\n'
      f'{time[16:]}\n')
print(f'\033[7mEsses são os times que estão na tabela\033[m\n')
print(f'{sorted(time)}\n')

print(f'O Bragantino esta na posição {time.index('Bragantino')}')