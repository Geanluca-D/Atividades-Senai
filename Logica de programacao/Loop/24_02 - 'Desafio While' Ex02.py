#2 Escreva um programa que leia um número inteiro positivo e determine se ele é um
#  palíndromo (ou seja, se lido de trás para frente continua igual).

n = str(input('Digite um número: '))

n_invert = ''

for i in range(len(n)-1, -1, -1):
  n_invert += n[i]
if n_invert == n:
  print(f'O número {n} é um palíndromo')
else:
  print(f'O número {n} não é um palíndromo')