
# SETTER = Configurando um valor (=) @xxxxx.setter setter configura
# GETTER = Obter um valor (.) @property getter lê

class Pessoa:
    def __init__(self, nome):
        self.nome = nome


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('Eliezer')

print(p1.nome)

