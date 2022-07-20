"""
For / Else em Python
"""
variavel = ['Eliezer Silva', 'joazinho', 'Maria']

for valor in variavel:
    if valor.upper().startswith('J'):  # Função para verificar se um iterável começa com o parâmetro
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)

