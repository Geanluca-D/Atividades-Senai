#Ex11 Criar uma Sequência Numérica

lista = []
num = int(input('Digite um número: '))

for i in range(1,9999):
  if len(lista) < 10:
    if i % num == 0 :
      lista.append(i)

print(lista)