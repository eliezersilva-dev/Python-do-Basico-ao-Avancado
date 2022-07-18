"""
função len - quantidade de caracteres
function _len_()
"""

usuario = input('Digite seu usuário: ')
qtd_carcteres = len(usuario)

print(usuario, qtd_carcteres, type(usuario), type(qtd_carcteres))

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foram {len(string1) + len(string2)}')

