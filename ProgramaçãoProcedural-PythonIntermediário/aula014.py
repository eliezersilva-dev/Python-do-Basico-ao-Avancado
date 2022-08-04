"""
Combinations, Permuttions e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem não importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Eliezer', 'Silva', 'Maria', 'João', 'Letícia']

for grupo in combinations(pessoas, 2):  # ordem não importa
    print(grupo)
print('-'*20)

for grupo in permutations(pessoas, 2):  # ordem importa
    print(grupo)
print('-' * 20)

for grupo in product(pessoas, repeat=2):  # ordem importa e repete valores
    print(grupo)
print('-' * 20)

