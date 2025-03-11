# 22. Criar uma lista de frutas e verificar se &quot;banana&quot; está presente.

frutas = []

for i in range(1, 6):
  f = str(input(f'Digite uma fruta ({i}/5): '))
  frutas.append(f)

if 'banana' in frutas:
  print('Banana foi uma das frutas digitadas')
else:
  print('Banana não foi uma das frutas digitadas')