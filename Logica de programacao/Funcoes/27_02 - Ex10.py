# Exercício 10: Crie uma função que receba uma lista de números e retorne essa
#lista ordenada em ordem crescente.

def numeros (lista):
  cres = sorted(lista)
  return cres

lista = []

while True:
  n = int(input('Digite um número (ou -1 para cancelar a ação): '))
  if n == -1:
    break
  else:
    lista.append(n)

print(numeros(lista))