"""
Formatando valores com modificadores
:s - Texto (str)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (número)f - Quantidade de casas decimais (float)
: (carctere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
> - esquerda
< - direita
^ - centro
link útil - https://docs.python.org/pt-br/3/library/string.html
"""

nome = 'Eliezer Lucas'
print(nome)
nome_formatado = '{:#^30}'.format(nome)
print(nome_formatado)
print(nome.upper())

num1 = 10
num2 = 3
divisao = num1 / num2

print(divisao)
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print(f'{num2:0>10}')
print(f'{num2:0<10}')
print(f'{num2:0^10}')

