
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
nomesep = nome.split()
nomesemespaço = "".join(nomesep)
print('Seu nome completo tem', len(nomesemespaço), 'letras')
print('Seu primeiro nome tem', len(nomesep[1]), 'letras')