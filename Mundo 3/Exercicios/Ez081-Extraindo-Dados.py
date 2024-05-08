lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} valores\n\n'
      f'Os valores digitados na ordem decrescente foram {lista})\n')
if 5 in lista:
    print(f'O valor 5 foi digitado e esta na lista')
else:
    print('O valor 5 não foi digitado e não esta na lista')