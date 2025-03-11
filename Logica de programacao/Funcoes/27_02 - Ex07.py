# Exercício 7: Crie uma função que receba uma lista de números e retorne o
# maior número dessa lista.

#da para usar a função max, o código fica mais curto

def maior (lista):
  num = 0
  for i in lista:
    if i > num:
      num = i
  return num

lista = []

while True:
  n = int(input('Digite um número (digite 0 para cancelar): '))
  if n == 0:
    break
  else:
    lista.append(n)

print(f'O maior número da lista é {maior(lista)}')