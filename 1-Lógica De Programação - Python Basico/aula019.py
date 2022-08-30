"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'EliezerLucas'

# usando while
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# usando for in
for letra in texto:
    print(letra)

# usando função range
for n in range(2, 10, 1):
    print(n)

# usando a função range para encontrar o múltiplo de um número
for i in range(10):
    if i % 8 == 0:
        print(i)








