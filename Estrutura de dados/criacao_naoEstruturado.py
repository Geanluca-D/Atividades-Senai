#DADOS NÃO ESTRUTURADO - CRIAÇÃO
#CSV

import pandas as pd

#========== ESTRUTURA DE DICIONÁRIO ===================
dados_csv = {
    'Nome': ['Geanluca', 'Douglas', 'Jonas', 'Gabriel'],
    'Idade': [20, 19, 15, 26],
    'Cidade': ['São Paulo', 'São Caetano', 'São Bernardo', 'Tokyo']
}
#======================================================

df_csv = pd.DataFrame(dados_csv)

#========== SALVA EM CSV ==============================
df_csv.to_csv('dadosNao.csv', index=False)
#======================================================