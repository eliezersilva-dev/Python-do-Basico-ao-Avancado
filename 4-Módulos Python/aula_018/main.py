import random
import string

digitos = string.digits
caracteres = string.ascii_letters
simbolos = '_-'

geral = digitos + caracteres + simbolos
print(''.join(random.choices(geral, k=13)))
