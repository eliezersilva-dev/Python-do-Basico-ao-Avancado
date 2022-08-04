"""
List Comprehension Python
Sintaxe:
newlist = [expression for item in iterable if condition == True]
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]  # iterando sobre cada elemento da lista
print(l2)
print('--------------------------')

ex2 = [v * 2 for v in l1]  # iterando e realizando operações
print(ex2)
print('--------------------------')

ex3 = [(v, v2) for v in l1 for v2 in range(3)]  # usando dois laços for
print(ex3)
print('--------------------------')

l3 = ['Eliezer', 'João', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l3]  # usando funções
print(ex4)
print('--------------------------')

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for x, y in tupla]
print(ex5)
ex5 = [(y, x) for x, y in tupla]  # invertendo valores de exibição
print(ex5)
ex5 = dict(ex5)  # fazndo casting de tuple para dict
print(ex5)
print('--------------------------')

l4 = list(range(100))
ex6 = [v for v in l4 if v % 3 == 0 if v % 8 == 0]  # usando if
print(ex6)
print('--------------------------')

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l4]  # usando else
print(ex7)
print('--------------------------')






