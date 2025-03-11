#1 Escreva um programa que leia um número N e imprima todos os termos da sequência de
#  Fibonacci até que o maior termo seja menor ou igual a N.

n = int(input('Digite um número: '))
fib = 0
fib2 = 1
fib3 = 1

while True:
  print(fib3)
  fib3 = fib + fib2
  fib = fib2
  fib2 = fib3
  if fib3 > n:
    break