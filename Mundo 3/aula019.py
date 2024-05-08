estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for elemento in brasil:
    for indice, objeto in elemento.items():
        print(f'O campo {indice} tem valor {objeto}')
