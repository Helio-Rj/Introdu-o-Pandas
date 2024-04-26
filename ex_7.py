import pandas as pd

#  from IPython.core.display_functions import display
#  se quizer usar o 'display'

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Tabela do mês de dezembro apenas
tabela_vendas_dez = pd.read_excel('Vendas - Dez.xlsx')

tabela_vendas = tabela_vendas.append(tabela_vendas_dez)

# visualizar a base de dados
pd.set_option('display.max_columns', None)

#  Adicionando coluna nova a tabela a partir das que existem
tabela_vendas['Comissão'] = tabela_vendas['Valor Final'] * 0.5

#  Adicionando uma nova coluna a tabela com valor zerado
tabela_vendas.loc[:, 'Imposto'] = 0

#  Exibição de lojas/quantidade
lojas = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

tabela_vendas['Comissão'] = tabela_vendas['Comissão'].fillna(tabela_vendas['Comissão'].mean())

print(tabela_vendas)
