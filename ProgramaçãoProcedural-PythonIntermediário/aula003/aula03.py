"""
Funções em Python - def (parte 3)
args - kwargs
"""


def func1(a1, a2, a3, nome=None, a4=None):
    print(a1, a2, a3, nome, a4)
    return nome, a4


var = func1(1, 2, 3, nome='Eliezer', a4='4')
print(var[0], var[1])
print('--------------------------')

# _______________________________________________________________

lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
print(*lista) # pode-se utlilizar separador sep' '
print('--------------------------')

# ________________________________________________________________


def func2(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
# args = list(args)  # casting tupla para lista




func2(1, 2, 3, 4, 5)
# desempacotar lista dentro da função
# lista = [1, 2, 3, 4, 5]
# func2(*lista)

print('--------------------------')


def func3(*args, **kwargs):
    print(args)
    print(kwargs)

    nome = kwargs.get('nome')
    print(nome)


li = [1, 2, 3, 4, 5]
la = [10, 20, 30, 40, 50]
func3(*li, *la, nome='Eliezer', sobrenome='Silva')



