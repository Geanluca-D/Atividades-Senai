# Faça um programa que receba a idade de 15 pessoas e que calcule e
# mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com
# relação ao total de pessoas:
#  Até 15 anos
#  De 16 a 30 anos
#  De 31 a 45 anos
#  De 46 a 60 anos
#  Acima de 61 anos

a15 = 0
a30 = 0
a45 = 0
a60 = 0
a61 = 0

for i in range(1, 16):
    idade = int(input('Digite a idade: '))
    if idade <= 15:
        a15 += 1
    elif idade <= 30:
        a30 += 1
    elif idade <= 45:
        a45 += 1
    elif idade <= 60:
        a60 += 1
    else:
        a61 += 1
print(f'Há {a15} pessoas quem tem até 15 anos')
print(f'Há {a30} pessoas quem tem entre 16 e 30 anos')
print(f'Há {a45} pessoas quem tem entre 31 e 45 anos')
print(f'Há {a60} pessoas quem tem entre 46 e 60 anos')
print(f'Há {a61} pessoas quem tem 61 anos ou +')

total = a15 + a30 + a45 + a60 + a61
perA15 = a15*100/total
perA61 = a61*100/total

print(f'Na primeira faixa etária há {perA15:.2f}% de pessoas, e na última faixa etária há {perA61:.2f}% de pessoas')