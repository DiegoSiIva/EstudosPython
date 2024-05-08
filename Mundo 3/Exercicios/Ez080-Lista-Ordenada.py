lista = []
for pos in range(0, 5):
    num = int(input(f'Digitie um valor para posição {pos+1}: '))
    if pos == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')