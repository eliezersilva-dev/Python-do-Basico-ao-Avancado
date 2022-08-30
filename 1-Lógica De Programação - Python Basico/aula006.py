"""
Iniciar com letra, pode conter números, separar_, letras minúsculas
"""
nome = 'Eliezer'
print(nome, type(nome))
idade = 42
altura = 1.81
e_maior = idade > 18
peso = 92
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior?:', e_maior)

print('Seu nome é', nome, ','' sua idade é de ', idade, ' anos', 'e seu IMC é', int(imc))


