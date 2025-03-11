#EX09

val = float(input('Digite o valor da conta: '))

if val > 150 :
  nval = val - 20
  print(f'Após o desconto o valor da conta ficou {nval}')
else :
  print('O valor não é aplicável a descontos')