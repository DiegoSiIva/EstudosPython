continua = 'S'
n = 0
cont = 0
soma = 0
maior = 0
menor = 0
while continua in 'Ss':
    cont += 1
    n = int(input('Digite um numero: '))
    soma += n
    if maior < n:
        maior = n
    if menor == 0:
        menor = n
    if menor > n:
        menor = n
    continua = str(input('Deseja digitar outro ?[S/N]: '))
media = soma / cont
print('A média desses valores é {} e o maior valor foi {} e o menor foi {}'.format(media, maior, menor))