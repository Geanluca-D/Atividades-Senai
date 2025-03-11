# Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

idade2 = 0

for i in range(1, 11):
    idade = int(input('Digite a idade: '))
    idade2 += idade
med = idade2 / i

if med <= 25:
    print(f'A média de idade da turma é {med}, a turma é jovem')
elif med <= 60:
    print(f'A média de idade da turma é {med}, a turma é adulta')
else:
    print(f'A média de idade da turma é {med}, a turma é idosa')