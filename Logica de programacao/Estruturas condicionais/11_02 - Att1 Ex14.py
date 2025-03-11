#EX14

dia = str(input('Digite um número de 1 a 7: '))

match dia :
  case '1' :
    print('Este número equivale ao Domingo')
  case '2' :
    print('Este número equivale a Segunda-Feira')
  case '3' :
    print('Este número equivale a Terça-Feira')
  case '4' :
    print('Este número equivale a Quarta-Feira')
  case '5' :
    print('Este número equivale a Quinta-Feira')
  case '6' :
    print('Este número equivale a Sexta-Feira')
  case '7' :
    print('Este número equivale ao Sábado')
  case _ :
    print('Valor inválido')