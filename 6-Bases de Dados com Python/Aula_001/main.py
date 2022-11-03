import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Eliezer", 90.5)')
# conexao.commit()

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 54.5))
#
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'João', 'peso': 25}
# )
#
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Rose', 'peso': 64}
# )
#
# conexao.commit()

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )

# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )
# conexao.commit()


# cursor.execute('SELECT * FROM clientes')
#
# for linha in cursor.fetchall():
#     identificador, nome, peso = linha
#     print(identificador, nome, peso)

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()

