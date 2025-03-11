# 5. Crie uma função soma_lista(numeros) que recebe uma lista de números
# e retorna a soma.
# Se a lista contiver valores inválidos, capture a exceção e exiba uma
# mensagem de erro.

def soma_lista(numeros):
  soma = 0
  for i in numeros:
    soma += i
  return soma

while True:
  try:
    n = list(map(int, input('Digite uma lista de números entre espaços: ').split()))
    print(f'A soma dos valores é {soma_lista(n)}')
  except ValueError:
    print('Valor inválido! Tente de novo')
    print()
  else:
    break