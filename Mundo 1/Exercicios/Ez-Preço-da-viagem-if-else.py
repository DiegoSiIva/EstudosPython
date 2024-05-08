km = float(input('Digite a distancia em km da viagem: '))

curta = 0.50 * km

longa = 0.45 * km

if km <= 200:
    print('Você vai gastar {:0.2f}R$ nesta viagem'.format(curta))
else:
    print('Você vai gastar {:0.2f}R$ nesta viagem'.format(longa))
print('Boa Viagem!!')