"""
Funções em Python - def (parte 2)
"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(10, 2)

if divide:
    print(divide)
else:
    print('Conta inválida.')


def var():
    return ('Eliezer', 'Silva')


A_var = var()
print(var, type(var))
