print('Veja se vc foi aprovado!\n\n')

n1 = float(input('Digite a nota da primeira unidade: '))
n2 = float(input('Digite a nota da segunda unidade: '))
n3 = float(input('Digite a nota da terceira unidade: '))

media = (n1+n2+n3)/3

print('Sua media foi: {:0.1f}'.format(media))

if media >= 7:
    print('Você foi aprovado!!!')
else:
    print('Você foi reprovado! :(')