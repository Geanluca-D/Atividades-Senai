#Somar números até o usuário digitar 0. Peça números ao usuário e
#some-os até que ele digite 0.

num = int(input('Digite um número: '))
soma = 0

while num != 0:
  soma += num
  num = int(input('Digite outro número(digite 0 para sair): '))
print(f'A soma dos números digitados é: {soma}')