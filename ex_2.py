import pandas as pd

#  from IPython.core.display_functions import display
#  se quizer usar o 'display'

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)

print(tabela_vendas.head(6))  # pode se escolher o N° de linhas para exibição em ordem crescente
print(tabela_vendas.shape)  # mostra quantas linhas e colunas a tabela tem
print(tabela_vendas.describe())  # Descrição completa para análise de dados
