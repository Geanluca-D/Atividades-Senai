# 6. Crie uma função que recebe uma lista de palavras e retorna a palavra
# com mais letras.

def maisLetra(lista):
  maiorNome = max(lista, key=len)
  return maiorNome

lista = list(map(str, input('Digite uma lista de palavras entre espaços: ').split()))

print(f'O maior nome da lista é: {maisLetra(lista)}')