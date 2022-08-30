"""
Lançando Exceções em Python
"""

# Levantando erro
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Erro: ', error)
print(divide(2, 0))

# Lançando o erro para fora do escopo do try (logando o error) usando 'raise'
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Erro dentro do escopo: ', error)
        raise
try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print('Fora do escopo:', error)


# Criar (levantar) sua própria exceção
def divide(n3, n4):
    if n4 == 0:
        raise ValueError('n2 não pode ser zero')
    return n3 / n4
# Logando minha própria exceção
try:
    print(divide(2, 0))
except ValueError as erro:
    print('Não divide por zero.')
    print('Logou o erro:', erro)


# Tratando um input não numérico com try

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converte_numero(input('Digite um número: '))
if numero is None:
    print('Valor digitado não é numérico.')

else:
    numero = numero + 2
    print(numero)
