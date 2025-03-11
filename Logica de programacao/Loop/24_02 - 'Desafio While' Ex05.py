#5 Escreva um programa que leia um número inteiro positivo e determine se ele é um
#  quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).

n = int(input('Digite um número: '))
if (n**(1/2)) // 1 == (n**(1/2)) :
  print(f'O número {n} é um quadrado perfeito')
else:
  print(f'O número {n} não é um quadrado perfeito')