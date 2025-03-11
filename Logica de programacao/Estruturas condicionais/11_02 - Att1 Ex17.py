#EX16/17

tel = str(input('Telefonou para a vítima?[S/N]: '))
loc = str(input('Esteve no local do crime?[S/N]: '))
mor = str(input('Mora perto da vítima?[S/N]: '))
dev = str(input('Devia para a vítima?[S/N]: '))
trab = str(input('Já trabalhou com a vítima?[S/N]: '))

lista = [tel, loc, mor, dev, trab]
qnt = lista.count('S' or 's')

if qnt == 2 :
  print('Você é um suspeito')
elif qnt == 3 or qnt == 4:
  print('Você é um cúmplice')
elif qnt == 5 :
  print('Você é o assassino!')
else :
  print('Você é inocente')