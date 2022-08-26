"""
Eliezer Silva
Desafio - Validador de CNPJ
___________________________
Exemplos de CNPJ:
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

Forma de calcular:

0  4  2  5  2  0  1  1  0  0  0  1  X  X
5  4  3  2  9  8  7  6  5  4  3  2
0  16 6  10 18 0  7  6  0  0  0  2 = 65
fórmula -> 11 - (65 % 11) = 1
Primeiro dígito = 1 (Se o dígito for maior que 9, ele se torna 0)

0  4  2  5  2  0  1  1  0  0  0  1  1  X
6  5  4  3  2  9  8  7  6  5  4  3  2 = 67
fórmula -> 11 - (65 % 11) = 10 (Se o resultado for maior que 9, ele se torna 0)
Segundo dígito = 0

Novo CNPJ + dígitos = 04.252.011/0001-10
CNPJ original = 04.252.011/0001-10
Válido
"""

import cnpj

cnpj1 = '04.252.011/0001-10'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')
