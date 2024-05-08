def leiadinheiro(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isalpha() or n.strip() == '':
            print(f'\033[0;31mERRO! "{n}" é um preço invalido\033[m')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return valor
