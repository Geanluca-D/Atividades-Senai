# 3. Crie uma função calcular_media(numeros) que recebe uma lista de
# números e retorna a média.
# Se a lista estiver vazia, a função deve tratar a exceção e exibir uma
# mensagem adequada.

def calcular_media(numeros):
  med = 0
  for i in numeros:
    med += i
  med /= len(numeros)
  return med

while True:
  try:
    n = list(map(int, input('Digite uma lista de números entre espaços: ').split()))
    print(f'A média dos valores é {calcular_media(n)}')

  except ValueError:
    print('Valor inválido! Tente de novo')
    print()

  except ZeroDivisionError:
    print('Lista vazia! Tente de novo')
    print()

  else:
    break