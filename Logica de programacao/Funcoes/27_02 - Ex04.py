# Exercício 4: Crie uma função que calcule o fatorial de um número.

def fatorial (num):
  res = 1
  for i in range(num, 1, -1):
    res *= i
  return res

n = int(input('Digite um número para calcular o fatorial: '))

print(f'{n}! = {fatorial(n)}')