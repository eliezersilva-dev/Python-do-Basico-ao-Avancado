"""
Tuplas
Similar a lista. A diferança é que a tupla não pode ser editada
"""

tupla1 = (1, 2, 3, 'Eliezer')  # pode ser criada sem parenteses tupla = 1, 2, 3, 'Eliezer'

print(tupla1)
print(tupla1[3])
print('--------------')

for v in tupla1:
    print(v)
print('--------------')

print(tupla1[2:])
print('--------------')

# Desempacotar tuplas segue o mesmo conceito de lista
n1, n2, *n3 = tupla1
print(n3)

#  Passando tupla para lista e vice versa

t1 = list(tupla1)
t1[3] = 'Eliezer Silva'
t1 = tuple(t1)
print(t1)
