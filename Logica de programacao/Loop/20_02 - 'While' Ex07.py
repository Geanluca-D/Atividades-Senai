# Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
# um número até acertar. (Declare um valor e receba outro)

nsec = 7
num = int(input('Tente adivinhar o número de 1 a 10: '))

while num != nsec:
  num = int(input('Número errado, tente de novo: '))

print('Você acertou!!')