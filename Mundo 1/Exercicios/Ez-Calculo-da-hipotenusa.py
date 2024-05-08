from math import pow, sqrt
print('Faça o calculo da Hipotenusa!\n')
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cate adjacente: '))

co = pow(co, 2)
ca = pow(ca, 2)

hipotenusa = sqrt(co + ca)

print('O valor da Hipotenusa é {:.2f}'.format(hipotenusa))