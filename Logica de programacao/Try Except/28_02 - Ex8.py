# 8. Crie uma função contar_caracteres(texto, caractere) que conta quantas
# vezes um caractere aparece em um texto.
# Se texto não for uma string, exiba um erro.

def contar_caracteres(texto, caractere):
  cont = 0
  for i in texto:
    if i == caractere:
      cont += 1
  return cont

while True:
  try:
    text = str(input('Digite uma frase: '))
    letra = str(input('Digite uma letra: '))
    if text == float or letra == float:
      print('Valor inválido! Tente novamente')
      print()

  except ValueError:
    print(f'A letra "{letra}" aparece {contar_caracteres(text, letra)} vezes')
    break

  else:
    break