#Faça um programa que leia 5 números e informe o maior número.

lista = []
num2 = 0

for i in range(1, 6):
    num = int(input('Digite um número: '))
    if num > num2:
        maior = num
        num2 = num
print(maior)