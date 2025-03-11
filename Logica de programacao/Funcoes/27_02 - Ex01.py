# Exercício 1: Crie uma função que receba dois números como parâmetros e
# retorne a soma deles.

def soma (val, val2):
  res = val + val2
  return res

n = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

n3 = soma(n, n2)

print(f'A soma dos dois números é {n3}')