#EX11

turno = str(input('Digite o turno em que você estuna no seguinte formato: matutino = M, vespertino = V, noturno = N.: '))

match turno:
  case 'M':
    print('Bom dia!')
  case 'V':
    print('Boa tarde!')
  case 'N':
    print('Boa noite1')
  case _:
    print('Valor inválido!')