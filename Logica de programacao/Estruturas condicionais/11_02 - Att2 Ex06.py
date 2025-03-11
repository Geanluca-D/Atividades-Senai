#DESAFIO

patente = str(input('Digite a patente: '))

#GENERAL
if patente == 'general' :
  print('Acesso total a zona de segurança')

#SOLDADO
elif patente == 'soldado':
  res1 = str(input('Está em missão especial?[S/N]: '))
  if res1 == 'S' :
    res2 = str(input('Está acompanhado de um oficial superior?[S/N]: '))
    if res2 == 'S' :
      print('Acesso total a zona de segurança')
    else:
      print('Acesso negado, é necessário a presença de um oficial superior')
  else:
    print('Acesso negado, é necessário estar em uma missão especial para acessar a zona de segurança e ter a presença de um oficial superior')

#CIENTISTA
elif patente == 'cientista':
  res11 = str(input('Possui uma autorização secreta?[S/N]: '))
  if res11 == 'S' :
    res12 = str(input('Qual o nível de segurança?: '))
    if res12 > 5 :
      print('Acesso total a zona de segurança')
    else:
      res13 = str(input('Está acompanhado de uma escolta militar?[S/N]: '))
      if res13 == 'S' :
        print('Acesso total a zona de segurança')
      else:
        print('Acesso negado, é necessário a companhia de uma escolta militar se seu nível de segurança for menor do que 5')
  else:
    print('É necessário uma autorização secreta')

#CIVIL
elif patente == 'civil':
  res21 = str(input('Você é algum familiar direto de um militar?[S/N]: '))
  if res21 == 'S' :
    print('Acesso total a zona de segurança')
  else :
    res22 = str(input('Hoje é segunda-feira ou quinta-feira?[S/N]: '))
    if res22 == 'S':
      print('Acesso total a zona de segurança')
    else :
      print('É necessário ser algum familiar direto de um militar ou acessar o sistema as segundas ou quintas')

#CONSULTOR DE SEGURANÇA
elif patente == 'consultor de segurança':
  res31 = int(input('Apresente um código de acesso válido: '))

  if res31 == 1234 :
    print('Acesso total a zona de segurança')
  else :
    res32 = str(input('Está acompanhado de um militar de nível superior?[S/N]: '))
    if res32 == 'S' :
      print('Acesso total a zona de segurança')
    else :
      print('É necessário um código de acesso válido ou estar acompanhado de um militar de nível superior')
