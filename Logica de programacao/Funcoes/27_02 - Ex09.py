# Exercício 9: Crie uma função que conte quantas vogais existem em uma string
# fornecida.

def vogais (frase):
  v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  cont = 0
  for i in frase:
    if i in v:
      cont += 1
  return cont

frase = (input('Digite uma frase: '))
print(f'Há {vogais(frase)} vogais na frase digitada')