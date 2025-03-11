#Ex7 Contar Números Negativos

lista = []

for i in range(1,6):
  num = float(input('Digite um número: '))
  if num < 0:
    lista.append(num)
print(lista)