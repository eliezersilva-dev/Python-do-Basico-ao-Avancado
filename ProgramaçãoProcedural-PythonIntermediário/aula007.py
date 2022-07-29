"""
Dicionários - dict {'chave' : 'valor'}
* devem conter valores únicos
* suporta qualquer tipo de dados
* concatenar dicionários d1.update(d2)
* deletar chave d1.pop(chave)
* deletar último item d1.popitem()
"""

d1 = dict(chave1='Valor1', chave2='Valor2')  # criando dicionário
print(d1)
d1['nova_chave'] = 'Valor2'  # adicionando chave
print(d1)
print('-----------------')
d2 = {'str': 'valor',
      123: 'outro valor',
      (1, 2, 3, 4): 'Tupla'}
print(d2)
print(d2.get('str'))  # pegando valor
print('-----------------')
d2['str'] = 'Eliezer'  # mudando valor pela chave
print(d2)
print('-----------------')
del d2['str']  # deletando valor pela chave
print(d2)
print('-----------------')
d3 = dict(ID=10, Nome='Eliezer', Sobrenome='Silva')
print(d3)
print('Nome' in d3.keys())
print('Eliezer' in d3.values())  # retorna valor boleano
print(len(d3))  # função len conta quantos pares (chave/valor)
print('-----------------')

for i in d3:  # iterando sobre as chaves do dicionário
    print(i)
print('-----------------')

for i in d3.values():  # iterando sobre os valores do dicionário
    print(i)
print('-----------------')

for i in d3.items():  # iterando sobre as chaves e valores
    print(i)
print('-----------------')

for i, j in d3.items():  # desempacotar
    print(i, j)
print('-----------------')

clientes = {
    'cliente1': {
        'nome': 'Eliezer',
        'sobrenome': 'Silva'
    }, 'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira'
    }, 'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Santos'
    },
}

for chave, valor in clientes.items():
    print(f'Exibindo {chave}')
    for dados_chave, dados_valor in valor.items():
        print(f'\t{dados_chave} = {dados_valor}')
print('-----------------')
