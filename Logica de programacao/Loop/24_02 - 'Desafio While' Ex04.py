#4 Escreva um programa que leia um número inteiro positivo e determine se ele é um número
#  perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
#  mesmo) é igual ao próprio número.

n = int(input('Digite um número inteiro positivo: '))
soma = 0

for i in range(1, n):
  if n % i == 0:
    soma += i
if n == soma:
  print(f'O número {n} é perfeito')
else:
  print(f'O número {n} não é perfeito')