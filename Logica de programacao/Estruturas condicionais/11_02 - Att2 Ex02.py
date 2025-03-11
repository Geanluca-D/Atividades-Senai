#EX02

idade = int(input('Digite a sua idade: '))

if idade < 12 :
  print('Criança')
elif idade >= 12 and idade <= 17 :
  print('Adolescente')
elif idade >= 18 and idade <= 64 :
  print('Adulto')
else :
  print('Idoso')