#EX03

peso = float(input('Digite seu peso em kg: '))
alt = float(input('Digite sua altura em m: '))

imc = peso / (alt**2)

if imc < 18.5 :
  print('Abaixo do peso')
elif imc >= 18.5 and imc < 25 :
  print('Peso normal')
elif imc >= 25 and imc < 30 :
  print('Sobrepeso')
else :
  print('Obesidade')