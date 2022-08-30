"""
Eliezer Silva
Exercício 05
Dado as listas some os valores dos produtos.
"""

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# # Formas comuns (ineficientes):

# total = 0
# for produto in carrinho:
#     total += produto[1]
# print(total)

# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))

total = sum([float(y) for x, y in carrinho])  # total = [(x,y) for x, y in carrinho]
print(total)
