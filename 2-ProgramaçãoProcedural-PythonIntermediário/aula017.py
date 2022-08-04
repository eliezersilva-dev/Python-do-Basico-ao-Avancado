"""
Função Filter - usada para filtrar aquilo que se pede
"""

from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)  # filtrar itens maiores que 5 em lista
print(list(nova_lista))

# filtrar produtos maiores que 30
novos_produtos = filter(lambda x: x['preco'] > 30, produtos)
for i in novos_produtos:
    print(i)
# filtrar pessoas menores de 18 anos
menores = filter(lambda x: x['idade'] < 18, pessoas)
for i in menores:
    print(i)
