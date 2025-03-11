# 24. Verificar se duas listas são idênticas (mesmo tamanho e valores na mesma ordem).


#POSSIBILIDADE 3 - VALORES IGUAIS, COMPRIMENTO IGUAL
lista1 = [10 , 20, 30, 40, 50]
lista2 = [10 , 20, 30, 40, 50]

print(lista1)
print(lista2)

if lista1 == lista2:
  print('As duas listas são iguais')
else:
  print('As duas listas são diferentes')
print()

#POSSIBILIDADE 1 - VALORES DIFERENTE, COMPRIMENTO COINCIDE
lista3 = [10 , 20, 30, 40, 50]
lista4 = [13 , 24, 32, 45, 51]

print(lista3)
print(lista4)

if lista3 == lista4:
  print('As duas listas são iguais')
else:
  print('As duas listas são diferentes')
print()

#POSSIBILIDADE 3 - VALORES COINCIDEM, COMPRIMENTO DIFERENTE
lista5 = [10 , 20, 30, 40, 50]
lista6 = [20, 30, 40, 50]

print(lista5)
print(lista6)

if lista5 == lista6:
  print('As duas listas são iguais')
else:
  print('As duas listas são diferentes')
print()