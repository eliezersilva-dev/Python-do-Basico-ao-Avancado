"""
Função Map
"""

from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x * 2, lista)  # usando map
# nova_lista = [x * 2 for x in lista] # usando comprehension
# print(lista)
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)
# precos = map(lambda p: p['preco'], produtos) # listando preço
# for preco in precos:
#     print(preco)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] + (p['preco'] / 100) * 5, 2)  # aplicando 5% usando round para arrendodar em 2 casas
#     return p                                                # outra fórmula pra calcular porcentagem  5% de x = x*1.05
#
# novos_produtos = map(aumenta_preco, produtos)
# for produto in novos_produtos:
#     print(produto)

nomes = map(lambda p: p['nome'], pessoas)
for i in nomes:
    print(i)

