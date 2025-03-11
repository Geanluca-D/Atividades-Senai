#Ex18 Criar um Triângulo Numérico

lista = []
num = int(input('Digite um número: '))
num2 = 0

for i in range(1,num+1):
  num2 += 1
  lista.append(num2)
  print(lista)