# Exercício 5: Crie uma função chamada tabuada que recebe um número e
# imprime sua tabuada do 1 ao 10.

def tabuada (num):
  for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
  return ''

n = int(input('Digite um número para calcular sua tabuada: '))

print(tabuada(n))