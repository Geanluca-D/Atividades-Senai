# 2. Crie uma função que recebe uma lista de números e retorna a
# quantidade de números positivos.

def pos(lista):
  cont = 0
  for i in lista:
    if i > 0:
      cont += 1
  return cont

lista = []

while True:
  n = int(input('Digite um número (ou 0 para cancelar a ação): '))
  if n == 0:
    break
  else:
    lista.append(n)

print(f'A quantidade de números positivos na lista é {pos(lista)}')