"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista1 = [1, 2, 3, 5, 'eliezer', True, 1.2]

# utilizando os índices
#          0    1    2    3    4
lista2 = ['A', 'B', 'C', 'D', 'E']
#         -5   -4   -3   -2   -1
print(lista2[4])
print(lista2[0:3:1])  # fatiamento
print(lista2[::-1])   # invertendo lista

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)

l3 = l1 + l2
print(l3)

l3.append('a')
print(l3)

l3.insert(0, 'banana')
print(l3)

l3.pop()
print(l3)

del(l3[0])
print(l3)

# Somar todos os valores de uma lista
# que contenha os valores de 1 a 10
l4 = list(range(1, 11))
print(l4)
soma = 0
for i in l4:
    soma = soma + i
print(soma)


# Checar o Type de cada elemento da lista
l5 = ['sting', True, 10, 10.5]
for i in l5:
    print(f'{i} {type(i)}')


