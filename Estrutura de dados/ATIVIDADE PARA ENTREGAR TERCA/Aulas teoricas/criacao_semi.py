#SEMI ESTRUTURADO
#JSON

import pandas as pd

#========== ESTRUTURA DE DICIONÁRIO ===================
dados_json1 = {
    'Nome': ['Geanluca', 'Douglas', 'Jonas', 'Gabriel'],
    'Idade': [20, 19, 15, 26],
    'Cidade': ['Sao Paulo', 'Sao Caetano', 'Sao Bernardo', 'Tokyo']
}
#======================================================

df_json = pd.DataFrame(dados_json1)

#========== SALVAR EM JSON ============================
df_json.to_json('dadosSemi.json', orient='records', lines=False)
#Define o nome do arquivo e a forma em que os dados vão ser salvos (records = registros)
#======================================================