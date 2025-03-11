# Faça um programa que leia 5 números e informe a soma e a média dos
# números.

num2 = 0

for i in range(1, 6):
    num = int(input('Digite um número: '))
    num2 += num
print(f'A média dos valores é de {num2/i}')