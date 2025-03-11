#Ex20 Contar uma Letra em uma Frase

frase = str(input('Digite uma frase: ')).lower()
letra = str(input('Digite a letra a ser contada: ')).lower()

for i in frase:
  qnt = frase.count(letra)
print(f'A letra {letra} aparece {qnt}x na frase')