"""
POO geral
métodos public, protected, private
Em Python não há o conceito de public, protected e private
assim, adotou-se a conveção de usar '_' private ou protected e
'__' para private muito privado
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
print()
print(bd.dados)

# bd.inserir_clientes(1, 'Eliezer')
# bd.inserir_clientes(2, 'Maria')
# bd.inserir_clientes(3, 'Carina')
# print(bd.dados)
# bd.lista_clientes()
# bd.apaga_cliente(3)
# bd.lista_clientes()
# print(bd.dados)

