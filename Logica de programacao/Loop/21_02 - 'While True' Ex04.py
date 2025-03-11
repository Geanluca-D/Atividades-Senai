# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número
# negativo seja inserido. No final, exiba o maior número informado.

num = int(input('Digite um número: '))
maior = 0

while num > 0:
  if num > maior:
    maior = num
    num = int(input('Digite outro número (digite um número negativo para terminar a entrada de valores): '))
  else:
    num = int(input('Digite outro número (digite um número negativo para terminar a entrada de valores): '))

print()
print(f'O maior número digitado é {maior}')