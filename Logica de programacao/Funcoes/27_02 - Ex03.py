# Exercício 3: Crie uma função chamada media_lista que recebe uma lista de
# números e retorna a média deles.

def media_lista(numeros):
  med = 0
  for i in numeros:
    med += i
  med /= len(numeros)
  return med

lista = []
n = int(input('Digite um número para calcular a média: '))

while True:
  lista.append(n)
  n = int(input('Digite um número para calcular a média (digite 0 para cancelar): '))
  if n == 0:
    break

print(f'A média dos valores é {media_lista(lista)}')