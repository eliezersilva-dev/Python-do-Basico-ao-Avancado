"""
Groupby - Agrupando valores
"""

from itertools import groupby

alunos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'José', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Henrique', 'nota': 'D'},
    {'nome': 'Silva', 'nota': 'B'},
    {'nome': 'Eliezer', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'C'},
    {'nome': 'Marta', 'nota': 'C'},
    {'nome': 'Carina', 'nota': 'D'}
]

# Ordenar lista com sort
alunos.sort(key=lambda item: item['nota'])

# Agrupando com groupby
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

# for i, j in alunos_agrupados:
#     print(f'Agrupamento: {i}')
#     for ii in j:
#         print(ii)

# Verificar quantos alunos tiraram determinada nota
# for i, j in alunos_agrupados:
#     print(f'Grupo: {i}')
#     quantidade = len(list(j))
#     print(f'{quantidade} alunos tiraram a nota {i}')


# Exemplo : Ordenar em grupos por idade
#
# from itertools import groupby
#
# pessoas = [
#     {'nome': 'luiz', 'idade': 30},
#     {'nome': 'joão', 'idade': 20},
#     {'nome': 'maria', 'idade': 40},
#     {'nome': 'helena', 'idade': 21},
#     {'nome': 'rosana', 'idade': 20},
#     {'nome': 'osvaldo', 'idade': 21},
#     {'nome': 'eleonor', 'idade': 40},
# ]
#
#
# def retorna_idade(pessoa):
#     return pessoa['idade']
#
#
# ordenadas_por_idade = sorted(pessoas, key=retorna_idade)
# agrupadas_por_idade = groupby(ordenadas_por_idade, key=retorna_idade)
#
# for idade, grupo in agrupadas_por_idade:
#     print(f'Grupo de pessoas de {idade} anos')
#
#     for pessoa in grupo:
#         print('\t', pessoa)
#
# """
# Saída:
#
# Grupo de pessoas de 20 anos
#          {'nome': 'joão', 'idade': 20}
#          {'nome': 'rosana', 'idade': 20}
# Grupo de pessoas de 21 anos
#          {'nome': 'helena', 'idade': 21}
#          {'nome': 'osvaldo', 'idade': 21}
# Grupo de pessoas de 30 anos
#          {'nome': 'luiz', 'idade': 30}
# Grupo de pessoas de 40 anos
#          {'nome': 'maria', 'idade': 40}
#          {'nome': 'eleonor', 'idade': 40}
# """

