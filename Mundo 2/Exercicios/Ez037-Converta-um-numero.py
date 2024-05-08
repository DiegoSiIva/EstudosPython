print('\033[1;7;35mConverta seu numero para binario, octal ou hexadecimal\033[m\n\n')

numero = int(input('Digite o numero que deseja converter: \n'))
bin = bin(numero)
octal = oct(numero)
hexa = hex(numero)

modo = str(input('Para qual formato deseja converter?: '))

if modo == 'binario':
    print('O numero {} convertido para binario é {}'.format(numero, bin))
elif modo == 'octal':
    print('O numero {} convertido para octal é {}'.format(numero, octal))
elif modo == 'hexadecimal':
    print('O numero {} convertido para hexadimal é {}'.format(numero, hexa))
else:
    print('Não existe essa conversão!!')