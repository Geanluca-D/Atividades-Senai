# Exercício 6: Crie uma função que receba uma string e retorne True se ela for
# um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para
# frente) e False caso contrário.

def inverter (texto):
  return texto[::-1]

text = (input('Digite um texto: '))

if text == inverter(text):
  print(f'O texto {text} é um palíndromo')
else:
  print(f'O texto {text} não é um palíndromo')