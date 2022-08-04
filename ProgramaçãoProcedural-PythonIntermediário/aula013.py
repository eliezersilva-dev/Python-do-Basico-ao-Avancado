"""
count - Itertools
contador built-in do Python
"""

from itertools import count

contador = count()  # start= - começo step= -  passo do contador

for valor in contador:
    print(round(valor, 2))  # função round arredonda, nesse caso setado em 2 casas decimais

    if valor >= 10:
        break

lista = ['Eliezer', 'João', 'Maria', 'Luiz', 'Márcia']
lista = zip(contador, lista)
print(list(lista))



