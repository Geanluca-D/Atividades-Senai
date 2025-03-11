# 3. Crie uma função que recebe uma lista de números e retorna a
# quantidade de números que são múltiplos de 3.

def mult(lista):
  cont = 0
  for i in lista:
    if i % 3 ==0:
      cont += 1
  return cont

lista = list(map(int, input('Digite uma lista de números entre espaços: ').split()))

print(f'Há {mult(lista)} números da lista que são multiplos de 3')