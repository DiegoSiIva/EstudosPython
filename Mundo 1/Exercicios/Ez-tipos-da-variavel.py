n1 = input('Digite algo:')

print('O tipo dessa variavel é:', type(n1))
print('Essa variavel  é composta só de espaços ?', n1.isspace())
print('Essa variavel é alphanumerico?', n1.isalnum())
print('Essa variavel é alfabético?', n1.isalpha())
print('Essa variavel esta em maiusculo?', n1.isupper())
print('Essa variavel esta em minusculo?', n1.islower())
print('Essa variavel esta capitalizada ?', n1.istitle())#capitalizada é quando a primeira letra é maiuscula e o resto minusculo
print('Essa variavel é um número?',n1.isnumeric())
print('Essa variavel é um número decimal?',n1.isdecimal())