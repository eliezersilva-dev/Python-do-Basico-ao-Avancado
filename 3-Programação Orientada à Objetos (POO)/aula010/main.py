"""
Herança simples e Sobreposição de membros
Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É
"""

from classes import *

# cliente1 = Cliente('Eliezer', 41)
# print(cliente1.nome)
# cliente1.falar()
# cliente1.comprar()
#
# print()
#
# aluno1 = Aluno('Maria', 27)
# print(aluno1.nome)
# aluno1.falar()
# aluno1.estudar()
#
# print()
#
# pessoa = Pessoa('Rose', 34)
# print(pessoa.nome)
# pessoa.falar()

c2 = ClienteVIP('Joaquim', 53)
print(c2.nome)
c2.falar()

a1 = AlunoVIP('Karina', 35, 'Matos')
print(a1.nome, a1.sobrenome)
a1.falar()


