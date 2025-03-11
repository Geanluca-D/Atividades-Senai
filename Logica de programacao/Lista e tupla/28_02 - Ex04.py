# 4. Crie uma função que recebe uma lista de palavras e junta tudo em uma
# única frase.

def frase(lista):
  fra = ''
  for i in lista:
    fra += f'{i} '
  return fra

lista = list(map(str, input('Digite uma lista de palavras entre espaços: ').split()))

print()
print(lista)
print(frase(lista))