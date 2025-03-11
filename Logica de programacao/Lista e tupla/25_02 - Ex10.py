# 10. Ordenar uma lista de números em ordem crescente e decrescente.

n = [16 , 92, 43, 75, 13]
nCopia = n.copy()
cres = []
decr = []

for i in n:
  if len(n) != 0:
    cres.append(min(n))
    n.remove(min(n))
print(cres)

for i in n:
  if len(nCopia) != 0:
    decr.append(max(nCopia))
    nCopia.remove(max(nCopia))
print(decr)