# 4. Verificar se um número específico está presente na lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input('Digite um número para verificar se está na lista: '))
cont = 0

for i in lista:
  if i == n:
    print(f'O número {n} está na lista no índice {i-1}')
    cont += 1

if cont == 0:
  print(f'O número {n} não está na lista')