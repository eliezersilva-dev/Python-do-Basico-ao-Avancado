"""
Composição
"""

from classes import Cliente, Endereco

cliente1 = Cliente('Eliezer', 41)
cliente1.insere_endereco('Ituverava', 'SP')
print(cliente1.nome, cliente1.idade)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Maria', 27)
cliente2.insere_endereco('Dourados', 'MS')
print(cliente2.nome, cliente2.idade)
cliente2.lista_endereco()
print()

cliente3 = Cliente('Rose', 34)
cliente3.insere_endereco('Uberlância', 'MG')
print(cliente3.nome, cliente3.idade)
cliente3.lista_endereco()
print()

