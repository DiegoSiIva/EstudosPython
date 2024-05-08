exp = str(input('Digite a expressão: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')


if len(pilha) % 2 == 0:
    print('A expressão está correta!')

if len(pilha) % 2 == 1:
    print('A expressão está incorreta!')
