#  Formatação de stings
nome = 'Eliezer'  # str
idade = 42  # int
altura = 1.81  # float
e_maior = idade > 18  # bool
peso = 92
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior?:', e_maior)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{1} {0} {0} {2} {1}'.format(nome, idade, imc))
print('{i} {n} {n} {im} {i}'.format(n=nome, i=idade, im=imc))  # nomeando parametros



