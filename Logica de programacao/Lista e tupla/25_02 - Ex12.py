# 12. Inverter a ordem dos elementos em uma lista.

lista = [10 , 20, 30, 40, 50]
lCopia = lista.copy()
invert = []

while len(invert) < len(lista):
  invert.append(lCopia[len(lCopia)-1])
  lCopia.pop(len(lCopia)-1)

print(invert)