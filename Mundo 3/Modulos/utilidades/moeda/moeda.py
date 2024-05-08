def moedas(num, moeda='R$'):
    return f'{moeda}{num:<8.2f}'.replace('.', ',')


def metade(num, format=False):
    met = num / 2
    return met if format is False else moedas(met)


def dobro(num, format=False):
    dob = num * 2
    return dob if format is False else moedas(dob)


def aumenta(num, porcentagem, format=False):
    mais = num * (porcentagem / 100)
    soma = num + mais
    return soma if format is False else moedas(soma)


def diminui(num, porcentagem, format=False):
    menos = num * (porcentagem / 100)
    sub = num - menos
    return sub if format is False else moedas(sub)


def resumo(num, porcentagemmais, porcentagemmenos):
    print('_' * 30)
    print(f'{'RESUMO DO VALOR':^25}')
    print('_' * 30)
    print(f'Preço analisado: \t{moedas(num)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'O dobro do preço: \t{dobro(num, True)}')
    print(f'{porcentagemmais}% de aumento: \t{aumenta(num, porcentagemmais, True)}')
    print(f'{porcentagemmenos}% de redução: \t{diminui(num, porcentagemmenos, True)}')
    print('_' * 30)
