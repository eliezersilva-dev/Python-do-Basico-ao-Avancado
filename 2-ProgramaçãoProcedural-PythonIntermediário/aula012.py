"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Ituverava']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
print(cidades_estados)
print(list(cidades_estados))

from itertools import zip_longest, count

indice = count()

cidades_estados = zip(   # ou zip_longest mas usado com count pode gerar um loop infinito
    indice,
    cidades,
    estados)  # zip_longest substitui o valores faltantes por none
              # setar none: fillvalue= '..'

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)









