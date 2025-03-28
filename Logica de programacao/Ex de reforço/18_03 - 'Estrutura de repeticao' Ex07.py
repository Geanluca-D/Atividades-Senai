#7. Faça um programa que imprima na tela apenas os números ímpares entre
#1 e 150.

lista = []
print('Números impáres entre 1 e 150:')
for i in range(1, 151):
    if i % 2 != 0:
        lista.append(i)

print(lista)