def area(compr,larg):
    metro = compr * larg
    print(f'A area de um terreno {compr:0.1f}x{larg:0.1f} é de {metro}m²')


print('Controle de Terrenos')
print('_'* 20)
compr1 = float(input('Digite o comprimento do terreno(m): '))
larg1 = float(input('Agora digite a largura do terreno(m): '))

area(compr1, larg1)