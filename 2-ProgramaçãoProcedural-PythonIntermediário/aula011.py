"""
Geradores, Iteradores e Iteráveis Python
"""

lista1 = [0, 1, 2, 3, 4, 5]
print(hasattr(lista1, '_iter_'))
print(hasattr(lista1, '_next_'))

lista2 = [1, 2, 3, 4, 5]
lista2 = iter(lista2)
print(next(lista2))
print(next(lista2))
print(next(lista2))

import sys
import time

lista3 = list(range(10))
print(sys.getsizeof(lista3))  # Quantidade de memória


def gera():
    r = []
    for n in range(10):
        r.append(n)
        time.sleep(0.2)
    return r


g = gera()

for v in g:
    print(v)
print('-------------------')


def gerador():
    r = []
    for n in range(10):
        yield n
        time.sleep(0.2)
    return r

h = gerador()

print(next(h))
print(next(h))
print(next(h))
print('----------------------')

for v in h:
    print(v)

print('----------------------')

lista = [x for x in range(1000)]
print(type(lista))
print(sys.getsizeof(lista))
lista = (x for x in range(1000))
print(type(lista))
print(sys.getsizeof(lista))

print('-' * 30)







