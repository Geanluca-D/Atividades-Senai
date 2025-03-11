# Encontrando o maior número inserido pelo usuário. Peça números ao
# usuário e, ao digitar 0, exiba o maior número inserido.

num = int(input('Digite um número: '))
maior = 0

while num != 0:
  if num > maior:
    maior = num
    num = int(input('Digite outro número (Ou digite 0 para sair): '))
  else:
    num = int(input('Digite outro número (Ou digite 0 para sair): '))

print(f'O maior número dentre os digitados é {maior}')