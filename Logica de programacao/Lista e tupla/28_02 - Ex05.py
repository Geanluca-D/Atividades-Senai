# 5. Crie uma função que recebe uma lista de números e substitui os
# números negativos por zero.

def neg(n):
  lista = []
  for i in n:
    if i < 0:
      num = 0
      lista.append(num)
    else:
      num = i
      lista.append(num)
  return lista


n = list(map(int, input('Digite uma lista de números entre espaços: ').split()))

print(neg(n))