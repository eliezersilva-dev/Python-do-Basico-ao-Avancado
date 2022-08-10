"""
Try, Except - Tratando exceções em Python
Ao tratar o erro o programa continua rodando apesar do erro.
"""

# Pegando qualquer tipo de erro - Não é uma boa prática
try:
    print(a)
except:
    print('Erro')


# Tratando erros específicos e mostrando para o usuário
try:
    print(b)
except NameError as erro:
    print('Erro:', erro)

# Tratando erros inesperados
try:
    print(c)
except Exception as erro:
    print('Ocorreu um erro inesperado.')


# Usando else para retornar(qualquer coisa) em caso de não ocorrer erro
d = 'Hello'
try:
    print(d)
except Exception as erro:
    print('Erro')
else:
    print('Tudo ok.')


# Usando a cláusula Finally
# Executada de qualquer maneira, com ou sem erro, com ou sem else
# Muito útil para fechar arquivos ou conexão com bancos de dados
try:
    print(e)
except Exception as erro:
    print('Deu erro')
finally:
    print('Executei em Finally :)')
