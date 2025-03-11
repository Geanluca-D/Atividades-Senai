#EX13

sal = float(input('Digite o seu salário: '))

if sal < 280 :
  aum = sal * 0.2
  nsal = sal + aum
  print(f'Seu antigo salário era de {sal}, houve um aumento de 20%, o valor do aumento foi de {aum}, seu novo salário é de {nsal}')
elif sal < 700 :
  aum = sal * 0.15
  nsal = sal + aum
  print(f'Seu antigo salário era de {sal}, houve um aumento de 15%, o valor do aumento foi de {aum}, seu novo salário é de {nsal}')
elif sal < 1500 :
  aum = sal * 0.10
  nsal = sal + aum
  print(f'Seu antigo salário era de {sal}, houve um aumento de 10%, o valor do aumento foi de {aum}, seu novo salário é de {nsal}')
else :
  aum = sal * 0.05
  nsal = sal + aum
  print(f'Seu antigo salário era de {sal}, houve um aumento de 5%, o valor do aumento foi de {aum}, seu novo salário é de {nsal}')