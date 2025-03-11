#EX10

time1 = int(input('Digite os gols do primeiro time: '))
time2 = int(input('Digite os gols do segundo time: '))

if time1 > time2 :
  print('O primeiro time ganhou o jogo')
elif time1 == time2 :
  print('O jogo terminou em empate')
else :
  print('O segundo time ganhou o jogo')