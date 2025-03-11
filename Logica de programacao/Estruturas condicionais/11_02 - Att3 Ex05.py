#EX05

conta = float(input('Digite o valor da conta: '))

if conta > 100 :
  nconta = conta + conta * 0.1
  print(f'O valor da conta + a gorjeta é de {nconta}')
else :
  nconta = conta + conta * 0.05
  print(f'O valor da conta + a gorjeta é de {nconta}')