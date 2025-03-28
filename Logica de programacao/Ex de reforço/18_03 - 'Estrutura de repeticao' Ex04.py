#4. Faça um programa que leia 5 números e informe a soma e a média dos
#números.

soma = 0

for i in range(1, 6):
    n = int(input('Digite um número: '))
    soma += n

med = soma/i

print(f'A média dos valores informados é: {med}')