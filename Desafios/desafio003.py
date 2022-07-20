# Jogo da forca

import random

lista_palavras = ['perfume', 'banana', 'chicote', 'planeta', 'eliezer', 'xadrez', 'boneca', 'telefone', 'caneta', 'laranja']
secreto = random.choice(lista_palavras)
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('Você perdeu! Tente novamente.')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower()

    if letra not in secreto:
        chances = chances - 1

    if len(letra) > 1:
        print('Ahh! isso não vale. Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuu! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Aff! A letra "{letra}" não exista na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra in secreto:
        if letra in digitadas:
            secreto_temporario += letra
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal!! Você ganhou!!')
        print(f'A palavra secreta era "{secreto_temporario}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    print(f'Você ainda tem {chances} chances.')
    print()


