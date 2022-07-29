"""
Eliezer Silva
Sistema de perguntas e respostas
"""
print()
print('---------- Perguntas ---------')
print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 3 * 2 - 4 ?',
        'respostas': {'a': '4', 'b': '2', 'c': '6'},
        'resposta_certa': 'b'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 9 * 5 - 2 ?',
        'respostas': {'a': '43', 'b': '54', 'c': '68'},
        'resposta_certa': 'a'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8 * 2 + 8 / 4 ?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    },
}

resposta_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns! Resposta certa.')
        resposta_certas += 1
    else:
        print('Ops! Resposta errada')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas / qtd_perguntas * 100

print(f'Você acertou {resposta_certas} respostas. '
      f'Sua taxa de acerto foi de {porcentagem_acerto}%')
