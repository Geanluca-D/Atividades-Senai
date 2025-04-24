#SEMI ESTRUTURADO

import pandas as pd

df_semi = pd.read_json('dadosSemi.json')

print(df_semi.head(2))
print()
print(df_semi.tail(1))
print()
print(df_semi.loc[2])
print()

#O head limita a quantidade de retornos a partir do início da lista
#O tail limita a quantidade de retornos a partir do final da lista
#O loc retorna o valor do índice especificado