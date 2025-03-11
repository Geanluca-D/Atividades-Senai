# 23. Criar uma lista de 5 números e calcular a média dos elementos.

lista = [10 , 20, 30, 40, 50]
soma = 0

for i in lista:
  soma += i

print(lista)
print(f'A média da lista é {soma/len(lista)}')