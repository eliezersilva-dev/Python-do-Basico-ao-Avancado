"""
Relação entre objetos
Agregação
"""

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Calça', 80)
p3 = Produto('Boné', 30)

carrinho.lista_produto()
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)
carrinho.lista_produto()
print(carrinho.soma_total())
