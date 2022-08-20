"""
Criando, lendo, escrevendo e apagando arquivos
Gerenciadores de contexto
https://docs.pyton.org/3/library/functions.html#open
"""

file = open('abc.txt', 'w+')  # Criando um arquivo txt "w" subscreve
file.write('Linha 1\n')  # Escrevendo no arquivo
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # Setando o cursor de leitura do Python
print(file.read())  # Lendo arquivo
print('-'*20)

file.seek(0, 0)
print(file.readline())  # Lendo linha
print(file.readline())
print('-'*20)

file.seek(0, 0)
print(file.readlines())  # Lendo linhas em forma de lista
file.seek(0, 0)
for i in file:  # Usando for para ler arquivo
    print(i)
print('-'*20)

# Usando bloco try
try:
    file.write('Linha 4\n')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()  # Fechando o arquivo

print('-'*20)


# Gerenciador de contexto
# Não precisa fechar o arquivo, a função with já fecha automaticamente
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())

print('-'*20)

with open('abc.txt', 'a+') as file:  # 'a' apendice(não subscreve)
    file.write('Outra linha\n')
    file.seek(0, 0)
    print(file.read())

# Apagando arquivos
# Importar 'os'
import os
os.remove('abc.txt')

print('-'*20)

# Manipulando arquivos json
# Importar JSON
import json

d1 = {
    'Pessoa1': {
        'nome': 'Eliezer',
        'idade': 41,
    },
    'Pessoa2': {
        'nome': 'Maria',
        'idade': 27
    }
}

print(d1)
d1_json = json.dumps(d1)  # Tranformando dicionário em json
# Criando um arquivo e salvando o json
with open('abc.json', 'w+') as file:
    file.write(d1_json)

# Acessando o json e transformando em lista para acessar as chaves
with open('abc.json', 'r') as file:
    d2_jason = file.read()
    d2_jason = json.loads(d2_jason)

print(d2_jason['Pessoa1'])









