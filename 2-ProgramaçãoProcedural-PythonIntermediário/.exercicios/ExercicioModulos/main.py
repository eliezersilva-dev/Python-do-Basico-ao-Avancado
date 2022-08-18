
from vendas.calc_preco import aumento, reducao
from vendas.formata import preco as formata

preco = 49.90
print(formata.real(preco))

preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(preco, 15, formata=True)
print(preco_com_reducao)
