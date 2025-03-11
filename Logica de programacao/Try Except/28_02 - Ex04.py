# 4. Crie uma função divisao_segura(a, b) que retorne o resultado da divisão
# a / b.
# Se b for zero, a função deve retornar &quot;Erro: Divisão por zero não
# permitida!&quot;.

def divisao_segura(a,b):
  res = a/b
  return res

while True:
  try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print(divisao_segura(a,b))

  except ZeroDivisionError:
    print('Divisão por zero! Tente de novo')
    print()

  else:
    break