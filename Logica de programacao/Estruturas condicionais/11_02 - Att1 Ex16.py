#EX16

idade = int(input('Digite sua idade: '))

if idade < 16 :
  print('Você é proibido de votar (proibido)')
elif idade < 18 :
  print('Você tem a opção de votar (optativo)')
elif idade < 65 :
  print('Você tem a obrigação de votar (Obrigatório)')
else :
  print('Você tem a opção de votar (optativo)')