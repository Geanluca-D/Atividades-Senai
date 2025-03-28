#2. Faça um programa que receba dois números inteiros e gere os números
#inteiros que estão no intervalo compreendido por eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n2 <= n1:
    print('Valores inválidos!')
else:
    print(f'Os números entre {n1} e {n2} são: ')

    for i in range(n1+1, n2):
     print(i)