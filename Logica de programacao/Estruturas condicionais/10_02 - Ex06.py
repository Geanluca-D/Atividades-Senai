#EX06

senha = int(input('Digite a senha: '))

match senha :
  case 1234 :
    print('ACESSO PERMITIDO')
  case _ :
    print('ACESSO NEGADO')