# Exercício 8: Crie uma função que receba uma lista de notas e retorne a média
# das notas.

def media (lista):
  med = 0
  for i in lista:
    med += i
  med /= len(lista)
  return med

lista = []

while True:
  n = int(input('Digite as notas para tirar a média (digite -1 para cancelar): '))
  if n == -1:
    break
  else:
    lista.append(n)

print(f'A média das notas é {media(lista)}')