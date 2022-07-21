"""
Validador de CPF
Escreva um algoritimo que valide um CPF

Cálculo de validação:
CPF aleatório = 168.995.350-09
--------------------------------------------------------------------
1 * 10 = 10         #       1 * 11 = 11 <-
6 * 9  = 54         #       6 * 10 = 60
8 * 8  = 64         #       8 * 9 =  72
9 * 7  = 63         #       9 * 8 =  72
9 * 6  = 54         #       9 * 7 =  63
5 * 5  = 25         #       5 * 6 =  30
3 * 4  = 12         #       3 * 5 =  15
5 * 3  = 15         #       5 * 4 =  20
0 * 2  = 0          #       0 * 3 =  0
     + ----         #    -> 0 * 2 =  0
        297 = X                  + -----
                                     343 = z     (z % 11) - 11
formula:(x % 11) - 11 = y(11)
Se y for 0 ou 1, o primeiro dígito é [0] (zero).
Se for 2, 3, 4, 5, 6, 7, 8, 9, 10 ou > o dígito y é (x % 11) - 11
Nesse exemplo o primeiro dígito é igual a 0
"""

# Loop infinito
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
