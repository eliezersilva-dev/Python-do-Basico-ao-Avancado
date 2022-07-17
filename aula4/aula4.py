"""
Tipos de dados
str - string - Texto'assim' ou "assim"
int - inteiro - 12345 0 -1-2-3
float - real/ponto flutuante - 10.50 1.5 -10.10 0.0
bool - booleano/lógico - True/False
"""

print('Eliezer', type('Eliezer'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))

# type cast
print('10', type('10'), type(int('10')))

print("Nome: Eliezer", type('Eliezer'))
print("Idade: ", 41, type(41))
print("Altura :", 1.81, type(1.81))
print("Você é maior de idade? ", bool(41 > 18))


