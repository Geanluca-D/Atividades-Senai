#DADOS ESTRUTURADOS - CRIAÇÃO
# pip install pandas
# pip install openpyxl

import pandas as pd

#========== ESTRUTURA DE DICIONÁRIO ===================
dados_planilha1 = {
    'Nome': ['Geanluca', 'Douglas', 'Jonas', 'Gabriel'],
    'Idade': [20, 19, 15, 26],
    'Cidade': ['São Paulo', 'São Caetano', 'São Bernardo', 'Tokyo']
}
#======================================================


#========== DATAFRAME =================================
df_planilha1 = pd.DataFrame(dados_planilha1)   #Transforma os dados da planilha em uma tabela organizada de linhas e colunas tipo excel
#======================================================


#========== SALVA NO EXCEL ============================
with pd.ExcelWriter('Dados estruturados.xlsx') as writer: 
    df_planilha1.to_excel(writer, sheet_name='Planilha 1', index=False)   #Informações para a criação da planilha
    
#Pega as informações e transforma em um novo arquivo, ex: html, json, sql
#======================================================