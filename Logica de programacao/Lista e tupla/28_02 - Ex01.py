# 1. Crie uma função que recebe duas palavras e retorna True se forem
# anagramas uma da outra.

def anagrama (pala, pala2):
  lista = []
  lista2 = []

  for i in pala:
    lista.append(i)
  for i in pala2:
    lista2.append(i)

  if sorted(lista) == sorted(lista2):
    return 'true'
  else:
    return 'false'


palavra = (input('Digite uma palavra: '))
palavra2 = (input('Digite uma palavra: '))

print(f'As duas palavras são anagramas: {anagrama(palavra, palavra2)}')