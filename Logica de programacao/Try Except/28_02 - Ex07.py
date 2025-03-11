# 7. Crie uma função pegar_elemento(lista, indice) que retorna o elemento
# de uma lista na posição indice.
# Se o índice não existir, trate o erro.

lista = [1, 2, 3, 4, 5]

def pegar_elemento(lista, indice):
  res = lista[indice]
  return res

while True:
  try:
    print(lista)
    ind = int(input('Digite um indice para retornar algum número da lista: '))
    print(f'O número retornado foi: {pegar_elemento(lista, ind)}')
  except ValueError:
    print('Valor inválido! Tente novamente')
    print()
  except IndexError:
    print('Valor inválido! Tente novamente')
    print()
  else:
    break