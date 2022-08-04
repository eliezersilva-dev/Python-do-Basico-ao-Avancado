"""
Função Reduce - Acumula valores
"""

from dados import pessoas, produtos, lista
from functools import reduce

# somar (acumular) todos valores de uma lista - usando for
# acumula = 0
# for i in lista:
#     acumula += i
# print(acumula)

# usando Reduce
# soma_lista = reduce(lambda x, y: y + x, lista, 0)
# print(soma_lista)

# somando preços de um dicionário
# soma_preco = reduce(lambda x, y: y['preco'] + x, produtos, 0)
# print(soma_preco)

# calculando a média da idade das pessoas de um dicionário
soma_idade = reduce(lambda x, y: y['idade'] + x, pessoas, 0)
print(soma_idade / len(pessoas))
