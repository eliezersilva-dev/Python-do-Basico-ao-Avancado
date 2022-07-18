"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso(float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com chaves)
"""

nome = 'Eliezer'
idade = 41
altura = 1.81
peso = 90.0
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}.')
