#Ex15 Exibir o dobro dos valores em uma lista

lista = []

for i in range(1,6):
  num = float(input('Digite um número: '))
  lista.append(num*2)
print(f'O dobro dos valores são: {lista}')