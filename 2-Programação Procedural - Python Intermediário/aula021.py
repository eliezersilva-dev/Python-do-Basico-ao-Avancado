"""
Módulos Padrão do Python
importando módulos
https://docs.python.org/3/py-modindex.html
"""
import random
import sys  # importa módulo inteiro
print(sys.platform)

from sys import platform  # importa os sub módulos (ctrl espaço após o import mostra opções)
print(sys.platform)

from sys import platform as so  # atribuindo 'apelido' para o módulo
print(so)

print('-'*20)

# gerando números aleatórios com o módulo random
import random

print(random.randint(0, 100))

for i in range(10):
    print(random.randint(0, 10))

