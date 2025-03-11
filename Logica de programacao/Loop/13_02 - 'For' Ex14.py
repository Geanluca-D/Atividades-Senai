#Ex14 Contar Números Pares em uma Lista

lista = []

for i in range(1,6):
  num = float(input('Digite um número: '))
  if num % 2 == 0:
    lista.append(num)
print(f'Há {len(lista)} números pares')