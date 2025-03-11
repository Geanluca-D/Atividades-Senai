# 28. Criar uma lista vazia e adicionar 3 elementos nela.

lista = []

for i in range(1, 4):
  add = str(input(f'Digite um valor a ser adicionado a lista ({i}/3): '))
  lista.append(add)

print(lista)