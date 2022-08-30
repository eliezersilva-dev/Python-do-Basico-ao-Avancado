"""
Funções Lambda - função anônima
"""


#  Função convencioanal
def funcao(arg1, arg2):
    return arg1 * arg2
var = funcao(2, 2)
print(var)

print('--------------------')

# Função lambda
a = lambda x, y: x * y
print(a(2, 2))

print('--------------------')

# Exemplo de uso:
lista = [['P1', 13],
         ['P2', 6],
         ['P3', 7],
         ['P4', 50],
         ['P5', 8]]


def func1(item): #  ordenando lista com função
    return item[1]

lista.sort(key=func1) #  O contrário seria lista.sort(key=func1, reverse=True)
print(lista)
print('--------------------')


# Ordenando com expressão lambda
lista.sort(key=lambda item: item[1])
print(lista)
print('--------------------')

# Ordenando a lista no print com a expressão sorted + lambda
print(sorted(lista, key=lambda i: i[1]))




