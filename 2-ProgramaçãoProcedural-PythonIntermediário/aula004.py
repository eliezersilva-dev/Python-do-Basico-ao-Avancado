"""
Escopo local - dentro da função
Escopo global - fora da função
"""

variavel = 'valor'


def fun1():
    print(variavel)

def fun2():
    variavel = 'outro valor'
    print(variavel)

fun1()
fun2()

print(variavel)
print('__________________')

# passando o valor de uma variável local para outra função local

def func1():
    var_local = 'Eliezer Silva'
    return var_local

def func2(arg):
    print(arg)

var1 = func1()
func2(var1)
