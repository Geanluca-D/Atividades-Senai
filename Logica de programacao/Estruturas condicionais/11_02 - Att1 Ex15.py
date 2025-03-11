#EX15

tipoTemp = str(input('A temperatura a ser convertida está em fahrenheit ou em celsius? Digite F ou C: '))
temp = float(input('Digite o valor a ser convertido: '))

match tipoTemp :
  case 'F' :
    ntemp = (temp - 32) * 5/9
    print(f'{temp}°F equivale a {ntemp}°C')
  case 'C' :
    ntemp = (temp * 9/5) + 32
    print(f'{temp}°C equivale a {ntemp}°F')
  case _:
    print('O tipo de temperatura informado é inválido')