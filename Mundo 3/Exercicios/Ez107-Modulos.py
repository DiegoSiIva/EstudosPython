from Modulos.utilidades.moeda import moeda


p = float(input('Digite o preço: R$'))

print(f'A metade de {p} é {moeda.metade(p)}\n'
      f'O dobro de {p} é {moeda.dobro(p)}\n'
      f'{p} Adicionando 13% fica {moeda.aumenta(p, 13)}\n'
      f'{p} Subtraindo 10% fica {moeda.diminui(p, 10)}')
