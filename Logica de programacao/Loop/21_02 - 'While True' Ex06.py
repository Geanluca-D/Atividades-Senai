# 6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até
# que o usuário informe um valor válido.

nota = int(input('Digite uma nota de 1 a 10: '))

while nota < 1 or nota > 10:
  nota = int(input('Valor inválido, digite novamente: '))

print('Valor válido!')