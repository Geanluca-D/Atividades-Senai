#Ex12 Contar Vogais

palavra = str(input('Digite uma palavra: ')).lower()
vogais = 'aeio'
qnt = 0

for i in palavra:
  if i in vogais:
    qnt += 1

print(f'A palavra {palavra} tem {qnt} vogais')