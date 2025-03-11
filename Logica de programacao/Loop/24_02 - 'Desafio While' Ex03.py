#3 Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.

n = str(input('Digite um número: '))
lista = []

for i in range(len(n)):
  lista.append(n[i])

print(f'O número {n} tem {len(lista)} dígitos')