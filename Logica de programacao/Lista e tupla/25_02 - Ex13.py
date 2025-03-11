# 13. Criar uma lista de números e imprimir apenas os números ímpares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impar = []

for i in lista:
  if i % 2 != 0:
    impar.append(i)
print(impar)