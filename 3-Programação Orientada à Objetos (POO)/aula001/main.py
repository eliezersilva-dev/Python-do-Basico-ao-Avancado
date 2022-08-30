"""
Classes
"""
from pessoa import Pessoa

p1 = Pessoa('Eliezer', 41)  # mesmo que: p1.nome = 'Eliezer' p1.idade = 41
p2 = Pessoa('Maria', 27)
print('------------')

p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('outra coisa')
p1.comer('outra coisa de novo')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
print(f'{p2.nome} nasceu no ano de {p2.ano_nascimento()}')
print('------------')

p2.falar('POO')
p2.comer('abóbora')
p2.para_falar()
p2.comer('abóbora')
p2.parar_comer()
print(f'O ano de nascimento de {p1.nome} é {p1.ano_nascimento()}')
print('------------')
