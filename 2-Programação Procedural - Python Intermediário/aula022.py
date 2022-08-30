"""
Como criar módulos em Python
"""
# Exemplo:

import math

PI = math.pi

def dobra_lista(valor):
    return [i*2 for i in valor]

def multiplica_lista(valor):
    r = 1
    for i in valor:
        r *= i
    return r

lista = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(dobra_lista(lista))
    print(multiplica_lista(lista))
    print(PI)
