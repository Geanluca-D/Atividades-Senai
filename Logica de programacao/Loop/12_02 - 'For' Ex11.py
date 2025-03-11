#EX11

palavra = input('Digite uma palavra: ').lower()
vogais = 'aeiou'
qnt = 0

for letra in palavra:
  if letra in vogais:
    qnt += 1

print(f'A palavra {palavra} tem {qnt} vogais')