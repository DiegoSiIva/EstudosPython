print('Alistamento Militar Obrigatorio!\n')

ano = int(input('Qual o seu ano de nascimento?: '))
idade = 2024 - ano
vencimento = idade - 18
falta = 18 - idade

if idade == 18:
    print('Este ano você fez 18 anos e precisa se alistar!')

elif idade > 18:
    print('Você esta atrasado e já deveria ter se alistado a {} ano(s)'.format(vencimento))

elif idade < 18:
    print('Ainda é cedo para você se alistar, faltam {} ano(s) para que você possa se alistar'.format(falta))
