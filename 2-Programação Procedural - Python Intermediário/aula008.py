"""
sets em Python - Conjuntos
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
sets não tem indíces
"""

set1 = {1, 2, 3, 4, 5, 6}
print(set1)
set1.discard(2)
print(set1)
set1.update('Python')  # não apresenta os elementos em ordem
print(set1)
set2 = set()
set2.add(1)
set2.add(2)
set2.add('Eliezer')
print(set2)
print('______________')

# o set não aceita elementos duplicados
# por isso é comum usa-lo para remover elementos duplicados de uma lista
lista = [1, 2, 1, 3, 1, 1, 3, 4, 5, 4, 3, 1, 'Eliezer', 'Eliezer']
print(lista)
set3 = set(lista)
print(set3)
lista = list(set3)
print(lista)
print('______________')

# union - unindo dois sets
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2
print(s3)
print('______________')

# intersection - os elementos que estão presentes em ambos sets
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 & s2
print(s3)
print('______________')

# diference - elementos apenas no set da esquerda nesse caso o s1
s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 - s2
print(s3)
print('______________')

# symetric diference - Elementos que estão nos dois sets, mas não em ambos
s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 ^ s2
print(s3)
print('______________')

# função útil para verificar se duas listas são iguais sem modificar as listas
# não considerando a ordens dos elementos

lista1 = ['João', 'Maria', 'Eliezer']
lista2 = ['Maria', 'Eliezer', 'João', 'Eliezer', 'João']

if set(lista1) == set(lista2):
    print('lista1 é igual a lista2')
else:
    print('lista1 é diferente de lista2')
