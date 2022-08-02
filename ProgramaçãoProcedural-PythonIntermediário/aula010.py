"""
Dictionary Comprehension Python
"""

lista1 = [
    ('chave1', 2),
    ('chave2', 4)
]
d1 = {x.upper(): y * 2 for x, y in lista1}  # multiplicando valores de dict com comprehension
print(lista1)
print(d1)

d2 = {x for x in range(10)}  # set com comprehension
print(d2, type(d2))

d3 = {f'chave {x}': x * 2 for x in range(10)}  # criando dict com for em comprehension
print(d3, type(d3))

