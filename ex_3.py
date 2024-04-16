import pandas as pd

#  from IPython.core.display_functions import display
#  se quizer usar o 'display'

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)

#  Exibição de lojas/quantidade
lojas = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(lojas.head(6))  # pode se escolher o N° de linhas para exibição em ordem crescente
print(lojas.shape)  # mostra quantas linhas e colunas a tabela tem
print(lojas.describe())  # Descrição completa para análise de dados
