"""
Classes
"""
from pessoa import Pessoa

p1 = Pessoa('Eliezer', 41)
p2 = Pessoa('Maria', 27)

print('-'*10)

p1.comer('maçã')
p1.comer('manga')
p1.parar_comer()
p1.comer('banana')
p1.falar('programação')
p1.parar_comer()
p1.falar('programação')
p2.falar(f'{p1.nome} nasceu no ano de {p1.ano_nascimento()}')



