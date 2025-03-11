# Some todos os números pares de 1 a 100 e mostre o resultado.

num = 0
soma = 0

while num < 100:
  num += 1
  if num % 2 == 0:
    soma += num

print(f'A soma de todos os números pares de 1 a 100 é {soma}')