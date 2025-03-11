# 25. Criar uma lista com 5 elementos e verificar se um número específico está presente.

lista = [10 , 20, 30, 40, 50]

n = int(input('Digite um número para verificar se está na lista: '))
print()

if n in lista:
  print(lista)
  print(f'O número {n} está na lista!')
else:
  print(lista)
  print(f'O número {n} não está na lista!')