#Ex2
val1 = int(input('Digite um número: '))
oper = str(input('Digite um operador (+ - * /): '))
val2 = int(input('Digite outro número: '))

match oper :
  case '+' :
    res = val1 + val2
    print('O resultado é:', res)
  case '-' :
    res = val1 - val2
    print('O resultado é:', res)
  case '*' :
    res = val1 * val2
    print('O resultado é:', res)
  case '/' :
    res = val1 / val2
    print('O resultado é:', res)
  case _ :
    print('O operador é inválido')