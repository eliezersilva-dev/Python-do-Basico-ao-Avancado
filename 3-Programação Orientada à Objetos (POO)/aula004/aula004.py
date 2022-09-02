"""
Atributos de Classes
"""


class A:
    vc = 123


a1 = A()
a2 = A()
a3 = A()
print(a1.vc)
print(a2.vc)
print(A.vc)
a1.vc = 456
print(a1.vc)
print(a2.vc)
A.vc = 999
print(a1.vc)
print(a2.vc)
print(a3.vc)


