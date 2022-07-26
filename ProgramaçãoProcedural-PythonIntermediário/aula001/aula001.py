"""
Funções em Python - def (parte1)
"""


def funcao():
    print('Hello World!')


funcao()
funcao()
funcao()


def saudacao(msg, nome):
    print(msg, nome)


saudacao('Olá!', 'Eliezer')
saudacao('Oi', 'João')


def frase(msg='Olá', nome='usuário'):
    print(msg, nome)


frase()
frase('Olá!', 'Eliezer')
frase('Eliezer', 'Olá!')
frase(nome='Zezinho', msg='Hi!')


def teste(msg='Olá.', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('a', '4')
    return f'{msg} {nome}'


print(teste('Ola', 'Eliezer'))

