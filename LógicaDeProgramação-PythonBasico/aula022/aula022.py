"""
Split, Join, Enumerate em Python
* Split - Dividir um objeto iterável
* Join - Juntar elementos uma lista
* Enumerate - Enumerar elementos da lista - desempacotamento
"""
# função strip remove espaço do início e do fim da string
# função capitalize inicia a string com maíscula

string1 = 'Pyhton é uma linguagem de programacao, poderosa'
lista1 = string1.split(' ')  # cada elemento em um índice
lista2 = string1.split(',')  # divide os indícies na virgula

print(lista1)
print(lista2)

string2 = 'Pyhton é uma linguagem de programacao'
lista3 = string2.split(' ')  # str em lista indicie no espaço
lista4 = ','.join(lista3)  # lista em str cada índice separado por vigula

print(string2)
print(lista3)
print(lista4)
print(type(lista4))

lista5 = [0, 1, 2, 3, 4, 5]
print(list(enumerate(lista5)))  # enumera elementos da lista - retorna tuplas

lista6 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for i, j in lista6:  # mesma coisa da função enumerate
    #print(i[0])
    print(i, j)

lista7 = ['Eliezer', 'João', 'Maria']
n1, n2, n3 = lista7
print(n1)
