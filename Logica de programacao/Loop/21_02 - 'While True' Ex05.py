# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário
# digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

nant = ''
cont = 0

while True:
  num = int(input('Digite um número: '))
  cont += 1
  if nant == num:
    break
  else:
    nant = num

print(f'Foram enseridos {cont} números')