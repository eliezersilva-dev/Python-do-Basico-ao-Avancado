"""
Relações entre ente objetos
Associação
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaEscrever

escritor = Escritor('João Farelo')
caneta = Caneta('Azul')
maquina = MaquinaEscrever()

print(escritor.nome)
print(caneta.cor)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()




