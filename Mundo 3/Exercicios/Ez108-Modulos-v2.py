from Modulos.utilidades.moeda import moeda


p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moedas(p)} é {moeda.moedas(moeda.metade(p), 'R$')}\n'
      f'O dobro de {moeda.moedas(p)} é {moeda.moedas(moeda.dobro(p), 'R$')}\n'
      f'{moeda.moedas(p)} Adicionando 13% fica {moeda.moedas(moeda.aumenta(p, 13), 'R$')}\n'
      f'{moeda.moedas(p)} Subtraindo 10% fica {moeda.moedas(moeda.diminui(p, 10), 'R$')}')
