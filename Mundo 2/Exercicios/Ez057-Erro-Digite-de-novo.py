sexo = str(input('Digite seu sexo [M/F]: ')).upper()
controle = 0

if sexo == 'M':
    controle += 1
elif sexo == 'F':
    controle += 1
else:
    while controle == 0:
        sexo = input('Digite o sexo novamente [M/F]: ').upper()
        if sexo == 'M':
            controle += 1
        elif sexo == 'F':
            controle += 1
print('FIM')