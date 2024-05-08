def voto(ano):
    from datetime import datetime
    data_atual = datetime.now()
    idade = data_atual.year - ano
    if idade < 18:
        print(f'Com {idade} anos: VOTO NEGADO!')
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATORIO!')
    else:
        if idade >= 65:
            print(f'Com {idade} anos: VOTO OPCIONAL')


i = int(input('Digite seu ano de nascimento: '))
voto(i)

