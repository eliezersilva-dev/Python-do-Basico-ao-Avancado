"""
Exercício 01
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

Exercício 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

Exercicio 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva 'Seu nome é muito curto'; se tiver entre 5 e 6 letras escreva
'Seu nome é normal; maior que 6 escreva 'Seu nome é muito grande'.
"""

print('Para começar por favor insira algumas informações.')

nome = input('Digite seu primeiro nome: ')
letras_nome = len(nome)
tamanho_nome = ''
if letras_nome <= 4:
    tamanho_nome = 'Seu nome é muito curto.'
elif letras_nome >= 5 or letras_nome <= 6:
    tamanho_nome = 'Seu nome é normal.'
else:
    letras_nome = 'Seu nome é muito grande.'

hora = input('Informe a hora. Formato (um número entre 00 - 23): ')
if hora.isdigit():
    hora = int(hora)
else:
    print('Hora informada inválida.')

saudacao = ''
if hora == 00 or hora <= 11:
    saudacao = 'Bom dia'
elif hora > 11 or hora <= 17:
    saudacao = 'Boa tarde'
elif hora > 17 or hora <= 24:
    saudacao = 'Boa noite'
else:
    saudacao = 'Hora inválida informada. Mais atenção no relógio.'

print(f'{nome} escolha um número inteiro positivo. Seu número não poderá ser negativo e \n'
      f'não poderá conter ponto ou vírgula.')

numero = input('Digite um número: ')
if numero.isnumeric():
    numero = int(numero)
else:
    print('Seu número não é inteiro. Número inválido. Reinicie o programa.')

if numero % 2 == 0:
    par_impar = 'par'
else:
    par_impar = 'impar'

print(f'{saudacao} {nome}. {tamanho_nome} O número que você escolheu é {par_impar}.')
