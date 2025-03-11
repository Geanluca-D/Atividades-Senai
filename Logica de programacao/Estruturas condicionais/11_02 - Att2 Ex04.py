#EX04

sal = float(input('Digite o seu salário: '))
temp = float(input('Digite seu tempo de serviço em anos: '))

if temp < 1 :
  print('O bônus salárial não é aplicável a você')
elif temp >= 1 and temp <= 3 :
  nsal = sal + sal * 0.05
  print(f'O seu bônus é de 5%, o seu novo salário é de {nsal}')
elif temp > 3 and temp <= 5 :
  nsal = sal + sal * 0.1
  print(f'O seu bônus é de 10%, o seu novo salário é de {nsal}')
else :
  nsal = sal + sal * 0.15
  print(f'O seu bônus é de 15%, o seu novo salário é de {nsal}')