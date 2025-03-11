# 16. Criar uma lista de nomes e exibir apenas os nomes que começam com a letra "A"

nomes = ['adriana', 'alencar', 'arthur', 'bruna', 'cezar', 'daniel', 'ester']
nCopia = nomes.copy()
a = []

for i in nomes:
  if i.startswith('a'):
    a.append(i)
print(a)