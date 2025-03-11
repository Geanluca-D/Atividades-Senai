#EX09

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
med = nota1 + nota2 / 2

if med >= 7 :
  print(f'Sua média é de: {med}, parabéns, você foi aprovado!')
elif med >= 5 :
  print(f'Sua média é de: {med}, você está de recuperação')
else :
  print(f'Sua média é de: {med}, infelizmente você reprovou')