# 1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até
# esse número.

num = int(input('Digite um número: '))
par = 2

while True:
  if num % 2 == 0:
    print(par)
    par += 2
    if par > num:
      break
  else:
    num -= 1