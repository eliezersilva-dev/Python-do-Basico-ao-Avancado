"""
Eliezer Silva
Exercício 05 - Programação Procedural Python
Dada a entrada:
string = '012345678901234567890123456789012345678901234567890123456789'
Fazendo o uso de List Comprehension retorne a seguinte saída:
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
"""

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(string)
print(retorno)
