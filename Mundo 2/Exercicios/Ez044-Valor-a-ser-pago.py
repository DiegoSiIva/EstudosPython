valor = float(input('Digite o valor do produto a ser pago: '))
avi = valor * 10/100
avic = valor * 5/100
car2x = valor / 2
car3x = valor * 20/100

forma = str(input('Qual vai ser a forma de pagamento?: ')).lower()

if forma in 'dinheiro cheque':
    print('O valor de a vista é {:.2f}'.format(valor-avi))
elif forma == 'cartão':
    parcela = int(input('Em quantas vezes você vai passar?: '))
    if parcela == 1:
        print('O valor é {:.2f}R$ com 5% de desconto'.format(valor-avic))
    elif parcela == 2:
        print('O valor das parcelas é de {:.2f}R$'.format(car2x))
    elif parcela >= 3:
        print('O valor das parcelas é de {:.2f}R$ com o acrescimo de 20%'.format((valor+car3x)/parcela))
else:
    print('Não aceitamos essa forma de pagamento!')