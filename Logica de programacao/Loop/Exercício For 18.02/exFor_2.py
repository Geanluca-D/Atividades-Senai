# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
lista = []

if num1 < num2:
    for i in range(num1+1, num2):
        lista.append(i)
    print(f'O intervalo de números inteiros é {lista}')
else:
    for i in range(num1-1, num2, -1):
        lista.append(i)
    print(f'O intervalo de números inteiros é {lista}')