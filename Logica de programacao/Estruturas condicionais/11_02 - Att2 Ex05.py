#EX05

vel = float(input('Digite a velocidade do veículo: '))

if vel <= 40 :
  print('Baixa velocidade')
elif vel <= 80 :
  print('Velocidade moderada')
elif vel <= 120 :
  print('Velocidade alta')
else :
  print('Velocidade muito alta')