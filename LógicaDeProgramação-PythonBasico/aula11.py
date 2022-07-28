"""
Operadores lógicos
and, or - Tabela verdade
not - negação ou inversão
in e not in - dentro/ existe
"""
a = 2
b = 3
c = 4
d = ''
nome = 'Eliezer'

if a < b and b < c:
    print('Sucesso!')

if a < b or b > c:
    print('Estude a tabela verdade!')

if not a == b:
    print('Sucesso not')

if not d:
    print('Preencha o valor de d')

if 'z' in nome:  # Se z existe em nome
    print(f'Existe a letra Z em {nome}.')

if 'f' not in nome:  # Se f não existe em nome
    print(f'A letra F não existe em {nome}.')

# Exemplo simples de aplicação
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')
# Banco de dados
usuario_bd = 'Eliezer'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')





