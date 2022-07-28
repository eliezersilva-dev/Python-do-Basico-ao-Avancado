"""
while em Python
Utilizado para realizar ações enquanto
uma condição for verdadeira - loop
sintaxe:
while <condição>:
    bloco
"""
# contar até 10
n1 = 0
while n1 <= 10:
    print(n1)
    n1 = n1 + 1
print('Terminou a contagem!')

# comando continue faz o cógido pular o bloco posterior ao comando
# exemplo contar até 10 e pular o número 3
n2 = 0
while n2 <= 10:
    if n2 == 3:
        n2 = n2 + 1
        continue
    print(n2)
    n2 = n2 + 1
print('Terminou a contagem!')

# o comando break interrompe a execução do loop
n3 = 0
while n3 <= 10:
    if n3 == 3:
        n2 = n2 + 1  # n2 += 1
        break
    print(n3)
    n3 = n3 + 1
print('Terminou a contagem!')

# Exemplo de aplicação do while:
while True:
    print()

    continuar = input('Calcular? [s/n] ')
    if continuar == 'n':
        print('Até logo.')
        break
    if continuar == 's':
        pass
    else:
        print('Digite [s] para sim ou [n] para não.\nReinicie o programa.')
        break

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador [+ - * /]: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Digite um operador válido.')





