# 7. Criar uma lista de strings e verificar quantas vezes uma palavra específica aparece.

palavra = ['mouse', 'teclado', 'monitor', 'mouse', 'mousepad', 'mouse']
cont = 0

for i in palavra:
  if i == 'mouse':
    cont += 1

print(f'A palavra mouse aparece {cont} vezes na lista')