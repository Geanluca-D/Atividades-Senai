# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

par = []
impar = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'A quantidade de números pares é {len(par)}, e a de números ímpares é {len(impar)}')