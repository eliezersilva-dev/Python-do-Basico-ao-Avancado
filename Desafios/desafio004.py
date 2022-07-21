"""
Desafio contador
Crie um laço de repepição que tenha a seguinte saída:
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
# usando while
contador_progressivo = -1
contador_regressivo = 11

while contador_progressivo < 8 or contador_regressivo > 10:
    contador_progressivo += 1
    contador_regressivo -= 1
    print(contador_progressivo, contador_regressivo)

# usando for, enumerate e range
for j, i in enumerate(range(10, 1, -1)):
    print(j, i)


