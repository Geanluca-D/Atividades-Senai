# 1. Crie uma função chamada calculadora que receba três parâmetros: dois
# números e uma operação (+, -, *, /).
# A função deve retornar o resultado da operação, mas precisa tratar as
# seguintes exceções:
#  Divisão por zero (ZeroDivisionError)
#  Tipo de dado inválido (ValueError)

def calc(n,n2,op):
  if op == '+':
    res = n + n2
    return res

  elif op == '-':
    res = n - n2
    return res

  elif op == '*':
    res = n * n2
    return res

  elif op == '/':
    res = n / n2
    return res

try:
  num1 = float(input('Digite um número: '))
  ope = str(input('Digite o tipo de operação a ser realizado (+ - * /): '))
  num2 = float(input('Digite outro número: '))
  print(f'{num1} {ope} {num2} = {calc(num1, num2, ope)}')

except ValueError:
  print('Valor inválido!')

except ZeroDivisionError:
  print('Divião por 0')