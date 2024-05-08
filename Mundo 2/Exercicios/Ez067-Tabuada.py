n = int(input('Quer ver a tabuada de qual valor? '))
count = 0
print('_' * 30)

while True:
    count += 1
    if n > 0:
        print(f'{n} x {count} = {n * count}')

    if count >= 10:
        count = 0
        n = int(input('Quer ver a tabuada de qual valor? '))
        print('_' * 30)

    if n < 0:
        break