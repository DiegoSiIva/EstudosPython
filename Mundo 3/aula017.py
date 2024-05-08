num =[2, 5, 9, 1]
numcopia = num[:] #cria uma copia da lista num
numigual = num #cria uma ligação entre as listas, oque acontecer em uma acontee na outra
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop()
del num[3]
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')