lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = str(input('Deseja continuar? [S/N]'))

    if continuar in 'nN':
        break

    if num % 2 == 0:
        listapar.append(num)
    if num % 2 == 1:
        listaimpar.append(num)

print(f'Os valores digitados foram {lista}\n'
      f'Os números pares são {listapar}\n'
      f'Os números impares são {listaimpar}')