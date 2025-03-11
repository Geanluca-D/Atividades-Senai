# Contar quantos números pares o usuário digitar. O programa deve
# contar quantos números pares o usuário inseriu. O usuário para
# digitando -1.

num = int(input('Digite um número: '))
cont = 0

while num != -1:
  if num % 2 == 0:
    cont += 1
    num = int(input('Digite outro número (ou digite -1 para sair): '))
  else:
    num = int(input('Digite outro número (ou digite -1 para sair): '))

print(f'A quantidade de números pares digitados foi de: {cont}')