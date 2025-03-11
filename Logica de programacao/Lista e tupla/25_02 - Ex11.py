# 11. Criar uma lista de 5 números e substituir o segundo elemento por um novo valor.

lista = [10 , 20, 30, 40, 50]

print(lista)
print()
n = int(input('Digite um número para substituir o segundo número da lista: '))

lista.insert(1, n)
lista.pop(2)

print(lista)