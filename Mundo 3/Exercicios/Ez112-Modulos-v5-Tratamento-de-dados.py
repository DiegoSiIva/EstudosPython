from Modulos.utilidades.dados import dado
from Modulos.utilidades.moeda import moeda
p = dado.leiadinheiro('Digite o preço: R$')

moeda.resumo(p, 80, 30)
