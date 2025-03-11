#EX12

idade = int('Digite a sua idade: ')

if idade <= 11 :
  print('Classificação etária: Criança')
elif idade <= 18 :
  print('Classificação etária: Adolescente')
elif idade <= 24 :
  print('Classificação etária: Jovem')
elif idade <= 40 :
  print('Classificação etária: Adulto')
elif idade <= 60 :
  print('Classificação etária: Meia idade')
elif idade > 60 :
  print('Classificação etária: Idoso')