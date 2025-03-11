#Ex16 Inverter uma Palavra

palavra = str(input('Digite uma palavra: '))

palavra_invert = ''

for i in range(len(palavra)-1, -1, -1):
  palavra_invert += palavra[i]
print(palavra_invert)