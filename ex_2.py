import pandas as pd

#  from IPython.core.display_functions import display
#  se quizer usar o 'display'

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)

# Comando que exibe as linhas que a condição pede
norte_shop = tabela_vendas.loc[tabela_vendas['ID Loja'] == 'Norte Shopping']

# Várias colunas e linhas
norte_shop2 = tabela_vendas.loc[tabela_vendas['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]

print(tabela_vendas)  # Tabela
print(tabela_vendas.head(6))  # pode se escolher o N° de linhas para exibição em ordem crescente
print(tabela_vendas.shape)  # mostra quantas linhas e colunas a tabela tem
print(tabela_vendas.describe())  # Descrição completa para análise de dados
print(tabela_vendas.loc[4:5])  # exibe as linhas pelos índeces da tabela
print(norte_shop)  # Várias colunas e linhas
print(norte_shop2)  # Várias colunas e linhas
print(tabela_vendas.loc[4, 'ID Loja'])  # Pegar Item específico
