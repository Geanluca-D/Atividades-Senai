# 5. Criar uma lista de números e imprimir apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []

for i in lista:
  if i % 2 == 0:
    par.append(i)

print(lista)
print()
print(par)