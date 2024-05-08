velocidade = int(input('Digite a velocidade do carro: '))

multa = velocidade * 7

if velocidade >= 80:
    print('Você excedeu o limite de velocidade e foi multado em: {}R$'.format(multa))
else:
    print('Você esta no limite da via!')
