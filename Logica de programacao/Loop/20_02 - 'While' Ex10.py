# Apenas aceitar números positivos. O programa deve continuar pedindo
# um número até o usuário digitar um número positivo.

num = int(input('Digite um número: '))

while num > 0:
  num = int(input('Digite um número (Digite um número negativo para sair): '))