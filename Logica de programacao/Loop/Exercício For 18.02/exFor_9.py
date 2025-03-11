# Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

cont = 0
num = int(input('Digite um número inteiro: '))

if num < 2:
    print(f'O número {num} não é primo')
else:
    for i in range(2, num):
        if num % i == 0:
            cont += 1

if cont == 0:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')