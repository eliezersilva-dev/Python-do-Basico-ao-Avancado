"""
Entrada de dados - Input
"""
# input('Qual o seu nome? ')

nome = input('Qual o seu nome? ')
print(f'Olá {nome}, tudo bem?')

idade = input('Qual a sua idade? ')  # a função input sempre retorna str
print(idade)
print(type(idade))

numero_1 = int(input('Digite um número: '))  # convertendo str em int - fazer "cast"
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)  # convertendo str em int
print(numero_1 + numero_2)



