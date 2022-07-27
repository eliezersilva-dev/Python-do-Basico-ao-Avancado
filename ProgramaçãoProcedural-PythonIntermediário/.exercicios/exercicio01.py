"""
# Crie uma função que exiba uma saudação com os parâmetros saudação e nome.

def saudacao(msg='Hello!', nome='Usuário'):
    print(msg, nome)


n_1 = input('Qual o seu nome? ')
saudacao('Olá', n_1)


# Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.

def soma(n1, n2, n3):
    return n1 + n2 + n3


numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))

print(f'A soma dos números informados é {soma(numero1, numero2, numero3)}.')


# Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
# percentual ex(10%). Retorne (return) o valor do primeiro número somado do
# aumento do percentual do mesmo.

def porcentagem(p1, p2):
    return ((p1 / 100) * p2) + p1


valor = float(input('Digite um valor: '))
porcento = float(input('Digite um valor de porcentagem: '))

print(f'{valor} + {porcento}% de {valor} = {porcentagem(valor, porcento)}')
"""

# # Fizz Buzz - Se o parâmetro da função for divisível por , retorne fizz,
# se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro
# da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário,
# retorne o número enviado.

def divisivel(v1):
    if v1 % 5 == 0 and v1 % 3 == 0:
        return f'FizzBuzz - {v1} é divisível por 3 e por 5'
    if v1 % 3 == 0:
        return f'Fizz - {v1} é divisível por 3'
    if v1 % 5 == 0:
        return f'Buzz - {v1} é divisível por 5'
    return v1


from random import randint

for i in range(10):
    valor_v1 = randint(0, 100)
    print(divisivel(valor_v1))
