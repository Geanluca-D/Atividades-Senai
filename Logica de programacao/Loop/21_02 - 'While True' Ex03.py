# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o
# usuário digite -1. Em seguida, exiba a média das notas.

media = 0
div = 0

while True:
  num = int(input('Digite a nota para a média (digite -1 para terminar a entrada de valores): '))
  if num != -1:
    media += num
    div += 1
  else:
    break
print(f'A média das notas é {media/div}')