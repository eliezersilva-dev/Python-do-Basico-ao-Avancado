"""
Trocando valores ente variáveie
"""

x = 'Eliezer'
y = 10
print(f'x = {x} z = {y}')
print()

# invertendo valores
z = x
x = y
y = z
print(f'x = {x} z = {y}')
print()

# invertendo valores em Python
x, y = y, x
print(f'x = {x} z = {y}')
print()

x = 'Eliezer'
y = 10
z = 'Silva'
print(f'x = {x} y = {y} z = {z}')
print()
x, y, z = z, x, y
print(f'x = {x} y = {y} z = {z}')
print()



