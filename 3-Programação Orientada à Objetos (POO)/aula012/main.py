"""
Eliezer Silva
Aula 12
"""

from contaPoupanca import ContaPoupanca
from contaCorrente import ContaCorrente


cp = ContaPoupanca(111, 222, 0)
cp.depositar(100)
cp.sacar(110)
print('---------------')
cc = ContaCorrente(111, 333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)


