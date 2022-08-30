
#  crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
#  da função executada.

def func1(arg):
    print(arg)


def func2():
    return 'valor da função 1'


var = func2()
func1(var)
print('---------------------')


#  Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da
#  função2 executada. Faça a função1 executar duas funções que recebam um número
#  diferente de argumentos.

def funcao_mestre(arg1, arg2):
    print(arg1, arg2)


def funcao_saudacao():
    return 'Olá aluno'


def funcao_nome():
    nome_local = input('Nome: ')
    return nome_local


saudacao = funcao_saudacao()
nome = funcao_nome()
funcao_mestre(saudacao, nome)

