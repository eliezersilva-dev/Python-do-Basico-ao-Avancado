
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print('Comprando...')


class ClienteVIP(Cliente):
    def falar(self):
        super(ClienteVIP, self).falar()
        print('Falando outra coisa...')


class Aluno(Pessoa):
    def estudar(self):
        print('Estudando...')

class AlunoVIP(Aluno):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
