# 7. Crie uma função que recebe uma lista de números e retorna a soma
# apenas dos números pares.

def par(lista):
  pares = 0
  for i in lista:
    if i % 2 == 0:
      pares += i
  return pares

lista = list(map(int, input('Digite uma lista de números entre espaços: ').split()))

print(f'A soma dos números pares é {par(lista)}')