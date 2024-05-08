from Modulos.utilidades.moeda import moeda


p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moedas(p)} é {moeda.metade(p, True)}\n'
      f'O dobro de {moeda.moedas(p)} é {moeda.dobro(p, True)}\n'
      f'{moeda.moedas(p)} Adicionando 13% fica {moeda.aumenta(p, 13, True)}\n'
      f'{moeda.moedas(p)} Subtraindo 10% fica {moeda.diminui(p, 10, True)}')
