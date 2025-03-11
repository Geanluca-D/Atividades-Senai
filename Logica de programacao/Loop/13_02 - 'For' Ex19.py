#Ex19 Calcular o Fatorial

num = int(input('Digite um número: '))
num2 = num

for i in range(num-1, 0, -1):
  num2 *= i
print(f'!{num} = {num2}')