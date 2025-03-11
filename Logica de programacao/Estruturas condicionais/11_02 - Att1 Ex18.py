#EX18

prod1 = float(input('Digite o valor do primeiro produto: '))
prod2 = float(input('Digite o valor do segundo produto: '))
prod3 = float(input('Digite o valor do terceiro produto: '))

if prod1 <= prod2 and prod1 <= prod3 :
  print('Você deveria comprar o primeiro produto')
elif prod2 <= prod1 and prod2 <= prod3 :
  print('Você deveria comprar o segundo produto')
else :
  print('Você deveria comprar o terceiro produto')