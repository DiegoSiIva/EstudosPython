valores = []
count = 0
while True:

    a = int(input(f'Digite um valor para posição {count}: '))
    if a in valores:
        print('Esse número já existe')
        count -= 1
    else:
        valores.append(a)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
    else:
        if continuar != 'S':
            print('Digite um valor valido!')
            continuar = str(input('Deseja continuar? [S/N]: ')).upper()


    count += 1
print(valores.sort())
