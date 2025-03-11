#Ex1

cat1 = int(input('Digite um dos lados do triângulo: '))
cat2 = int(input('Digite outro lado do triângulo: '))
hip = int(input('Digite o último lado do triângulo: '))

match (cat1 == cat2, cat1 == hip, cat2 == hip):
  case True, True, True :
    print('Esse é um triângulo equilátero')
  case (True, False, False) | (False, True, False) | (False, False, True) :
    print('Esse é um triângulo isósceles')
  case _:
    print('Esse é um triângulo escaleno')