#Faça um programa que leia 5 números e informe o maior número.

maior = 0

for i in range(1,6):
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n

print(f'O maior valor digitado é {maior}')