# Faça um programa que verifique e mostre os números entre 1.000 e 2.000
# que, quando divididos por 11 produzam resto igual a 2.

lista = []

for i in range(1000, 2001):
    if i % 11 == 2:
        lista.append(i)
print(f'Os números entre 1000 e 2000 que o resto da divisão por 11 é 2 são: {lista}')