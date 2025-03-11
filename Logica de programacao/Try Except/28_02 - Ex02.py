# 2. Crie uma função ler_inteiro() que solicita ao usuário um número inteiro.
# Se o usuário inserir um valor inválido (não inteiro), exiba uma mensagem
# e peça a entrada novamente até que um número válido seja fornecido.


def ler_inteiro():
  n = int(input('Digite um número inteiro: '))
  print('O número digitado é inteiro')

while True:
  try:
    ler_inteiro()

  except ValueError:
    print('Valor inválido! Tente de novo')
    print()

  else:
    break