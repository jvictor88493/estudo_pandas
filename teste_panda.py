import pandas as pd
vendas = pd.read_excel('Vendas - Dez.xlsx')
lucro_total = vendas['Valor Final'].sum()
qtde_produto = vendas['Quantidade'].sum()
print('O valor total das vendas foi {}'.format(lucro_total))
print('O valor total das vendas foi {}'.format(qtde_produto))