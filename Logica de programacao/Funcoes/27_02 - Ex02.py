# Exercício 2: Crie uma função que receba um número e retorne "Par" se o
# número for par ou "Ímpar" se o número for ímpar.

def par (val):
  if val % 2 == 0:
    return 'par'
  else:
    return 'impar'

n = int(input('Digite um número: '))
print(f'O número {n} é {par(n)}')