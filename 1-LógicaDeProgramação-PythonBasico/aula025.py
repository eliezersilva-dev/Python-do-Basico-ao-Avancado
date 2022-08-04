"""
estrutura condicional com operador 'or'
"""

nome = input('Qual o seu nome?')
if nome:
    print(nome)
else:
    print('Você não digitou nada.')

# simplificando com operador 'or'
nome1 = input('Digite seu nome: ')
print(nome or 'Você não digitou nada.')
