"""
Manipulando strings
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Links úteis
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

texto = 'Eliezer Lucas'  # indice começa em zero
print(len(texto))
print(texto[5])
print(texto[-1])
print(texto[0:14:2])
texto_novo = texto[2:9]  # fatiamento
print(texto_novo)

