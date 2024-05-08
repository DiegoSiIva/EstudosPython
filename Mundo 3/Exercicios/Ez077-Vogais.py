vogais = ('carro', 'casa', 'bola', 'pedra', 'lua', 'mesa', 'paralelepipedo')

for c in vogais:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
