#Ex10 Substituir Negativos

lista = []

for i in range(1,6):
  num = float(input('Digite um número: '))
  if num < 0:
    num = 0
    lista.append(num)
  else:
    lista.append(num)

print()
print(lista)