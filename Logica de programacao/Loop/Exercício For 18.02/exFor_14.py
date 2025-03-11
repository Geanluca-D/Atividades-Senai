# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

nota = float(input('Digite uma nota entre 0 e 10: '))

for i in range(1, 10):
    if nota >= 0 and nota <= 10:
        print('Valor válido!')
        break
    else:
        nota = float(input('Valor inválido!! Digite um novo valor válido: '))