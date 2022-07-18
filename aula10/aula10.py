"""
Operadores relacionais
== - Igual
>  - Maior que
>= - Maior e igual
<  - Menor que
<= - Menor e igual
!= - Diferente
Ao ser usado a expressão retorna expressão booleana
"""

print(2 == 2)
print(2 == '2')
print(2 > 2)
print(2 >= 2)
print(2 < 2)
print(2 <= 2)
print(2 != 2)

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#  idade limite para pegar empréstimo
idade_minima = 18
idade_maxima = 150

if idade < idade_minima:
    print(f'Olá {nome}. '
          f'Desculpe! Você não pode comprar cerveja.')
elif idade > idade_maxima:
    print(f'Olá Vovô!'
          f'O Senhor não pode comprar cerveja. '
          f'Que tal um whisky?')
else:
    print(f'Olá {nome}! '
    f'Você pode comprar cerveja. '
    f'Beba com moderação!')





