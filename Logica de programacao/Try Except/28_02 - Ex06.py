# 6. Crie uma função multiplicar(a, b) que retorna o produto de a e b.
# Se os valores não forem números, capture a exceção e exiba uma
# mensagem de erro.

def multiplicar(a, b):
  res = a*b
  return res

while True:
  try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print(f'{a} x {b} = {multiplicar(a,b)}')
  except ValueError:
    print('Valor inválido! Tente novamente')
    print()
  else:
    break
